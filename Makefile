all: client

.PHONY: client

clean:
	rm -rf build
	rm -rf components
	rm -rf dist

client:
	mkdir -p dist
	duo --use duo-coffee static/coffee/* > dist/build.js
	duo static/css/* > dist/build.css

run:
	go run web.go
