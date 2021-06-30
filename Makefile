ENSTA_BUILD_DIR = "build/ensta"
ANGERS_BUILD_DIR = "build/angers"
TEX_SRCS := $(shell find corps -name '*.tex')

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

PYTHON_PGF_SCRIPTS = scripts
PGF_BUILD_DIR = build/pgf
IMAGES_PGF = $(PGF_BUILD_DIR)/gerstner_wave.pgf $(PGF_BUILD_DIR)/gerstner_pixar.pgf 

$(IMAGES_PGF): $(PGF_BUILD_DIR)/%.pgf : $(PYTHON_PGF_SCRIPTS)/%.py
	python3 $< $@
	
GANTT_DIR = gantt
GANTT_BUILD_DIR = build/gantt
GANTT_PDF = $(GANTT_BUILD_DIR)/gantt_before.pdf $(GANTT_BUILD_DIR)/gantt_after.pdf

$(GANTT_PDF): $(GANTT_BUILD_DIR)/%.pdf : $(GANTT_DIR)/%.tex
	$(call pdflatex,$(GANTT_BUILD_DIR),$<)

report_ensta.pdf: report_ensta.tex ${TEX_SRCS} $(GANTT_PDF) $(IMAGES_PGF)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)
	$(call glossary,$(ENSTA_BUILD_DIR),report_ensta)
	$(call bibliography,$(ENSTA_BUILD_DIR),report_ensta)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)
	$(call pdflatex,$(ENSTA_BUILD_DIR),$<)

report_angers.pdf: report_angers.tex ${TEX_SRCS} $(GANTT_PDF) $(IMAGES_PGF)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)
	$(call glossary,$(ANGERS_BUILD_DIR),report_angers)
	$(call bibliography,$(ANGERS_BUILD_DIR),report_angers)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)
	$(call pdflatex,$(ANGERS_BUILD_DIR),$<)