# Project Management
venv:
    uv venv .venv

freeze:
    uv pip freeze > requirements.txt

install:
    uv pip install -r requirements.txt

update:
    uv pip install --upgrade -r requirements.txt
    uv pip freeze > requirements.txt

alias upgrade := update


# Development
alias run := serve
serve:
    .venv/bin/marimo edit
