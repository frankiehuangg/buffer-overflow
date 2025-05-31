#include <stdio.h>

const char *FLAG = "Orkom{b4by's_f1r5t_b0ff_eb7def3975bf0bfa502e81d7302021de}";

extern char *gets(char *);

void setup()
{
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stderr, NULL, 2, 0);
}

int main()
{
    setup();

    int secret = 0xC0DEAB1E;

    char buffer[32];

    printf("Let's start with an easy one!\n> ");

    gets(buffer);

    if (secret != 0xC0DEAB1E)
    {
        printf("Congratz for your first successful buffer overflow!\n");
        printf("You've successfully changed the value secret to 0x%8x\n", secret);
        printf("Here's your flag: %s\n", FLAG);
    }
    else
    {
        printf("Try again!\n");
    }
}