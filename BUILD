# The build makefile directive definitions

# 设置PROTOBUILD表示已经包含了这个定义
PROTOBUILD     := 1

# 设置Shell
SHELL          := /bin/bash
# 获得平台
Platform       := $(shell uname)
# 获得当前文件所在目录以及相关目录
RootDir        := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
ProtoDir       := $(RootDir)/proto
GoGenPath      := $(RootDir)/protoc-gen-go
PythonGenPath  := $(RootDir)/protoc-gen-python
SwaggerGenPath := $(RootDir)/protoc-gen-swagger

# Flag
ProtocFlags    := -I $(ProtoDir)

# Compiler check
CheckCompiler  := $(RootDir)/tools/compilercheck.py
CheckCompilerFlags := --version-file $(RootDir)/compilerversions

# Proto lint flags
ProtolintPlugin := protoc-gen-protolint=$(GOPATH)/bin/protoc-gen-protolint
ProtolintFlags  := Egoogle.,Eopenapiv2.

# Go flags
GoPackagePrefix := github.com/liferod/protobuf/protoc-gen-go

# for new version protoc-gen-go, need to add this param
GoCompileFlags  := paths=source_relative
GoCompileFlags  := $(GoCompileFlags),Mprotobuf/google/api/annotations.proto=google.golang.org/genproto/googleapis/api/annotations
GoCompileFlags  := $(GoCompileFlags),Mprotobuf/google/api/http.proto=google.golang.org/genproto/googleapis/api/annotations
GoCompileFlags  := $(GoCompileFlags),Mprotobuf/google/api/field_behavior.proto=google.golang.org/genproto/googleapis/api/annotations
GoCompileFlags  := $(GoCompileFlags),Mprotobuf/google/api/httpbody.proto=google.golang.org/genproto/googleapis/api/annotations
# GoCompileFlags  := $(GoCompileFlags),Mprotobuf/annotations.proto=$(GoPackagePrefix)/protobuf
# GoCompileFlags  := $(GoCompileFlags),Mprotobuf/options/auth.proto=$(GoPackagePrefix)/protobuf/options
# GoCompileFlags  := $(GoCompileFlags),Mopenapiv2/options/annotations.proto=$(GoPackagePrefix)/openapiv2/options
# GoCompileFlags  := $(GoCompileFlags),Mopenapiv2/options/openapiv2.proto=$(GoPackagePrefix)/openapiv2/options
# GoCompileFlags  := $(GoCompileFlags),Mgoogle/protobuf/descriptor.proto=google.golang.org/protobuf/types/descriptorpb

# Validate
GoValidCmd := go vet

# Extension
DescGoFlags := lang=go
DescPyFlags := lang=python,pyinit=import

export PROTOBUILD
export SHELL
export Platform
export RootDir
export ProtoDir
export GenPath
export GoGenPath
export PythonGenPath
export ProtocFlags
export ProtolintPlugin
export ProtolintFlags
export GoPackagePrefix
export GoCompileFlags
export GoValidCmd
export DescGoFlags
export DescPyFlags
