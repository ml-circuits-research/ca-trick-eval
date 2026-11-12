"""Meaningful mutation tests of the experiment's fail-closed integrity checks."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from campaign_integrity import sha,verify_frozen,verify_allocation

class GuardTests(unittest.TestCase):
    def test_input_and_runtime_mutation_and_extra_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            project=Path(tmp);suite=project/'suite';case=suite/'eval'/'d1234';case.mkdir(parents=True)
            doc=case/'evidence.md';doc.write_text('Evidence, never the answer.')
            runtime=project/'runner.py';runtime.write_text('fixed runtime')
            freeze={'files':{'eval/d1234/evidence.md':sha(doc)},'runtime_sources':{'runner.py':sha(runtime)}}
            (suite/'freeze.json').write_text(json.dumps(freeze))
            verify_frozen(suite,project)
            doc.write_text('Changed after freeze')
            with self.assertRaises(AssertionError):verify_frozen(suite,project)
            doc.write_text('Evidence, never the answer.')
            runtime.write_text('changed runtime')
            with self.assertRaises(AssertionError):verify_frozen(suite,project)
            runtime.write_text('fixed runtime')
            extra=case/'reference.md';extra.write_text('Must be rejected')
            with self.assertRaises(AssertionError):verify_frozen(suite,project)
    def test_unallocated_or_misconfigured_run(self):
        frozen={'allocation':[{'run_id':'r','model':'m','case_ids':['c']}], 'case_ids':['c'],
                'prompt_profile':'standard','reasoning_effort':'medium','timeout_seconds':600}
        args=SimpleNamespace(run_id='r',model='m',cases=None,prompt_profile='standard',effort='medium',timeout=600)
        verify_allocation(frozen,args)
        for field,value in [('run_id','other'),('model','other'),('cases',['other']),('prompt_profile','forensic'),('effort','low'),('timeout',1)]:
            bad=SimpleNamespace(**(vars(args)|{field:value}))
            with self.assertRaises(AssertionError):verify_allocation(frozen,bad)
if __name__=='__main__':unittest.main()
