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
bundle install
python generate.py
python run.py
python analyze.py

cd php
python generate.py
python run.py
python analyze.py

# analyze 
cd ..
python analyze_reports.py

