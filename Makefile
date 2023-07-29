.PHONY: help clean docs lint

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install: 		## install packages in virtualenv
	@pip install -r requirements-dev.txt

lint: 			## run linters
	poetry run ./lint

version:		## display software version
	@python -c "import pyslink; print(pyslink.__version__)"

release-pypi:		## release to pypi and github tag
	python setup.py sdist
	twine upload dist/* --username lsbardel --password $(PYPI_PASSWORD)
