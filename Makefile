.SILENT:
.PHONY: all protolint go python gw valid clean clean-go clean-python

include BUILD

all: protolint go python gw valid

protolint:
	echo [+] Run protolint
	$(MAKE) -C $(RootDir)/proto protolint

go: clean-go protolint
	mkdir -p $(GoGenPath)
	echo [+] Build go modules
	$(MAKE) -C $(RootDir)/proto go

python: clean-python protolint
	mkdir -p $(GoGenPath)
	echo [+] Build python modules
	$(MAKE) -C $(RootDir)/proto python

gw: go
	echo [+] Build gateway modules
	$(MAKE) -C $(RootDir)/proto gw

valid: go
	echo [+] Build gateway modules
	$(MAKE) -C $(RootDir)/proto valid

clean: clean-go clean-python

clean-go:
	rm -rf $(GoGenPath)

clean-python:
	rm -rf $(PythonGenPath)
