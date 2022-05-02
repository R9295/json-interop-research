import os

import parserkiosk
from libs import libs

os.system('cp ../base/test_serialize_further.yaml .')
for lib in libs:
    print(f'{lib.upper()}')
    with open(f'{lib}.config.yaml', 'r') as file:
        with open('config.yaml', 'w') as config:
            config.write(file.read())
        if lib == 'jsonmachine':
            os.system('parserkiosk . --path jsonmachine.template.jinja2 --ext Test.php --override')
        else:
            os.system('parserkiosk . --path php.template.jinja2 --ext Test.php --override')
    os.system(f'cp -r tests {lib}_tests')
    os.system(f'cp -r ../base/* {lib}_tests/')
    os.system('rm config.yaml')
    os.system('rm -rf tests')

print('')
parserkiosk.colors.print_success('Done generating suite. Use run.py to run test-suite')
