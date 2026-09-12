"""Run isolated menu tests and close only the test process after its report."""
import pathlib
import re
import subprocess
import sys
import time

root = pathlib.Path(__file__).resolve().parents[1]
sdk = root.parents[1] / 'work/renpy-sdk/renpy-8.5.3-sdk/renpy.exe'
names = sys.argv[1:] or ['sky_menu_intro', 'sky_menu_skip', 'sky_menu_save_restore', 'sky_menu_navigation', 'sky_menu_keyboard', 'sky_menu_social']
for name in names:
    stamp = str(time.time_ns())
    saves = root.parents[1] / 'work' / ('sky-qa-' + name + '-' + stamp)
    log = root / 'log.txt'
    old_mtime = log.stat().st_mtime_ns if log.exists() else 0
    proc = subprocess.Popen([str(sdk),str(root),'--savedir',str(saves),'test',name,'--overwrite-screenshots'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    result = ''
    try:
        deadline = time.monotonic()+65
        while time.monotonic()<deadline:
            if log.exists() and log.stat().st_mtime_ns != old_mtime:
                result = log.read_text(encoding='utf-8-sig',errors='replace')
                if '[rpytest] Status:' in result:
                    break
            if proc.poll() is not None:
                break
            time.sleep(.25)
    finally:
        if proc.poll() is None:
            proc.terminate()
        proc.wait(timeout=10)
    (root/'tests'/ (name+'.log')).write_text(result,encoding='utf-8')
    passed = '[rpytest] Status: PASSED' in result and bool(re.search(r'Test cases\s*:\s*\d+\s*\|\s*1 passed\s*\|\s*0 xfailed\s*\|\s*0 failed',result))
    print(name, 'PASS' if passed else 'FAIL', flush=True)
    if not passed:
        print(result[-4000:])
        sys.exit(1)
