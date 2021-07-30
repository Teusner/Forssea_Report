# Directory configuration
BUILD_DIR = build
ENSTA_DIR = ensta
ANGERS_DIR = angers
GANTT_DIR = gantt
IMAGES_DIR = imgs
DIAGRAMS_DIR = diagrams
SCRIPT_DIR = scripts
SRCS_DIR = corps

# Directory path combining
ENSTA_BUILD_DIR = $(BUILD_DIR)/$(ENSTA_DIR)
ANGERS_BUILD_DIR = $(BUILD_DIR)/$(ANGERS_DIR)
GANTT_BUILD_DIR = $(BUILD_DIR)/$(GANTT_DIR)
IMAGES_BUILD_DIR = $(BUILD_DIR)/$(IMAGES_DIR)
DIAGRAMS_BUILD_DIR = $(BUILD_DIR)/$(DIAGRAMS_DIR)

# TEX sources
TEX_SRCS := $(wildcard */*.tex)

# Images
IMAGES_PDF = $(IMAGES_BUILD_DIR)/gerstner_wave.pdf $(IMAGES_BUILD_DIR)/gerstner_pixar.pdf $(IMAGES_BUILD_DIR)/courant_constant.pdf $(IMAGES_BUILD_DIR)/noise_courant.pdf $(IMAGES_BUILD_DIR)/noise_perlin.pdf $(IMAGES_BUILD_DIR)/noise_random.pdf $(IMAGES_BUILD_DIR)/rosace_local.pdf $(IMAGES_BUILD_DIR)/rosace_local_simulation.pdf $(IMAGES_BUILD_DIR)/rosace_global.pdf $(IMAGES_BUILD_DIR)/rosace_global_simulation.pdf $(IMAGES_BUILD_DIR)/gerstner_velocity_pressure_depth.pdf $(IMAGES_BUILD_DIR)/absolute_orientation_tracking.pdf

# Diagrams
DIAGRAMS_PDF = $(DIAGRAMS_BUILD_DIR)/sa_latch.pdf $(DIAGRAMS_BUILD_DIR)/sa_tilt.pdf $(DIAGRAMS_BUILD_DIR)/sa_thruster.pdf $(DIAGRAMS_BUILD_DIR)/architecture_logicielle.pdf $(DIAGRAMS_BUILD_DIR)/latch_fsm.pdf $(DIAGRAMS_BUILD_DIR)/ros2_control.pdf $(DIAGRAMS_BUILD_DIR)/sa_rosace.pdf

# Gantt
GANTT_PDF = $(GANTT_BUILD_DIR)/gantt_before.pdf $(GANTT_BUILD_DIR)/gantt_after.pdf

# Directory guard
dir_guard = @mkdir -p $(@D)

# All recipe
all: ensta angers

# Images recipe
images : $(IMAGES_PDF)

$(IMAGES_PDF): $(IMAGES_BUILD_DIR)/%.pdf : $(SCRIPT_DIR)/%.py
	$(dir_guard)
	python3 $< $@

# Diagrams recipe
diagrams: $(DIAGRAMS_PDF)

$(DIAGRAMS_PDF): $(DIAGRAMS_BUILD_DIR)/%.pdf : $(DIAGRAMS_DIR)/%.drawio
	$(dir_guard)
	drawio -x -f pdf --crop -o $@ $<
	
# Gantt recipe
gantt: $(GANTT_PDF)

$(GANTT_PDF): $(GANTT_BUILD_DIR)/%.pdf : $(GANTT_DIR)/%.tex
	$(dir_guard)
	pdflatex --output-directory $(GANTT_BUILD_DIR) $<

# Ensta report recipe
ensta: $(ENSTA_BUILD_DIR)/report_ensta.pdf

$(ENSTA_BUILD_DIR)/report_ensta.pdf: report_ensta.tex ${TEX_SRCS} gantt images diagrams
	$(dir_guard)
	latexmk -pdf -shell-escape -output-directory=$(ENSTA_BUILD_DIR) $<

# Angers report recipe
angers: $(ANGERS_BUILD_DIR)/report_angers.pdf

$(ANGERS_BUILD_DIR)/report_angers.pdf: report_angers.tex ${TEX_SRCS} gantt images diagrams
	$(dir_guard)
	latexmk -pdf -shell-escape -output-directory=$(ANGERS_BUILD_DIR) $<

# Clean recipe
clean:
	rm -rf $(BUILD_DIR)