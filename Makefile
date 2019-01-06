.PHONY: all
all: clear-all install-dev test-offline docs built upload coverage-offline

.PHONY: test
test: clear-all install-dev
	pytest -k '' -q --cache-clear tests/

.PHONY: test-online
test-online: clear-all install-dev
	pytest -k 'Online' -q --cache-clear tests/

.PHONY: test-offline
test-offline: clear-all install-dev
	pytest -k 'not Online' -q --cache-clear tests/

.PHONY: lint
lint:
	pip install -q -e .[lint_dev]
	pycodestyle -r --statistics --count --show-source umbr_api/ tests/ examples/ setup.py
	pydocstyle -e --count --match='.+\.py' --match-dir='tests|umbr_api|examples'
	pep257 -s -e umbr_api/
	pep257 -s -e tests/
	pep257 -s -e examples/
	pep257 -s -e setup.py
	pylint --disable=R0401 umbr_api/ tests/*.py examples/ setup.py
	# flake8 --statistics --count --exclude venv

.PHONY: lint_opt
lint_opt:
	pip install -q -e .[lint_opt]
	bandit -r umbr_api/ tests/ examples/ ./setup.py --skip B101
	isort --check-only -df -rc umbr_api/ tests/ examples/ setup.py
	# isort -ac -rc umbr_api/ tests/ examples/ setup.py
	flake8 --statistics --count umbr_api/ tests/ examples/ setup.py
	safety check
	check-manifest -v
	pyroma -a ./

.PHONY: install-dev
install-dev:
	pip install -q -e .[dev]

.PHONY: install-doc
install-doc:
	pip install -q -e .[doc]

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
