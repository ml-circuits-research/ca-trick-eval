#!/usr/bin/env python3
"""Independently verify numeric findings for active candidates only."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    for c in json.loads((ROOT/'manifest.json').read_text()):
        if c['id']=='04_dacia_anexa':
            from check_discovery_oracle import main as check
        elif c['id']=='03_montis_garantii':
            from check_collateral_oracle import main as check
        else: raise ValueError('Register an independent oracle for '+c['id'])
        check()
if __name__=='__main__':main()
