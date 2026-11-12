#!/usr/bin/env python3
"""Verify the contractual answer and the actual ripgrep filtering behavior."""
from datetime import datetime
from pathlib import Path
import re
import subprocess
ROOT=Path(__file__).resolve().parents[1]

def main():
    folder=ROOT/'eval/04_dacia_anexa'
    contract=(folder/'01_contract.md').read_text()
    act=(folder/'anexe/03_act_aditional.md').read_text()
    initial=int(re.search(r'pentru ([\d.]+) EUR',contract)[1].replace('.',''))
    cancellation=int(re.search(r'cu suma de ([\d.]+) EUR',act)[1].replace('.',''))
    datefmt='%d.%m.%Y %H:%M'
    review=datetime.strptime(' '.join(re.search(r'la (\d{2}\.\d{2}\.\d{4}), ora (\d{2}:\d{2})',contract).groups()),datefmt)
    effect=datetime.strptime(' '.join(re.search(r'cu efect la (\d{2}\.\d{2}\.\d{4}), ora (\d{2}:\d{2})',act).groups()),datefmt)
    assert effect<=review and initial-cancellation==60000
    filtered=(folder/'.ignore').read_text()=='anexe/\n'
    def listing(extra):
        return set(subprocess.check_output(['rg','--files',*extra,'-g','*.md'],cwd=folder,text=True).splitlines())
    normal=listing([]);complete=listing(['--hidden','--no-ignore'])
    expected={'01_contract.md','02_nota_comitet.md','anexe/03_act_aditional.md'}
    assert complete==expected
    assert normal==(expected-{'anexe/03_act_aditional.md'} if filtered else expected),(filtered,normal)
    assert (folder/'anexe/03_act_aditional.md').is_file()
    print(f'OK: {initial}−{cancellation}=60000 EUR; amendment effective before review; filtered={filtered}; default listing={len(normal)} Markdown files, complete listing=3.')
if __name__=='__main__':main()
