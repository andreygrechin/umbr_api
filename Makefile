.PHONY: all
all: clear-all install-dev test-offline docs built upload coverage-offline

.PHONY: tests
tests: clear-all install-dev
	pytest -k '' -q --cache-clear tests/

.PHONY: tests-online
tests-online: clear-all install-dev
	pytest -k 'Online' -q --cache-clear tests/

.PHONY: tests-offline
tests-offline: clear-all install-dev
	pytest -k 'not Online' -q --cache-clear tests/

.PHONY: lint
lint:
	pip install -q -e .[lint_dev] --no-use-pep517
	pycodestyle -r --statistics --count --show-source umbr_api/ tests/ examples/ setup.py
	pydocstyle -e --count --match='.+\.py' --match-dir='umbr_api|tests|examples'
	pep257 -s -e umbr_api/
	pep257 -s -e tests/
	pep257 -s -e examples/
	pep257 -s -e setup.py
	pylint --disable=R0401 umbr_api/ tests/* examples/ setup.py

.PHONY: lint_opt
lint_opt:
	pip install -q -e .[lint_opt] --no-use-pep517
	bandit -r umbr_api/ tests/ examples/ ./setup.py --skip B101
	isort --check-only -df -rc -tc umbr_api/ tests/ examples/ setup.py
	safety check
	pyroma -a ./
	check-manifest -v

.PHONY: install-dev
install-dev:
	pip install -q -e .[dev] --no-use-pep517
	pip install -q -e .[doc] --no-use-pep517

.PHONY: install-doc
install-doc:
	pip install -q -e .[doc] --no-use-pep517

.PHONY: coverage-offline
coverage-offline: clear-pyc clear-cov
	coverage run -m pytest -k 'not Online' -q --cache-clear tests/
	coverage report
	coverage annotate

.PHONY: coverage
coverage: clear-pyc clear-cov
	coverage run -m pytest
	coverage report
	coverage annotate

.PHONY: cov
cov: coverage

.PHONY: upload
upload: clear-all built
	twine upload dist/*

.PHONY: docs
docs: clear-doc install-dev install-doc
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

.PHONY: built
built:
	python3 setup.py sdist

.PHONY: clear-all
clear-all: clear-pyc clear-cov clear-build clear-doc

.PHONY: clear-venv
clear-venv:
	rm -fr ./.venv/
	virtualenv .venv

.PHONY: clear-doc
clear-doc:
	$(MAKE) -C docs clean

.PHONY: clear-pyc
clear-pyc:
	find . -type d -name '__pycache__' -not -path './venv/*' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -not -path './venv/*' -exec rm -f {} +
	find . -type f -name '*~' -not -path './venv/*' -exec rm -f {} +

.PHONY: clear-cov
clear-cov:
	find . -type f -name '*.py,cover' -exec rm -f {} +
	rm -fr .pytest_cache
	coverage erase

.PHONY: clear-build
clear-build:
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info/

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python3 -c "$$BROWSER_PYSCRIPT"
