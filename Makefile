install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 project

uninstall:
	python3 -m pip uninstall hexlet_code-0.1.0-py3-none-any.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=project --cov-report xml