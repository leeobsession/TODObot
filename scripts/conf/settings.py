from dataclasses import dataclass
from dotenv import get_variables


@dataclass()
class Bots:
    bot_token: str
    admin_id: str


@dataclass()
class Settings:
    bots: Bots


def get_settings():
    config = get_variables('/home/leeobsession/.poetry.venv/TODObot/scripts/conf/.evn')
    #config = get_variables('/home/lee_obsession/TODObot/scripts/conf/.evn')
    return Settings(
        bots=Bots(
            bot_token=config['TOKEN'],
            admin_id=1061789651,
        )
    )


settings = get_settings()