# config.py
import os

# Base directory for the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Paths for specific files
HARMONIZATION_OUTPUT_DIR = os.path.join(BASE_DIR, "armonized_jsons")
PATIENT_PANEL_OUTPUT_DIR = os.path.join(BASE_DIR, "patient_panels")

# General settings
DEBUG_MODE = True
MAX_ROWS_TO_PROCESS = 100

