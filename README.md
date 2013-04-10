# mixedCase.nl
The source of (the new) mixedCase.nl, static files generated with [Felix Felicis](https://github.com/lepture/liquidluck).

## Getting started

1. `git clone git@github.com:kevinrenskers/mixedcase.nl.git`
2. `cd mixedcase.nl`
3. `virtualenv env`
4. `. env/bin/activate`
5. `pip install -r requirements.txt`
6. `make html`

## Viewing locally
With tornado installed (included in requirements.txt) the preview server auto-reloads on content changes, saving you from running `make html` and restarting the server.

1. `liquidluck server`
2. `open 127.0.0.1:8000`

## Publish to GitHub pages

1. `make publish`
