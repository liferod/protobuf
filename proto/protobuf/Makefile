.PHONY: all protolint go python gw valid
.SILENT:

ifndef PROTOBUILD
include ../../BUILD
endif

PackagePath 	:= protobuf
PackageName 	:= protobuf
CurrentProtoDir	:= $(ProtoDir)/$(PackagePath)
Protofiles 		:= $(CurrentProtoDir)/annotations.proto
GoCompileFlags 	:= $(GoCompileFlags),Mprotobuf/options/auth.proto=$(GoPackagePrefix)/protobuf/options,Mprotobuf/options/api.proto=$(GoPackagePrefix)/protobuf/options

all: protolint go python gw valid

protolint:
	echo [-] Run protolint on: $(PackageName)
	protoc $(ProtocFlags) --plugin=$(ProtolintPlugin) --protolint_out=$(ProtolintFlags):. $(Protofiles)
	$(MAKE) -C ./options protolint

go:
	$(MAKE) -C ./options go
	$(MAKE) -C ./google go
	echo [-] Build go module: $(PackageName)
	mkdir -p $(GoGenPath)
	protoc $(ProtocFlags) --go_out=$(GoCompileFlags):$(GoGenPath) $(Protofiles)
	cp -r golang/* $(GoGenPath)/$(PackagePath)/

python: $(Protofiles)
	$(MAKE) -C ./options python
	$(MAKE) -C ./google python
	echo [-] Build python module: $(PackageName)
	mkdir -p $(PythonGenPath)
	python -m grpc.tools.protoc $(ProtocFlags) \
		--python_out=$(PythonGenPath) \
		--grpc_python_out=$(PythonGenPath) \
		--desc_out=$(DescPyFlags),pyinit=no:$(PythonGenPath) \
		$(Protofiles)
	cp -r python/* $(PythonGenPath)/$(PackagePath)/ 2>/dev/null || :
	touch $(PythonGenPath)/$(PackagePath)/__init__.py

gw:

valid:
	echo [-] Valid generated module: $(PackageName)
	cd $(GoGenPath)/$(PackagePath) && $(GoValidCmd) .
	$(MAKE) -C ./options valid
