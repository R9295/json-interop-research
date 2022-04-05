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
import json

import parserkiosk
from libs import libs

reports = {}
dump = {}


for lib in libs:
    with open(f'{lib}_tests/report.json', 'r') as file:
        reports[lib] = json.loads(file.read())


def parse_reports(report):
    return [
        {
            'name': f'{item.get("id")[2:item.get("id").index(".rb")]}::{item.get("description")}',  # noqa E501
            'result': item.get('status'),
        }
        for item in report.get('examples')
    ]


for k, v in reports.items():
    dump[k] = parse_reports(v)

with open('report.json', 'w') as file:
    file.write(json.dumps(dump, indent=4, sort_keys=True))

parserkiosk.colors.print_success('Done, see report.json')
