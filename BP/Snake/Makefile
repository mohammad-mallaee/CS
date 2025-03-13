outdir:
	mkdir -p out

build: outdir
	javac -d out src/*.java

run: build
	java -cp out Main