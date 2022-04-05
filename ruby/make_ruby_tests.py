import glob
import os

tests = glob.glob('*_tests/test_*.rb')

for file in tests:
    os.system(f'mv {file} {file.split(".rb")[0]}_spec.rb')
