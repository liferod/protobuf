.PHONY: all protolint go python valid
.SILENT:

ifndef PROTOBUILD
include ../../../BUILD
endif

PackagePath 	:= openapiv2/options
PackageName 	:= openapiv2.options
CurrentProtoDir	:= $(ProtoDir)/$(PackagePath)
Protofiles 		:= $(CurrentProtoDir)/annotations.proto $(CurrentProtoDir)/openapiv2.proto

all: protolint go python valid

protolint:
	echo [-] Run protolint on: $(PackageName)
	protoc $(ProtocFlags) --plugin=$(ProtolintPlugin) --protolint_out=$(ProtolintFlags):. $(Protofiles)

go:
	echo [-] Build go module: $(PackageName)
	mkdir -p $(GoGenPath)
	protoc $(ProtocFlags) --go_out=$(GoCompileFlags):$(GoGenPath) $(Protofiles)

python: $(Protofiles)
	echo [-] Build python module: $(PackageName)
	mkdir -p $(PythonGenPath)
	python -m grpc.tools.protoc $(ProtocFlags) \
		--python_out=$(PythonGenPath) \
		--grpc_python_out=$(PythonGenPath) \
		--desc_out=$(DescPyFlags),pyinit=no:$(PythonGenPath) \
		$(Protofiles)
	cp -r python/* $(PythonGenPath)/$(PackagePath)/ 2>/dev/null || :

valid:
	echo [-] Valid generated module: $(PackageName)
	cd $(GoGenPath)/$(PackagePath) && $(GoValidCmd) .
