build:
	mkdir -p dist
	gcc -Wall -m64 -fno-stack-protector -O0 -o dist/main src/main.c
	gcc -Wall -m64 -fno-stack-protector -O0 -o dist/client src/client.c

clean:
	$(RM) dist/*
