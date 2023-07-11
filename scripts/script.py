import asyncio
from conf.config_bot import configurat


async def main():
    await configurat()


if __name__ == "__main__":
    asyncio.run(main())
