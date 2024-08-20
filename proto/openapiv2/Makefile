.PHONY: all protolint go python valid
.SILENT:

ifndef PROTOBUILD
include ../../BUILD
endif

PackagePath 	:= openapiv2
PackageName 	:= openapiv2
SubModules 		:= ./options

all: protolint go python valid

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
