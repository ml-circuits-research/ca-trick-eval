#!/usr/bin/env python3
"""Build scores from explicit manual reviews, never from answer keyword matches."""
import argparse
import json
import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('review',type=Path); args=ap.parse_args()
    args.review=args.review.resolve()
    data=json.loads(args.review.read_text())
    saved_manifest=args.review.parent/'manifest.json'
    manifest={c['id']:c for c in json.loads((saved_manifest if saved_manifest.exists() else ROOT/'manifest.json').read_text())}
    counts=dict(pass_=0,partial=0,miss=0,fail=0)
    fooled=omitted=valid=extras=wrong_final=contradictory=0
    lines=[f'# Evaluare: {data["run_id"]}','',f'Model cerut: `{data["model"]}`; efort `medium`. O sesiune proaspătă per caz, secvențial.','',
           'Rubrică aplicată manual de agentul care a construit corpusul; nu este o evaluare independentă sau o măsurare statistică. Nu se deduce cauza internă doar din verdict.','',
           '| Caz | Pass | Partial | Miss | Fail | Verdict |','|---|---:|---:|---:|---:|---|']
    detail=[]
    for case_id in manifest:
        if case_id not in data['cases']: continue
        review=data['cases'][case_id]
        c=manifest[case_id]
        effective_run=review.get('run_id',data['run_id'])
        base=ROOT/'results'/case_id/'runs'/effective_run
        receipt=json.loads((base/'receipt.json').read_text())
        assert receipt['status']=='completed'
        assert receipt['model_requested']==data['model']
        if data.get('require_current_inputs'):
            assert set(receipt['input_sha256'])==set(c['files'])
            for name,digest in receipt['input_sha256'].items():
                assert hashlib.sha256((ROOT/'eval'/case_id/name).read_bytes()).hexdigest()==digest,(case_id,name)
        assert set(review['findings'])=={f['id'] for f in c['findings']}
        answer=(base/'answer.md').read_text()
        local=dict(pass_=0,partial=0,miss=0,fail=0)
        reference_link=f'../{case_id}/runs/{effective_run}/reference.md' if (base/'reference.md').exists() else f'../{case_id}/reference.md'
        detail += [f'## {case_id}','',f'Rulare: `{effective_run}`. [Răspuns brut](../{case_id}/runs/{effective_run}/answer.md) · [Etalon]({reference_link})','']
        for f_id,r in review['findings'].items():
            assert r['status'] in ('pass','partial','miss','fail')
            if r['quote']: assert r['quote'] in answer,(case_id,f_id,'quote not exact')
            assert r['reason']
            key='pass_' if r['status']=='pass' else r['status']
            local[key]+=1; counts[key]+=1
            detail += [f'**{f_id}: {r["status"]}** — {r["reason"]}','']
            if r['quote']: detail += ['> '+r['quote'].replace('\n','\n> '),'']
        assert review['additional_errors'] is not None
        for error in review['additional_errors']:
            assert error['severity'] in ('minor','material')
            assert error['quote'] in answer
            assert error['reason']
        has_error=bool(local['fail'] or any(e['severity']=='material' for e in review['additional_errors']))
        wrong_final+=review.get('outcome')=='wrong_final_verdict'
        contradictory+=review.get('outcome')=='contradictory_report'
        extras+=bool(review['additional_errors'])
        valid+=1; fooled+=has_error; omitted+=bool(local['miss'])
        verdict='păcălit' if has_error else ('omisiuni' if local['miss'] else ('incomplet' if local['partial'] else 'corect'))
        verdict={
            'wrong_final_verdict':'verdict final greșit',
            'wrong_executive_with_reservations':'executiv greșit; rezerve în corp',
            'contradictory_report':'contradicție; corecție ulterioară',
            'correct_with_omission':'verdict corect; omisiune',
            'correct':'corect',
        }.get(review.get('outcome'),verdict)
        lines.append(f'| {case_id} | {local["pass_"]} | {local["partial"]} | {local["miss"]} | {local["fail"]} | {verdict} |')
        detail += ['Afirmații suplimentare greșite:','']
        if not review['additional_errors']: detail += ['Nu am identificat.','']
        for error in review['additional_errors']:
            detail += [f'- **{error["severity"]}**: {error["reason"]}', '', '> '+error['quote'].replace('\n','\n> '),'']
        detail += [review['notes'],'']
        assessment='\n'.join(detail[detail.index(f'## {case_id}'):])+'\n'
        assessment=assessment.replace(f'../{case_id}/runs/{effective_run}/answer.md','answer.md').replace(reference_link,'reference.md' if (base/'reference.md').exists() else '../../reference.md')
        (base/'assessment.md').write_text(assessment)
    lines += ['',f'**Rapoarte cu erori materiale: {fooled}/{valid}.** Cazuri cu omisiuni: {omitted}/{valid}. Cazuri cu erori suplimentare, inclusiv minore: {extras}/{valid}.',
              '',f'Distincție explicită în evaluările care o folosesc: **{wrong_final} verdict(e) final(e) greșit(e)** și **{contradictory} raport(oarte) contradictoriu(ii), corectat(e) ulterior în același răspuns**.',
              '',f'Findings: {counts["pass_"]} pass, {counts["partial"]} partial, {counts["miss"]} miss, {counts["fail"]} fail.','',
              '## Limite și rulări excluse','',data['limitations'],'']+detail
    dest=args.review.parent/'summary.md'; dest.write_text('\n'.join(lines)+'\n')
    print(f'{wrong_final}/{valid} wrong final verdicts; {contradictory} contradictory reports; {counts}; {dest.relative_to(ROOT)}')
if __name__=='__main__': main()
