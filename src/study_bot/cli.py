import os, enum
import click
from dotenv import load_dotenv
# import core modules here
from study_bot.llm.base import LLMClient
from study_bot.llm.gemini_client import GeminiClient


class Mode(enum.StrEnum):
    PARSE = 'parse'
    SUMMARY = 'summary'
    CARDS = 'cards'
    CONFIG = 'config'


def create_llm_client(provider:str, model: str) -> LLMClient:
    client: LLMClient
    api_key: str

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    # TODO: setup provider & model options and defaults
    if provider != "gemini" or model != 'gemini-3-flash-preview':
        return None
    elif api_key == None:
        # Can raise a custom exception, or do this only if a api key is required.
        return None
    else:
        client = GeminiClient(api_key)
        return client


@click.command()
@click.argument(
    'mode',
    type=click.Choice(Mode, case_sensitive=False),
    nargs=1
)
# TODO: Make the filename arg not required for 'config' mode & also testing
#@click.argument(
#    'filename',
#    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
#    nargs=1
#)
def main(mode: str): # TODO: add filename: str to main
    client: LLMClient
    
    click.echo("This is a study automation tool.")

    if mode == Mode.PARSE:
        # do unique parse checks & call parse module
        click.echo("Entered PARSE mode.")
    elif mode == Mode.SUMMARY:
        # do unique checks & call summary module
        click.echo("Entered SUMMARY mode.")
    elif mode == Mode.CARDS:
        # do unique checks & call cards module
        click.echo("Entered CARDS mode.")
    elif mode == Mode.CONFIG:
        # enter config (either core module or coupled with cli)
        click.echo("Entered CONFIG mode.")

    # Prototype
    client = create_llm_client("gemini", 'gemini-3-flash-preview')
    if client is not None:
        click.echo(
            client.generate(prompt="Explain how AI works in a few words.")
        )
        client.close()
    else:
        click.echo("No client configured.")
        return 1

    return 0

if __name__ == "__main__":
    main()
