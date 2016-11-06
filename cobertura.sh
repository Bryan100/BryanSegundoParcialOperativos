#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/pruebasComandosArchivos/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml
PYTHONPATH=. py.test --cov-report xml --cov=../pruebasComandosArchivos
PYTHONPATH=. py.test --cov-report html --cov=../pruebasComandosArchivos