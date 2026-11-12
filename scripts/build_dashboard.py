#!/usr/bin/env python3
"""Build a static HTML evidence matrix from receipts and explicit manual assessments."""
import hashlib
import html
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MODELS=['gpt-6-luna','gpt-6.1-terra','gpt-6.1-sol','gpt-6-sol','gpt-6-astra']
def esc(s): return html.escape(str(s))
def link(path,label):
    return f'<a href="../{esc(path.relative_to(ROOT).as_posix())}">{esc(label)}</a>'
def revision(receipt):
    prompt_hash=hashlib.sha256((receipt['folder']/'prompt.md').read_bytes()).hexdigest()
    return hashlib.sha256(json.dumps({'files':receipt['input_sha256'],'prompt':prompt_hash},sort_keys=True).encode()).hexdigest()[:12]
def main():
    cases=json.loads((ROOT/'manifest.json').read_text())
    records=[]
    for c in cases:
        for p in sorted((ROOT/'results'/c['id']).glob('runs/*/receipt.json')):
            r=json.loads(p.read_text()); r['case']=c['id']; r['folder']=p.parent; r['run']=p.parent.name
            reviewfile=ROOT/'results'/r['run']/'review.json'
            review=json.loads(reviewfile.read_text()) if reviewfile.exists() else {}
            r['review']=review.get('cases',{}).get(c['id'])
            r['revision']=revision(r)
            r['current']=r['input_sha256']=={name:hashlib.sha256((ROOT/'eval'/c['id']/name).read_bytes()).hexdigest() for name in c['files']}
            records.append(r)
    rows=[]
    for c in cases:
        cells=[]
        for model in MODELS:
            runs=[r for r in records if r['case']==c['id'] and r['model_requested']==model and r['current']]
            completed=[r for r in runs if r['status']=='completed' and r['review']]
            errors=sum(r['status']!='completed' for r in runs)
            if completed:
                bad=sum(any(f['status'] in ('fail','miss','partial') for f in r['review']['findings'].values()) or any(e['severity']=='material' for e in r['review']['additional_errors']) for r in completed)
                material=any(any(f['status'] in ('fail','miss') for f in r['review']['findings'].values()) or any(e['severity']=='material' for e in r['review']['additional_errors']) for r in completed)
                css='bad' if material else ('incomplete' if bad else 'good')
                groups=[]
                for mode,profile,label in [(mode,profile,label+' / '+profile) for mode,label in [('strict','Izolare strictă'),('context','Separare de context')] for profile in ['forensic','standard']]:
                    group=[r for r in completed if r.get('isolation_mode','context')==mode and r.get('prompt_profile','forensic')==profile]
                    if group:
                        failures=sum(any(f['status'] in ('fail','miss') for f in r['review']['findings'].values()) or any(e['severity']=='material' for e in r['review']['additional_errors']) for r in group)
                        wrong=sum(r['review'].get('outcome')=='wrong_final_verdict' for r in group)
                        misses=sum(f['status']=='miss' for r in group for f in r['review']['findings'].values())
                        partials=sum(f['status']=='partial' for r in group for f in r['review']['findings'].values())
                        false_claims=sum(f['status']=='fail' for r in group for f in r['review']['findings'].values())+sum(e['severity']=='material' for r in group for e in r['review']['additional_errors'])
                        groups.append(f'{label}: {failures}/{len(group)} cu erori materiale/omisiuni<br><small>{wrong} verdicte false · {false_claims} afirmații false · {misses} omisiuni · {partials} incomplete</small>')
                value='<br>'.join(groups)
            else:
                css='pending'; value='În așteptarea evaluării' if any(r['status']=='completed' for r in runs) else 'Nicio rulare validă'
            if errors: value+=f'<br><small>{errors} eroare tehnică exclusă</small>'
            cells.append(f'<td class="{css}">{value}</td>')
        rows.append(f'<tr><th>{esc(c["title"])}<small>{esc(c["profile"])} · {len(c["findings"])} findinguri planificate</small></th>'+''.join(cells)+'</tr>')
    details=[]
    for r in records:
        review=r['review']; folder=r['folder']; status=r['status']
        links=[link(folder/'receipt.json','Configurație și hashuri'),link(folder/'input','Intrări'),link(folder/'reference.md','Etalon')]
        if (folder/'answer.md').exists(): links.append(link(folder/'answer.md','Răspuns brut'))
        if (folder/'assessment.md').exists(): links.append(link(folder/'assessment.md','Evaluare finding cu finding'))
        if status!='completed':
            links.append(link(folder/'stderr.log','Eroare tehnică'))
            incident=ROOT/'results'/r['run']/'infrastructure.md'
            if incident.exists(): links.append(link(incident,'Cauză și remediere'))
        isolation_label='izolare strictă verificată' if r.get('isolation_mode')=='strict' else 'separare de context; fără izolare strictă la citire'
        info=''
        provenance=''
        if r.get('cli_version'):
            code_revision=hashlib.sha256(json.dumps(r['source_sha256'],sort_keys=True).encode()).hexdigest()[:12]
            provenance=f'<p class="meta">CLI {esc(r["cli_version"])} · revizie cod runner/cazuri/izolare {code_revision}</p>'
        if review:
            counts={s:sum(f['status']==s for f in review['findings'].values()) for s in ('pass','partial','miss','fail')}
            bad=[fid+': '+f['status'] for fid,f in review['findings'].items() if f['status']!='pass']
            outcome_label={'correct':'Corect','correct_with_incomplete_finding':'Verdict corect; demonstrație incompletă','correct_with_material_error':'Verdict corect; eroare în demonstrație','correct_with_finding_error':'Verdict corect; finding greșit','correct_with_omission':'Verdict corect; finding omis','wrong_final_verdict':'Verdict final greșit','contradictory_report':'Raport contradictoriu'}.get(review['outcome'],review['outcome'])
            info=f'<p><b>{esc(outcome_label)}</b> · '+esc(' / '.join(f'{n} {s}' for s,n in counts.items()))+'</p>'
            info+='<p>'+esc('; '.join(bad) if bad else 'Toate findingurile planificate au fost găsite și demonstrate.')+'</p>'
            info+='<p>'+esc(review['notes'])+'</p>'
            for error in review['additional_errors']:
                info+='<p><b>Afirmație suplimentară greșită ('+esc(error['severity'])+'):</b> '+esc(error['reason'])+'</p><blockquote>'+esc(error['quote'])+'</blockquote>'
            extras=review.get('additional_findings',[])
            if extras: info+='<p>Findinguri suplimentare: '+esc('; '.join(x['claim']+' ['+x['status']+']' for x in extras))+'</p>'
        else: info='<p>'+('Rezultat tehnic invalid; exclus din evaluarea modelului.' if status!='completed' else 'Rulare completă; evaluare manuală în așteptare.')+'</p>'
        details.append(f'<article><h3>{esc(r["case"])} · {esc(r["model_requested"])}</h3><p class="meta">Rulare {esc(r["run"])} · revizie {r["revision"]} · {isolation_label} · profil {esc(r.get('prompt_profile','forensic'))} · efort {esc(r["reasoning_effort"])} · {r["duration_seconds"]} s · {esc(r["timestamp_utc"])} · {"intrări curente" if r["current"] else "intrări anterioare"}</p>{provenance}{info}<p>'+ ' · '.join(links)+'</p></article>')
    page='''<!doctype html><html lang="ro"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dosare · matrice Codex × model</title><style>
:root{font-family:system-ui,sans-serif;color:#152633;background:#f4f7f9;line-height:1.6}body{max-width:1180px;margin:auto;padding:32px 24px}h1{line-height:1.2;font-size:2.2rem}h2{margin-top:2rem}a{color:#075c9e}table{width:100%;border-collapse:collapse;background:white}th,td{padding:18px;text-align:left;border:1px solid #d9e1e6}th small{display:block;font-weight:normal;color:#526471}.good{background:#e1f4e8}.bad{background:#ffe8df}.incomplete{background:#fff4ce}.pending{background:#edf0f4}.scroll{overflow:auto}article{background:white;border:1px solid #d9e1e6;padding:18px 24px;margin:16px 0;border-radius:10px}article h3{margin-top:0}.meta,small{font-size:.85rem;color:#526471}code{overflow-wrap:anywhere}footer{margin-top:40px;color:#526471}@media(max-width:650px){body{padding:20px 12px}th,td{padding:12px;min-width:155px}h1{font-size:1.7rem}}
</style><h1>Review în orb al dosarelor</h1><p>Agentul primește numai dosarul și întrebarea beneficiarului. Refacem independent reviewul, apoi comparăm răspunsul cu findingurile planificate în <code>results/</code>. Nu cerem modificări de cod.</p><p><a href="research-plan.html">Protocolul nou și planul experimental</a> · <a href="pilot-report.html">Pilot controlat: rulări și rezultate</a></p><h2>Matrice caz × model</h2><p>Matricea numără rulările cu afirmații materiale false sau findinguri omise. Demonstrațiile incomplete sunt raportate separat și marcate cu galben. Omisiunile și demonstrațiile incomplete nu sunt echivalente cu un verdict fals; matricea și detaliile de mai jos le separă. Un finding parțial nu este prezentat ca martor al unei concluzii induse în eroare. Numărătorul este numărul rulărilor cu erori materiale sau omisiuni, numitorul este numărul rulărilor complete și evaluate pe intrările curente.</p><div class="scroll"><table><thead><tr><th>Dosar</th>'''+''.join('<th>'+esc(m)+'</th>' for m in MODELS)+'''</tr></thead><tbody>'''+''.join(rows)+'''</tbody></table></div><h2>Rulări și dovezi</h2><p>Fiecare revizie este derivată din hashurile fișierelor și ale promptului. Profilul forensic cere explicit independență, contradicții și consecvența rezumatului; standard este un brief obișnuit de review, cu aceleași documente și întrebări. Rezultatele profilurilor sunt separate. Modelul indicat este cel cerut CLI-ului, nu o verificare independentă a backendului. Protocolul folosește Codex exec, sesiuni noi, sandbox read-only, efort medium și aceleași întrebări pentru toate modelele. Separarea de context din rulările inițiale nu ascunde tehnic restul proiectului; logurile au fost auditate. Rulările marcate „izolare strictă” folosesc un filesystem separat cu bubblewrap: proiectul și rezultatele nu sunt montate, iar verificările sunt salvate în configurația rulării.</p>'''+''.join(details)+'''<h2>Limitele experimentului</h2><p>Corpus sintetic și construit adaptiv; evaluatorul este și autorul. Rezultatele sunt martori observați, nu rate generale de vulnerabilitate. Cedru, Aster, Montis și Dacia au fost retrase pentru lipsa unui eșec material ferm. Testele de format Caldera au fost abandonate la cererea utilizatorului. Criogena a fost retras după trei reviewuri corecte. Nadir este păstrat pentru o eroare explicită de demonstrație Luna, cu verdict final corect. Cazurile noi sunt candidați până la evaluare; o explicație incompletă nu este suficientă pentru a declara un atac reușit. Erorile tehnice sunt păstrate și excluse din numitor. Findingurile suplimentare se acceptă numai cu probe verificabile, separat de afirmațiile suplimentare false.</p><footer>Generat din manifest, receipt.json și review.json. <a href="../README.md">Protocol</a> · <a href="../archive/rejected-controls-20261112/README.md">Cedru și Aster</a> · <a href="../archive/rejected-montis-20261112/README.md">Montis</a> · <a href="../archive/rejected-dacia-20261112/README.md">Dacia</a> · <a href="../archive/abandoned-caldera-20261112/README.md">Caldera abandonat</a> · <a href="../archive/rejected-criogena-20261112/README.md">Criogena</a> · <a href="../archive/ten-dossiers-v1/README.md">Arhiva celor zece dosare anterioare</a></footer></html>'''
    out=ROOT/'docs'; out.mkdir(exist_ok=True)
    (out/'index.html').write_text(page)
    print('Generated docs/index.html')
if __name__=='__main__':main()
