#include <stdio.h>

const char *hello_world = "Hello World!";
char *among_us = "Among US";
char lorem_ipsum[] = "Lorem Ipsum";
char *unknown;

void print_all()
{
    char *name = "yellow";

    printf("%s\n", hello_world);
    printf("%s\n", among_us);
    printf("%s\n", lorem_ipsum);

    printf("What is your name? ");
    scanf("%16s", unknown);

    printf("Hello, %s! My name's %s!\n", unknown, name);
}

int main()
{
    print_all();
}
