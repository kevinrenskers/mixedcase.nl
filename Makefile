html:
	rm -fr deploy
	liquidluck build

publish: html
	ghp-import deploy -p -m "Update site"
