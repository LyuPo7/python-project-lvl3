install:
	poetry install

test:
	poetry run pytest -vv --ff --cov=page-loader --cov-report xml tests/tests.py 

lint:
	poetry run flake8 page-loader --show-source --ignore=E131,E501 --verbose

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

publish:
	poetry publish --repository PyPiTest

.PHONY: install test lint selfcheck check build
