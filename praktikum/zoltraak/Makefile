build:
	mkdir -p dist
	gcc -Wall -m64 -fno-stack-protector -o dist/client src/client.c
	cd dist && \
		patchelf --set-interpreter ld-linux-x86-64.so.2 client && \
		patchelf --replace-needed libc.so.6 libc.so.6 client && \
		patchelf --set-rpath . client

clean:
	$(RM) dist/*
