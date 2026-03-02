import os, enum
import click
from dotenv import load_dotenv
# import core modules here
from study_bot.llm.base import LLMClient
from study_bot.llm.gemini_client import GeminiClient


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


def input_file_argument(f):
    return click.argument(
        'filename',
        type=click.Path(exists=True, dir_okay=False, readable=True),
        nargs=1
    )(f)


@click.group()
def main():
    """
    This is a study automation tool. 

    Takes input in the form of .pdf, and outputs in markdown or json syntax as text to stdout.
    """
    # Perform any globally required operations here, like loading stored config.

    click.echo("This is a study automation tool.")


@main.command()
@input_file_argument
def parse(input_file: str):
    """
    Parses a pdf document into structured json.
    """
    # do unique parse checks & call parse module
    click.echo("Entered PARSE mode.")


@main.command()
def config():
    """
    Allows the change of stored configuration.
    """
    click.echo("Entered CONFIG mode.")


@main.group
def generate():
    """
    Parses a pdf file into a specified output.
    """
    client: LLMClient
    click.echo("Hi, this is generate.")
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


@generate.command()
@input_file_argument
def summary(input_file: str):
    """
    Output a concise summary in markdown syntax.
    """
    # do unique checks & call summary module
    click.echo("Entered SUMMARY mode.")


@generate.command()
@input_file_argument
def cards(input_file: str):
    """
    Outout anki cards in markdown syntax.
    """
    # do unique checks & call cards module
    click.echo("Entered CARDS mode.")


if __name__ == "__main__":
    main()
