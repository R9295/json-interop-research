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

from parserkiosk import colors


def read_report(lang):
    with open(f'{lang}/report.json', 'r') as report:
        return report.read()


def get_report_list(report_dict, lang):
    return [
        {'name': f'{lang}.{key}', 'results': value}
        for key, value in report_dict.items()
    ]


def diff_reports(report1, report2):
    diff = []
    for i in report1.get('results'):
        if i not in report2.get('results'):
            diff.append(
                {
                    'name': i.get('name'),
                    '__who_passed': report1.get('name')
                    if i.get('result') == 'passed'
                    else report2.get('name'),
                }
            )
    return diff


def format_report_names(report1, report2):
    return f'{report1["name"]} vs {report2["name"]}'


if __name__ == "__main__":
    results = {}
    python_report = json.loads(read_report('python'))
    node_report = json.loads(read_report('nodejs'))
    ruby_report = json.loads(read_report('ruby'))
    reports = get_report_list(python_report, 'python')
    reports.extend(get_report_list(node_report, 'nodejs'))
    reports.extend(get_report_list(ruby_report, 'ruby'))
    for index, report in enumerate(reports):
        for index2, report2 in enumerate(reports):
            if index2 != index and not results.get(
                format_report_names(report2, report)
            ):
                diff = diff_reports(report, report2)
                results[format_report_names(report, report2)] = diff
    with open('analysis.json', 'w') as file:
        file.write(json.dumps(results, indent=4))
    colors.print_success('Done. See: analysis.json')
