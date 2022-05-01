import json
import xmltodict
from libs import libs
from parserkiosk import colors


data = {}

for lib in libs:
    with open(f'{lib}_tests/results.xml', 'r') as file:  # ugh
        parsed = xmltodict.parse(file.read())
        suite = [suite for suite in parsed.get('testsuites').values()][0]
        filtered = []
        for test_file in suite.get('testsuite'):
            for test in test_file.get('testcase'):
                filtered.append({
                        'name': f'{test.get("@class")}::{test.get("@name")}',
                        'result': 'failed' if test.get('failure') else 'passed'
                    })
        data[lib] = filtered

with open('report.json', 'w') as file:
    file.write(json.dumps(data))

colors.print_success('Done, see report.json')
