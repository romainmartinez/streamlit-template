# Define variables
# Extract the environment name from environment.yml
env_name := `awk '/name:/ {print $2; exit}' environment.yml`
# Determine the base path of the conda environment
env_base := `[[ $CONDA_PREFIX == *"envs"* ]] && echo $CONDA_PREFIX_1 || echo $CONDA_PREFIX`
# Construct the path to the environment's bin directory
env_bin := env_base / "envs" / env_name / "bin"

# Default target to show a menu of options if no target is specified
default:
    @just --choose --unsorted

# Install dependencies and update the conda environment
install:
    conda env update

# Lint the codebase using ruff for formatting and fixing issues
lint:
    {{ env_bin }}/ruff format
    {{ env_bin }}/ruff check --fix --no-cache --unsafe-fixes

# Run tests using pytest
test:
    {{ env_bin }}/pytest

# Run the Streamlit application
run:
    {{ env_bin }}/streamlit run src/home.py

# Run the Streamlit application in development mode to bypass auth
dev:
    {{ env_bin }}/streamlit run src/home.py -- local

# Generate data
generate_data:
    {{ env_bin }}/python src/bin/generate_data.py
