#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/BryanSegundoParcialOperativos/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml
PYTHONPATH=. py.test --cov-report xml --cov=../BryanSegundoParcialOperativos
PYTHONPATH=. py.test --cov-report html --cov=../BryanSegundoParcialOperativos
