MIN_PYTHON_VERSION = 3.11.0

PYTHON_VERSION := $(shell python3 --version 2>&1 | awk '{print $$2}')


check-python-version:
	@echo "Checking python version..."
	@if [ "$(shell printf "$(PYTHON_VERSION)\n$(MIN_PYTHON_VERSION)" | sort -V | head -n1)" != "$(MIN_PYTHON_VERSION)" ]; then \
        echo "ERROR: Python 3.11.0 or higher is required. You are using $(PYTHON_VERSION)"; \
        exit 1; \
    fi

init: check-python-version
	python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install poetry && \
    poetry install && \
    pre-commit install
