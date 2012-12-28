# mixedCase.nl
The source of (the new) mixedCase.nl, static files generated with [Felix Felicis](https://github.com/lepture/liquidluck).

## Building locally

1. `$ git clone git@github.com:kevinrenskers/mixedcase.nl.git`
2. `$ cd mixedcase.nl`
3. `$ virtualenv env`
4. `$ . env/bin/activate`
5. `$ pip install -r requirements.txt`
6. `$ make html`
7. `$ liquidluck server`

## Publish

1. `$ make publish`
