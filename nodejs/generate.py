'''
Copyright (C) 2022 Aarnav Bos

This program is free software: you can redistribute it and/or modify

it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import os

import parserkiosk
from libs import libs

curdir = os.path.curdir

os.system('cp -r ../base/fixtures fixtures')
os.system('cp ../base/test_serialize_further.yaml .')
for lib in libs:
    print(f'{lib.upper()}')
    with open(f'{lib}.config.yaml', 'r') as file:
        with open('config.yaml', 'w') as config:
            config.write(file.read())
    os.system('parserkiosk . --override --path ./node_js.jinja2 --ext test.js')
    os.system(f'cp -r tests {lib}_tests')
    os.system(f'cp -r ../base/commons.js {lib}_tests/')
    os.system('rm config.yaml')
    os.system('rm -rf tests')

print('')
parserkiosk.colors.print_success('Done generating suite. Use run.py to run test-suite')
