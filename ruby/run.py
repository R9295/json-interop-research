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
import sys
import parserkiosk
from libs import libs

for lib in libs:
    os.chdir(f'{lib}_tests')
    # conditional there because I use the debian packaged ruby
    if len(sys.argv) == 2 and sys.argv[1] == '--with-alias':
        os.system('bundle2.7 exec rspec spec . --format json > report.json')
    else:
        os.system('bundle exec rspec spec . --format json > report.json')
    os.chdir('..')
print(parserkiosk.colors.print_success('Done running test suite, run analyze.py next'))
