.PHONY: install setup-env run

install:
	pip install .
	@echo "✅ Requirements installed"

setup-env:
	@if [ ! -f .env ]; then \
		cp .env.example .env && echo "✅ .env file created"; \
	else \
		echo "⚠️ .env file already exists"; \
	fi

setup-venv:
	python3 -m venv venv
	@echo "✅  Virtual environment created."
	@echo "➡️  Run 'source venv/bin/activate' (Linux/macOS) or 'venv\\Scripts\\activate' (Windows) to activate it."

run:
	python main.py
