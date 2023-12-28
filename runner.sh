#!/bin/bash

script_dir="$(dirname "$(readlink -f "$0")")"

cd "${script_dir}"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

