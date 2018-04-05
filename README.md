# mixedCase.nl
The source of (the new) mixedCase.nl, static files generated with [Felix Felicis](https://github.com/lepture/liquidluck).

## Getting started

1. `npm -g install surge`
2. `git clone git@github.com:kevinrenskers/mixedcase.nl.git`
3. `cd mixedcase.nl`

### virtualenv

1. `virtualenv -p python2.7 env`
2. `. env/bin/activate`
3. `pip install -r requirements.txt`

## Viewing locally
With tornado installed (included in requirements.txt) the preview server auto-reloads on content changes, saving you from running `make html` and restarting the server.

1. `make serve`
2. `open 127.0.0.1:8000`

## Publish to GitHub pages

Install surge locally, and then:

1. `make publish`
