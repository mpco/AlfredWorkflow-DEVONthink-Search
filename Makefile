all: build open

open:
	open ~/Desktop/DEVONthink\ Search.alfredworkflow

build:
	zip -r ~/Desktop/DEVONthink\ Search.alfredworkflow . -x '*.git*'
