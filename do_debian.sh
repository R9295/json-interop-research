#!/bin/bash

# Since I use the debian built package for ruby, bundle == bundle2.7

# run
cd python
python generate.py
python run.py
python analyze.py
cd ..

# nodejs
cd nodejs
npm install
python generate.py
python run.py
python analyze.py
cd ..

# ruby
cd ruby
bundle2.7 install
python generate.py
python run.py --with-alias
python analyze.py
cd ..

cd php
python generate.py
python run.py
python analyze.py

# analyze all
cd ..
python analyze_reports.py

