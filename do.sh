#!/bin/bash

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

# analyze 
cd ..
python analyze_reports.py
npx serve -s .

