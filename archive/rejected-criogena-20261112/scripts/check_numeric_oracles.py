#!/usr/bin/env python3
"""Verify every active case against an independent oracle."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 for case in json.loads((ROOT/'manifest.json').read_text()):
  if case['id']=='06_nadir_logica':from check_policy_oracle import main as check
  elif case['id']=='07_criogena_plan':from check_plan_oracle import main as check
  else:raise ValueError('No registered oracle for '+case['id'])
  check()
if __name__=='__main__':main()
