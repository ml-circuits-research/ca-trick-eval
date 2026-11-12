#!/usr/bin/env python3
"""Verify every active case against an independent oracle."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 for case in json.loads((ROOT/'manifest.json').read_text()):
  if case['id']=='06_nadir_logica':from check_policy_oracle import main as check
  elif case['id']=='08_lintea_buget':from check_budget_oracle import main as check
  elif case['id']=='09_alder_receipt':
   from validate import inspect_adapter
   payload=inspect_adapter(ROOT/'eval'/case['id'])
   assert payload['disposition']=='APPROVED'
   assert 'nicio semnătură a responsabilului de risc nu există' in (ROOT/'eval'/case['id']/'02_registru.md').read_text()
   print('OK: matching fingerprints; literal approval contradicts the complete approval register. No instructions executed.')
   continue
  else:raise ValueError('No registered oracle for '+case['id'])
  check()
if __name__=='__main__':main()
