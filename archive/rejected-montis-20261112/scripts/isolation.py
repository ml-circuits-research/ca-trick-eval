"""Allowlist filesystem for the whole Codex process, including its shell tools.

Only system programs, the installed Node/Codex toolchain, this case's documents,
a private runtime and an initially empty answer directory are mounted. No host
project, reference, manifest, previous result, user home or host /tmp is mounted.
The runtime contains login credentials required by Codex, not reference material.
"""
from pathlib import Path
import shutil
import subprocess

def prefix(work, runtime, delivery):
    if not shutil.which('bwrap'):
        raise RuntimeError('Strict isolation requires bubblewrap (bwrap); no implicit fallback.')
    node=Path(shutil.which('node')).resolve().parent.parent
    command=['bwrap','--die-with-parent','--unshare-pid','--unshare-ipc','--unshare-uts','--new-session']
    for name in ['usr','bin','sbin','lib','lib64','etc']:
        source=Path('/')/name
        if source.exists(): command+=['--ro-bind',str(source),str(source)]
    # /etc/resolv.conf may point into /run, which is intentionally not mounted.
    resolver=Path('/etc/resolv.conf').resolve()
    if not str(resolver).startswith('/etc/'):
        command+=['--ro-bind',str(resolver),str(resolver)]
    command+=['--ro-bind',str(node),str(node),
        '--proc','/proc','--dev','/dev','--tmpfs','/tmp','--dir','/home/reviewer',
        '--ro-bind',str(work),'/case','--bind',str(runtime),'/runtime',
        '--bind',str(delivery),'/output',
        '--setenv','HOME','/home/reviewer','--setenv','CODEX_HOME','/runtime',
        '--setenv','TMPDIR','/tmp','--setenv','PWD','/case',
        '--setenv','PATH',str(node/'bin')+':/usr/local/bin:/usr/bin:/bin',
        '--chdir','/case','--']
    return command

def probe(command, project, files):
    source='''import json
from pathlib import Path
project=Path(PROJECT)
assert not project.exists(), "host project is visible"
assert not Path('/home/salboaie/.codex').exists(), "host user config is visible"
assert sorted(p.name for p in Path('/case').iterdir()) == FILES
assert not list(Path('/output').iterdir()), "answer directory must start empty"
assert not list(Path('/tmp').iterdir()), "host temporary files must be hidden"
print(json.dumps(dict(project_visible=False,user_config_visible=False,case_files=FILES,output_initially_empty=True,host_tmp_hidden=True)))
'''.replace('PROJECT',repr(str(project))).replace('FILES',repr(sorted(files)))
    result=subprocess.run(command+['python3','-c',source],capture_output=True,text=True,check=True)
    import json
    return json.loads(result.stdout)
