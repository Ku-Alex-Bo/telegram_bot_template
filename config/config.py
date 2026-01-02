from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix=False,
    environments=True,
    env_switcher="ENV_FOR_DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    load_dotenv=True,
)
