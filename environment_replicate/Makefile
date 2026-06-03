PYTHON_VERSION := 3.11.8
PYENV_ROOT := $(USERPROFILE)/.pyenv/pyenv-win
PKG := pytest ruff black

.PHONY: install install-pyenv install-python install-poetry add exportrequirements lint test run clean

# ----------------------------
# INSTALL EVERYTHING
# ----------------------------

install: install-pyenv install-python install-poetry add exportrequirements run test

# ----------------------------
# PYENV
# ----------------------------
install-pyenv:
ifeq ($(OS),Windows_NT)
	@if not exist "$(PYENV_ROOT)" ( \
		echo Installing pyenv-win... && \
		git clone https://github.com/pyenv-win/pyenv-win.git $(USERPROFILE)\.pyenv \
	) else ( \
		echo pyenv already installed \
	)
endif

# ----------------------------
# PYTHON
# ----------------------------
install-python:
ifeq ($(OS),Windows_NT)
	@set PATH=$(PYENV_ROOT)\bin;$(PYENV_ROOT)\shims;$(PATH) && \
	pyenv install -s $(PYTHON_VERSION) && \
	pyenv local $(PYTHON_VERSION)
endif

# ----------------------------
# POETRY
# ----------------------------
install-poetry:
	@pip install poetry
	@poetry config virtualenvs.in-project true
	@if not exist pyproject.toml poetry init --no-interaction
	@poetry install --no-root

# ----------------------------
# ADD PACKAGES
# ----------------------------
add:
    
	@poetry add $(PKG)
	@echo '---------------------Adding Packages-----------------------'

exportrequirements:
	poetry self add poetry-plugin-export@latest
	poetry export -f requirements.txt -o requirements.txt --without-hashes
# ----------------------------
# RUN
# ----------------------------
run:
	@if not exist src mkdir src
	@if not exist src\main.py echo print("Hello from main") > src\main.py

# ----------------------------
# TEST
# ----------------------------
test:
	@if not exist tests mkdir tests
	@if not exist tests\test_main.py echo def test_dummy(): assert True > tests\test_main.py

# ----------------------------
# LINT
# ----------------------------
lint:
	@poetry run ruff check src/

