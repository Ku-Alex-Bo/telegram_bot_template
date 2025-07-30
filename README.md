# 📝 Telegram bot template

## 📦 Stack:

- `aiogram` — Main telegram bot framework
- `aiogram-dialog` — Dialogs & FSM handling
- `fluentogram` —  Internationalization (i18n) with Fluent
- `dynaconf` — Flexible and environment-based settings management
- `isort`, `black`, `flake8` - Code formatting and linting

---

## 🚀 Getting Started:

1. **Clone this template:**

```bash
git clone https://github.com/Ku-Alex-Bo/telegram_bot_template
cd telegram_bot_template
```

2. **Create virtual environment:**
```bash
setup-venv
```
Then activate it:
- *Windows*
```bash
venv\Scripts\activate
```
- *Mac/Linux*
```bash
source venv/bin/activate
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
