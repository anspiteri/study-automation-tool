import os
import click
from dotenv import load_dotenv
# import core modules here
from study_bot.llm.base import LLMClient
from study_bot.llm.gemini_client import GeminiClient

@click.command()
@click.option("--provider", default="gemini", help="specify ai vendor")
def main(provider: str):
    client: LLMClient
    api_key: str

    load_dotenv()
    if provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        client = GeminiClient(api_key)
    else:
        # Can raise a custom exception, or do this only if a api key is required.
        api_key = ""
    
    click.echo("This is a study automation tool.")

    if client is not None:
        click.echo(
            client.generate(prompt="Explain how AI works in a few words.")
        )
    else:
        click.echo("No client configured.")


if __name__ == "__main__":
    main()
