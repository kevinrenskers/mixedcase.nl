server:
	liquidluck server

clean:
	rm -fr deploy

html: clean
	liquidluck build

publish: html
	ghp-import deploy -p -m "Update site"
