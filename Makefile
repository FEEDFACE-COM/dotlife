
BUILD_VERSION ?= $(shell git describe --tags)
BUILD_RELEASE = $(shell if echo ${BUILD_VERSION} | egrep -q '^[0-9]+\.[0-9]+\.[0-9]+$$'; then echo true; else echo false; fi )



PACKAGE_NAME=dotlife
PACKAGE_VERSION=$(shell echo ${BUILD_VERSION} | sed -e 's/-.*//')
PACKAGE_SOURCES=$(shell find ${PACKAGE_NAME} -type f -name \*.py | tr '\n' ' ')
PACKAGE_ASSETS=$(shell find scripts -type f | tr '\n' ' ')
PACKAGE_PRODUCT=${PACKAGE_NAME}-${PACKAGE_VERSION}-py3-none-any.whl


help:
	@echo "### Usage Help ###"
	@echo "make package  # build package"
	@echo "make release  # build release package"
	@echo "make shell    # run python shell"
	@echo "make info     # show product version info"



install: package
	pip3 install -e .

package: 
	unlink ${PACKAGE_NAME}/about.py
	${MAKE} dist/${PACKAGE_PRODUCT}

release:
	@if ${BUILD_RELEASE}; then true; else { echo "REFUSE TO RELEASE UNTAGGED VERSION ${BUILD_VERSION}"; false; }; fi;
	${MAKE} package

shell:
	@echo "### Shell ###"
	PYTHONSTARTUP=./shell.py python3 

info: 
	@echo "### Version Info ###"
	@echo "  version:  ${BUILD_VERSION}"
	@echo "  package:  dist/${PACKAGE_PRODUCT}"
	@${BUILD_RELEASE} && echo "  release:  dist/${PACKAGE_PRODUCT}"; true
	

version:
	unlink ${PACKAGE_NAME}/about.py
	${MAKE} ${PACKAGE_NAME}/about.py 

${PACKAGE_NAME}/about.py:
	@echo "### Tag Source ${PACKAGE_NAME} ${PACKAGE_VERSION} ###"
	echo "VERSION='${PACKAGE_VERSION}'" >| ${PACKAGE_NAME}/about.py
	echo "NAME='${PACKAGE_NAME}'" >> ${PACKAGE_NAME}/about.py



dist/${PACKAGE_PRODUCT}: ${PACKAGE_SOURCES} ${PACKAGE_ASSETS} ${PACKAGE_NAME}/about.py
	@echo "### build dist/${PACKAGE_PRODUCT} ###"
	python3 setup.py bdist_wheel
	@echo "### package at dist/${PACKAGE_PRODUCT} ###"






clean:
	@echo "### Clean Up ###"
	-find . -type f -name \*.pyc -delete
	-find . -type f -name __pycache__ -delete
	-rm -rf build/ dist/ .eggs/ ${PACKAGE_NAME}.egg-info/ ${PACKAGE_NAME}/__pycache__/

.PHONY: package release shell clean info help 


