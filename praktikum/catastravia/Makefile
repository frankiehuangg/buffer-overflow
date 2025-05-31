build:
	mkdir -p dist
	gcc -Wall -m64 -fno-stack-protector -no-pie -o dist/main src/main.c
	gcc -Wall -m64 -fno-stack-protector -no-pie -o dist/client src/client.c

clean:
	$(RM) dist/*
