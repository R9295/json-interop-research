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

os.system('rm -rf *_tests')
if os.path.exists('report.json'):
    os.system('rm report.json')
os.system('rm -rf __pycache__')
os.system('rm -rf fixtures')
os.system('rm test_serialize_succ.yaml')
os.system('rm test_serialize_fail.yaml')
os.system('rm report.json')