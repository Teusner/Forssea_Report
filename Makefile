ENSTA_BUILD_DIR = "build/ensta"
ANGERS_BUILD_DIR = "build/angers"
TEX_SRCS := $(shell find corps -name '*.tex')

GANTT_DIR = "gantt"
GANTT_BUILD_DIR = "build/gantt"

define pdflatex
	pdflatex --output-directory $(1) $(2)
endef

define glossary
	makeglossaries -d $(1) $(2)
endef

define bibliography
	bibtex $(shell find $(1) -name '$(2).aux')
endef

all: report_ensta.pdf report_angers.pdf

gantt_before.pdf: $(shell find $(GANTT_DIR) -name gantt_before.tex)
	$(call pdflatex,$(GANTT_BUILD_DIR),$<)

gantt_after.pdf: $(shell find $(GANTT_DIR) -name gantt_after.tex)
	$(call pdflatex,$(GANTT_BUILD_DIR),$<)

report_ensta.pdf: report_ensta.tex ${TEX_SRCS} gantt_before.pdf gantt_after.pdf
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)
	$(call glossary,$(ENSTA_BUILD_DIR),report_ensta)
	$(call bibliography,$(ENSTA_BUILD_DIR),report_ensta)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)

report_angers.pdf: report_angers.tex ${TEX_SRCS} gantt_before.pdf gantt_after.pdf
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)
	$(call glossary,$(ANGERS_BUILD_DIR),report_angers)
	$(call bibliography,$(ANGERS_BUILD_DIR),report_angers)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)