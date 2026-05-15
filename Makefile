.PHONY: setup test test-quiet

PYTHON ?= python

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest

test-quiet:
	$(PYTHON) -m pytest -q
