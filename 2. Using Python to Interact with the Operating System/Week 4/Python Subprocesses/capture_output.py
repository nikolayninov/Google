#!/usr/bin/python3

import subprocess

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result)
print(result.returncode)
print(result.stdout.decode().split())
print("-"*70)
new_result = subprocess.run(['rm', 'does_not_exist'], capture_output=True)
print(new_result.stdout)
print(new_result.stderr)
