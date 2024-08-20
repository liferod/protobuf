.PHONY: all protolint go python gw valid
.SILENT:

ifndef PROTOBUILD
include ../BUILD
endif

SubModules 		:= ./protobuf ./openapiv2 ./errors

all: protolint go gw valid

protolint:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) protolint &&) :

go:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) go &&) :

python:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) python &&) :
	touch $(PythonGenPath)/$(PackagePath)/__init__.py

gw:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) gw &&) :

valid:
	$(foreach SubModule,$(SubModules),$(MAKE) -C $(SubModule) valid &&) :
