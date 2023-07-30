.PHONY: help clean docs lint

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install: 		## install packages in virtualenv
	@pip install -U pip poetry
	@poetry install

lint: 			## run linters
	poetry run ./lint

version:		## display software version
	@python -c "import pyslink; print(pyslink.__version__)"

publish:		## release to pypi
	@poetry publish --build -u lsbardel -p $(PYPI_PASSWORD)
