# Add any tasks that are not dependent on files to the .PHONY list.
.PHONY: dev pip_dev lint test test_unit

dev:
	python dev.py

pip_dev:
	pip install --upgrade pip
	python -m venv env
	pip install -r requirements.txt -r requirements-dev.txt --use-deprecated=legacy-resolver

lint:
	flake8 employee/ tests/

test:
	py.test tests/ -vv

test_unit:
	py.test \
		-vv \
		--cov employee tests/unit/ \
		--cov-report xml
