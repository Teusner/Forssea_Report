ENSTA_BUILD_DIR = "build/ensta"
ANGERS_BUILD_DIR = "build/angers"
TEX_SRCS := $(shell find corps -name '*.tex')

GANTT_DIR = "gantt"
GANTT_FILE := $(shell find $(GANTT_DIR) -name gantt.tex)

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

gantt.pdf: $(GANTT_FILE)
	$(call pdflatex,$(GANTT_DIR),$<)

report_ensta.pdf: report_ensta.tex ${TEX_SRCS} $(GANTT_FILE)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)
	$(call glossary,$(ENSTA_BUILD_DIR),report_ensta)
	$(call bibliography,$(ENSTA_BUILD_DIR),report_ensta)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)

report_angers.pdf: report_angers.tex ${TEX_SRCS} $(GANTT_FILE)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)
	$(call glossary,$(ANGERS_BUILD_DIR),report_angers)
	$(call bibliography,$(ANGERS_BUILD_DIR),report_angers)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)