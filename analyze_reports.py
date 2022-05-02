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
import json  # lol

import matplotlib.pyplot as plt
import pandas
import seaborn as sns
from parserkiosk import colors


def read_report(lang):
    with open(f'{lang}/report.json', 'r') as report:
        return report.read()


def get_report_list(report_dict, lang):
    return [
        {'name': f'{lang}.{key}', 'results': value}
        for key, value in report_dict.items()
    ]


if __name__ == "__main__":
    print('')
    colors.print_success('Generating final report')
    results = {}
    python_report = json.loads(read_report('python'))
    node_report = json.loads(read_report('nodejs'))
    ruby_report = json.loads(read_report('ruby'))
    php_report = json.loads(read_report('php'))
    reports = get_report_list(python_report, 'python')
    reports.extend(get_report_list(node_report, 'nodejs'))
    reports.extend(get_report_list(ruby_report, 'ruby'))
    reports.extend(get_report_list(php_report, 'php'))
    for test in reports[0].get('results'):
        results[test.get('name')] = {}
    for report in reports:
        for test in report.get('results'):
            results[test.get('name')].update({report.get('name'): test.get('result')})
    matrix = []
    for key, value in results.items():
        for k, v in value.items():
            matrix.append(
                {
                    'implementation': k,
                    'test': key,
                    'passed': v == 'passed',
                }
            )
    with open('analysis.json', 'w') as file:
        file.write(json.dumps({'data': matrix}, indent=4))
    df = pandas.read_json('./analysis.json', orient='split')
    df['passed'] = df.apply(lambda row: 0 if row.get('passed') else 0.6, axis=1)
    data = df.pivot_table(values='passed', index='test', columns='implementation')
    plt.subplots(figsize=(30, 80))
    sns.heatmap(
        data, linewidths=1, linecolor='white', vmax=1, square=True, cbar=False
    ).figure.savefig('matrix.png', dpi=140)
    colors.print_success('Done. See matrix.png or analysis.json')
