.PHONY: all
all: clear-all install-dev test-offline docs built upload coverage-offline

.PHONY: test
test: clear-all install-dev
	pytest -q --cache-clear tests/

.PHONY: test-online
test-online: clear-all install-dev
	pytest -k 'Online' -q --cache-clear tests/

.PHONY: test-offline
test-offline: clear-all install-dev
	pytest -k 'not Online' -q --cache-clear tests/

.PHONY: lint
lint:
	pycodestyle -r --statistics --count --show-source umbr_api/ tests/ examples/ setup.py
	pep257 -s -e umbr_api/
	pep257 -s -e tests/
	pep257 -s -e examples/
	pep257 -s -e setup.py
	# flake8 --statistics --count --exclude venv

.PHONY: install-dev
install-dev:
	pip install -q -e .[dev]

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
docs: clear-pyc install-dev
	$(MAKE) -C docs html

.PHONY: built
built:
	python3 setup.py sdist

.PHONY: clear-all
clear-all: clear-pyc clear-cov clear-build

.PHONY: clear-pyc
clear-pyc:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -exec rm -f {} +
	find . -type f -name '*~' -exec rm -f {} +

.PHONY: clear-cov
clear-cov:
	find . -type f -name '*.py,cover' -exec rm -f {} +
	rm -fr .pytest_cache
	coverage erase

.PHONY: clear-build
clear-build:
	rm -fr docs/_build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info/
