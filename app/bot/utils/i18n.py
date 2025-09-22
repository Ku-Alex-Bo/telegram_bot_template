from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub

DIR_PATH = "locales"


def create_translator_hub() -> TranslatorHub:
    return TranslatorHub(
        locales_map={"ru": ("ru", "en"), "en": ("en", "ru")},
        translators=[
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["locales/ru/LC_MESSAGES/txt.ftl"]
                )
            ),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["locales/en/LC_MESSAGES/txt.ftl"]
                )
            )
        ],
        root_locale="ru"
    )
