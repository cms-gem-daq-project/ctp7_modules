# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS ?=
SPHINXBUILD?= sphinx-build
SOURCEDIR   = source
BUILDDIR    = build

.PHONY: doxygen doxyrest
.PHONY: cleandoxygen cleandoxyrest

doxygen:
	cp ctp7_modules.doxygen ctp7_modules.cfg
	# perl -pi -e "s|__GEM_OS_PROJECT__|$(GEM_OS_PROJECT)|g" ctp7_modules.cfg
	# perl -pi -e "s|__GIT_VERSION__|$(GIT_VERSION)|g" ctp7_modules.cfg
	doxygen ctp7_modules.cfg

doxyrest: doxygen
	cp doxyrest-config.lua.in doxyrest-config.lua
	perl -pi -e "s|__DOXYREST_PREFIX__|$(DOXYREST_PREFIX)|g" doxyrest-config.lua
	doxyrest -c doxyrest-config.lua

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: clean cleanall help Makefile

clean:
	rm -rf build
	rm -rf source/exhale-api

cleandoxygen:
	rm -rf doxybuild

cleandoxyrest:
	rm -rf source/doxyrest-api

cleanall: cleandoxygen cleandoxyrest

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
