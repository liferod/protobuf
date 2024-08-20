.PHONY: all protolint go python gw valid
.SILENT:

ifndef PROTOBUILD
include ../../BUILD
endif

PackagePath 	:= errors
PackageName 	:= errors
CurrentProtoDir	:= $(ProtoDir)/$(PackagePath)
Protofiles 		:= $(CurrentProtoDir)/code.proto $(CurrentProtoDir)/error_details.proto

all: protolint go gw valid

protolint:
	echo [-] Run protolint on: $(PackageName)
	protoc $(ProtocFlags) --plugin=$(ProtolintPlugin) --protolint_out=$(ProtolintFlags):. $(Protofiles)

go:
	echo [-] Build go module: $(PackageName)
	mkdir -p $(GoGenPath)
	protoc $(ProtocFlags) --go_out=$(GoCompileFlags):$(GoGenPath) $(Protofiles)
	cp -r golang/* $(GoGenPath)/$(PackagePath)/

python: $(Protofiles)
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
