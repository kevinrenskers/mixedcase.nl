serve:
	liquidluck server

clean:
	rm -fr deploy

html: clean
	liquidluck build

publish: html
	npm run deploy
