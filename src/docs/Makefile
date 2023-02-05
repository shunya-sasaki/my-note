# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

htmlbuild: html html_ja
	# @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	if [ -e ../../docs ]; then rm -rf ../../docs; fi
	cp -r ./_build/html ../../docs
	touch ../../docs/.nojekyll

html_%: Makefile
	$(eval SPHINXOPTS := $(SPHINXOPTS) -D language='ja')
	echo $(SPHINXOPTS)
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/html_$*" $(SPHINXOPTS) $(O)
	if [ -e $(BUILDDIR)/html/$* ]; then rm -rf $(BUILDDIR)/html/$*; fi
	mv "$(BUILDDIR)/html_$*/html" "$(BUILDDIR)/html/$*"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
