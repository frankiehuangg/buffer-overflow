build:
	mkdir -p dist
	gcc -Wall -m64 -fno-stack-protector -z execstack -no-pie -o dist/main src/main.c

clean:
	$(RM) dist/*
