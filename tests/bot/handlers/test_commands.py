from unittest.mock import AsyncMock, MagicMock

import pytest

from app.bot.handlers.commands import help_cmd, start_cmd


@pytest.mark.asyncio
async def test_start_cmd():
    message = AsyncMock()
    message.from_user = MagicMock()
    message.from_user.full_name = "Alex Test"

    i18n = MagicMock()
    i18n.welcome.text.return_value = "👋 Добро пожаловать в SerBuddy, Alex Test!"

    await start_cmd(message=message, i18n=i18n)

    message.answer.assert_awaited_once_with(
        text="👋 Добро пожаловать в SerBuddy, Alex Test!",
    )


@pytest.mark.asyncio
async def test_help_cmd():
    message = AsyncMock()

    i18n = MagicMock()
    i18n.help.text.return_value = "📄Это пример простого бота."

    await help_cmd(message=message, i18n=i18n)

    message.answer.assert_awaited_once_with(
        text="📄Это пример простого бота.",
    )
