# Streamlit Template

This Streamlit template is a starting point for creating Streamlit applications with sensible defaults. It includes a basic structure for a multi-page application, basic authentication, a script runner to install dependencies, run the application, tests, linter, formatter, and a simple data generator.

## Setup Instructions

1. Install [Miniconda](https://docs.anaconda.com/free/miniconda/)
2. Install [Just](https://github.com/casey/just)
3. Create a conda environment with `just install`

## Usage

Launch the Streamlit application with `just dev` (to bypass authentication) or `just run`. Navigate to `http://localhost:8501` in your web browser to interact with the Streamlit application.

The script runner `just` exposes some useful commands in the `justfile`:
-  `just lint`: Run the Ruff code linter and formatter on the codebase.
-  `just test`: Run the unit tests.
-  `just generate`: Generate data.
