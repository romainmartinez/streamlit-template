# Variables

env_name := `awk '/name:/ {print $2; exit}' environment.yml`
env_base := `[[ $CONDA_PREFIX == *"envs"* ]] && echo $CONDA_PREFIX_1 || echo $CONDA_PREFIX`
env_bin := env_base / "envs" / env_name / "bin"

default:
    @just --choose --unsorted

install:
    conda env update

lint:
    {{ env_bin }}/ruff format
    {{ env_bin }}/ruff check --fix --no-cache --unsafe-fixes

test:
    {{ env_bin }}/pytest

run:
    {{ env_bin }}/streamlit run src/home.py

dev:
    {{ env_bin }}/streamlit run src/home.py --local

generate_data:
    @echo "Generating data..."
