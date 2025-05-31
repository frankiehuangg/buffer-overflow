build:
	mkdir -p dist
	gcc -Wall -m64 -fno-stack-protector -no-pie -O1 -o dist/main src/main.c
	gcc -Wall -m64 -fno-stack-protector -no-pie -O1 -o dist/client src/client.c

clean:
	$(RM) dist/*
