# StudyBot
A personal study tool that automates tasks that I do regularly.

I wanted to use the opportunity presented in wanting to learn tooling & AI integration to create something that I could use. The goal with this tool is to able to automate a few tasks that I do regularly with LLMs for university, namely note summarisation and anki / flash card generation.

## Structure
```
StudyBot/
├── pyproject.toml
├── README.md
├── LICENSE
├── doc/* # see "Notes" below
└── src/
    └── study_bot/
        ├── __init__.py
        ├── cli.py
        ├── config.py
        ├── core/
        |   ├── __init__.py
        |   ├── pdf_parser.py
        |   ├── summariser.py
        |   └── card_generator.py
        └── llm/
            ├── __init__.py
            ├── base.py
            └── gemini_client.py
```

### Notes
- `core/` should contain all of the logic that is independent of the control layer, i.e. can be wrapped in any UI
- `doc/` see this for further documentation and notes
- `cli.py` will be the first interface implemented. Would like to create a web API in the future for self-hosting this tool.
- `llm` abstracts any logic that is concerned with model API interaction. This is modelled as a strategy design pattern,
allowing each LLM clients to be interchangeable. This will helpful in the future for integrating Ollama. Initially, I will
implement cloud hosted clients.

# Development
1. Setup virtual environment for environment isolation: `python -m venv .venv`
2. Activate virtual environment: `source .venv/bin/activate` (Linux)
3. Install project executable & dependencies: `pip install -e .` ('e' - for editable, sources from `src` files.)

## Usage
In command line type: `study --help` for options and usage.

## Future Build Options
1. `pip install .` - copies project to `.venv` site packages
2. `python -m build` - builds a "wheel"
3. Create a binary using `pyinstaller`, `pex`, or `shiv`

# Licensing
This project is licensed under the AGPL-3.0.

Dependencies:
- PyMuPDF and pymupdf4llm (AGPL-3.0)
- Layout extension (PolyForm Noncommercial 1.0.0)

NOTE: The layout extension may only be used for noncommercial purposes.
Commercial use of features relying on the layout extension is prohibited by its license.
