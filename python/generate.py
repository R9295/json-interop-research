import os
libs = ['json', 'simplejson', 'rapidjson', 'pysimdjson', 'ujson', 'orjson']


curdir = os.path.curdir


for lib in libs:
    print(f'{lib.upper()}')
    with open(f'{lib}.config.yaml', 'r') as file:
        with open('config.yaml', 'w') as config:
            config.write(file.read())
    if lib != 'pysimdjson':
        os.system('parserkiosk . --builtin python')
    else:
        os.system('parserkiosk . --path pysimdjson.template.jinja2 --ext py')
    os.system(f'cp -r tests {lib}_tests')
    os.system(f'cp -r base/* {lib}_tests/')
    os.system('rm config.yaml')
    print('')
