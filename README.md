# 📝 Telegram bot template
Production-ready Telegram bot template based on aiogram 3.
Includes i18n (rus, eng), clean project structure, and environment-based configuration.

## 📦 Stack:
- `Python >=3.12` - Python version
- `aiogram` — Main telegram bot framework
- `fluentogram` —  Internationalization (i18n) with Fluent
- `dynaconf` — Flexible and environment-based settings management
- `uv` - Fast Python package manager
- `ruff` - Code formatting and linting

---

## 🚀 Getting Started:

1. **Clone this template:**

```bash
git clone https://github.com/Ku-Alex-Bo/telegram_bot_template
cd telegram_bot_template
```

2. **Install uv**
```bash
pip install uv
```

3. **Set up environment variables**
```bash
make setup-env
```
Then configure your .env file (e.g., add bot token and other settings).

4. **Run the bot**
```bash
make run
```

## 📂 Project Structure
```
telegram_bot_template/
├── app/
│   └── bot/
│       ├── bot.py            # Bot initialization and setup
│       ├── handlers/         # Message and callback handlers
│       ├── keyboards/        # Inline and reply keyboards
│       ├── middlewares/      # Custom middlewares
│       └── utils/            # Helper utilities
│
├── config/
│   ├── config.py             # Dynaconf configuration loader
│   └── settings.toml         # Base settings
│
├── locales/
│   ├── en/                   # English translations
│   └── ru/                   # Russian translations
│
├── main.py                   # Application entrypoint
├── Makefile                  # Common development commands
├── pyproject.toml            # Project metadata and dependencies
└── README.md
```
## 🌍 Internationalization (i18n)

The template includes built-in internationalization using fluentogram.

- Supported languages out of the box: **English (EN)** and **Russian (RU)**
- Fluent (`.ftl`) translation files
- Middleware-based language detection
- Easy to add new languages

Translations are stored in the `locales/` directory:
```
locales/
├── en/
└── ru/
```
To add a new language:
1. Create a new folder in `locales/` (e.g. `de/`)
2. Add Fluent translation files
3. Register the language in the i18n configuration

## 🛠 Makefile commands

```bash
make run        # Run the bot
make setup-env  # Create .env file
```

## 📄 License

MIT
