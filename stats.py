import json
from parserkiosk import colors


with open('analysis.json', 'r') as f:
    analysis = json.loads(f.read())

analysis = analysis['data']


def get_amount_failed(analysis):
    count = 0
    for i in analysis:
        if not i.get('passed'):
            count += 1
    return count


def get_failed_per_impl(analysis):
    data = {}
    for i in analysis:
        if not i.get('passed'):
            if not data.get(i.get('implementation')):
                data[i.get('implementation')] = 1
            else:
                data[i.get('implementation')] += 1
    return data


def get_failed_per_lang(analysis):
    data = {}
    for i in analysis:
        if not i.get('passed'):
            lang = i.get('implementation').split('.')[0]
            if not data.get(lang):
                data[lang] = 1
            else:
                data[lang] += 1
    return data


colors.print_success('Total failed')
print(get_amount_failed(analysis))
print()

colors.print_success('Total failed per implementation')
for k, v in get_failed_per_impl(analysis).items():
    print(f'{k} :: {v}')
print()

colors.print_success('Total failed per language')
for k, v in get_failed_per_lang(analysis).items():
    print(f'{k} :: {v}')
