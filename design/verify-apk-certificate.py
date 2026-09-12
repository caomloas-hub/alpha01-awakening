"""Compare public signing certificates, without hashing files or printing keys."""
import re
import subprocess
import sys
from pathlib import Path

keytool, old_apk, new_apk = sys.argv[1:]
def cert(path):
    result = subprocess.run([keytool, '-printcert', '-rfc', '-jarfile', path], capture_output=True, check=True)
    pem = re.findall(rb'-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----', result.stdout, re.S)
    if not pem:
        raise RuntimeError('No public signing certificate found: ' + str(Path(path).name))
    return [re.sub(rb'\s+', b'', item) for item in pem]
assert cert(old_apk) == cert(new_apk), 'Signing certificate changed; do not publish as an in-place update.'
print('PASS: new APK and previous local v0.2.2 APK use the same public signing certificate.')
