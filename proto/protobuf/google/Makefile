.PHONY: all protolint go python
.SILENT:

ifndef PROTOBUILD
include ../../../BUILD
endif

PackagePath 	:= protobuf/google
PackageName 	:= protobuf.google
SubModules 		:= ./api

all: protolint go python

protolint:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) protolint &&) :

go:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) go &&) :

python:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) python &&) :
	touch $(PythonGenPath)/$(PackagePath)/__init__.py

gw:

valid:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) valid &&) :
