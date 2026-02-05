import os

# Project root dir
SRC_DIR = os.path.abspath(os.path.join(__file__, os.pardir))

# Repository root dir
REPO_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

# Path to folder where data is stored
DATA_DIR = os.path.join(REPO_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Path to folder where data is stored
OUTPUT_DIR = os.path.join(REPO_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
