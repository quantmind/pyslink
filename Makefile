.PHONY: help clean docs

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


install: 		## install packages in virtualenv
	@pip install -r requirements-dev.txt


lint: 			## run linters
	isort *.py
	black *.py
	flake8

version:		## display software version
	@python -c "import pyslink; print(pyslink.__version__)"

test-version:		## validate version with pypi
	@agilekit git validate

release-pypi:		## release to pypi and github tag
	python setup.py sdist
	twine upload dist/* --username lsbardel --password $(PYPI_PASSWORD)
