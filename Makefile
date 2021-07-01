# Directory configuration
BUILD_DIR = build
ENSTA_DIR = ensta
ANGERS_DIR = angers
GANTT_DIR = gantt
PGF_DIR = pgf
SCRIPT_DIR = scripts
SRCS_DIR = corps

# Directory path combining
ENSTA_BUILD_DIR = $(BUILD_DIR)/$(ENSTA_DIR)
ANGERS_BUILD_DIR = $(BUILD_DIR)/$(ANGERS_DIR)
GANTT_BUILD_DIR = $(BUILD_DIR)/$(GANTT_DIR)
IMAGES_BUILD_DIR = $(BUILD_DIR)/$(PGF_DIR)

# TEX sources
TEX_SRCS := $(wildcard */*.tex)

# Images
IMAGES_PGF = $(IMAGES_BUILD_DIR)/gerstner_wave.pgf $(IMAGES_BUILD_DIR)/gerstner_pixar.pgf $(IMAGES_BUILD_DIR)/courant_constant.pgf $(IMAGES_BUILD_DIR)/noise_courant.pgf $(IMAGES_BUILD_DIR)/noise_perlin.pgf $(IMAGES_BUILD_DIR)/noise_random.pgf

# Gantt
GANTT_PDF = $(GANTT_BUILD_DIR)/gantt_before.pdf $(GANTT_BUILD_DIR)/gantt_after.pdf

# Directory guard
dir_guard = @mkdir -p $(@D)

# All recipe
all: ensta angers

# Images recipe
pgf : $(IMAGES_PGF)

$(IMAGES_PGF): $(IMAGES_BUILD_DIR)/%.pgf : $(SCRIPT_DIR)/%.py
	$(dir_guard)
	python3 $< $@
	
# Gantt recipe
gantt: $(GANTT_PDF)

$(GANTT_PDF): $(GANTT_BUILD_DIR)/%.pdf : $(GANTT_DIR)/%.tex
	$(dir_guard)
	pdflatex --output-directory $(GANTT_BUILD_DIR) $<

# Ensta report recipe
ensta: $(ENSTA_BUILD_DIR)/report_ensta.pdf

$(ENSTA_BUILD_DIR)/report_ensta.pdf: report_ensta.tex ${TEX_SRCS} gantt pgf
	$(dir_guard)
	latexmk -pdf -output-directory=$(ENSTA_BUILD_DIR) $<

# Angers report recipe
angers: $(ANGERS_BUILD_DIR)/report_angers.pdf

$(ANGERS_BUILD_DIR)/report_angers.pdf: report_angers.tex ${TEX_SRCS} gantt pgf
	$(dir_guard)
	latexmk -pdf -output-directory=$(ANGERS_BUILD_DIR) $<