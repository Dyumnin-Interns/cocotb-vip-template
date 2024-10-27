# feature/doc branch
Create a branch called feature/doc and perform the following steps.
*  Rename the cocotb_vip_templates folder.
```bash
git mv src/cocotb_vip_templates/ src/cocotbext-<protocol-name>
find . -exec perl -p -ie 's/cocotb_vip_template /cocotbext_<protocolname>/
find . -exec perl -p -ie 's/cocotb-vip-template /cocotbext-<protocolname>/
```

*  Modify the project details in the pyproject.toml file.
*  Update the README.md file.
* Fillout the docstrings stubs in the src/cocotbext.../ folder.

# feature/<featurename> branch

* Write code for driver, monitor,bus etc.
* Create testcases in tests folder.
* Replace stub in verilog folder with a real sample if possible.
