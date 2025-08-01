.PHONY: install install-dev setup-env setup-venv run

setup-venv:
	python3 -m venv venv
	@echo "✅  Virtual environment created."
	@echo "➡️  Run 'source venv/bin/activate' (Linux/macOS) or 'venv\\Scripts\\activate' (Windows) to activate it."

install:
	pip install .
	@echo "✅ Requirements installed"

install-dev:
	pip install .
	@echo "✅ All Requirements installed"

setup-env:
	@if [ ! -f .env ]; then \
		cp .env.example .env && echo "✅ .env file created"; \
	else \
		echo "⚠️ .env file already exists"; \
	fi

run:
	python main.py
