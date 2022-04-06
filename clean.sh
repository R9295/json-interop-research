#!/bin/bash

rm analysis.json

cd python
python clean.py
cd ..

cd nodejs
python clean.py
cd ..

cd ruby
python clean.py
cd ..
