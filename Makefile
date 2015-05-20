.PHONY: docs help init docs test
.DEFAULT_GOAL := help

##
## Please use `make ^<target^>` where ^<target^> is one of
##

help:              ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

init:              ## install requirements
	@pip install -r requirements.txt

docs:              ## build docs
	@cp README.md docs/index.md
	@mkdocs build
	@mkdocs serve

test:              ## to run all tests
	@py.test

test_basic:        ## to run basic tests
	@py.test tests/test_basic.py

test_advanced:     ## to run advanced tests
	@py.test tests/test_advanced.py

requirements:      ## show requirements
	@pip freeze > requirements.txt
	@cat requirements.txt

##
