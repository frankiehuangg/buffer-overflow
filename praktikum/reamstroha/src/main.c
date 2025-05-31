#include <stdio.h>

extern char *gets(char *);

void setup()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main()
{
    char buf[15];
    char answer;
    setup();

    printf("Oops... something's leaking.\n");
    printf("%p\n", buf);

    printf("Well, I bet you can't do anything with that, though.\n");
    printf("Right?\n> ");

    scanf("%c%*c", &answer);
    if (answer == 'y' || answer == 'Y')
    {
        printf("Now we're talking.\n");
        printf("Just stop breaking my program, will you?\n");
    }
    else if (answer == 'n' || answer == 'N')
    {
        printf("That's interesting. Show me what will you do?\n> ");
        gets(buf);
        printf("Let's see what happens now!\n");
    }
    else
    {
        printf("I don't understand.\n");
    }
    return 0;
}
