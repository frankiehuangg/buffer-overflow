#include <stdio.h>
#include <string.h>

void setup()
{
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stderr, NULL, 2, 0);
}

int main()
{
    setup();

    const char *FLAG = "Orkom{wh0_tH3_h31L_c0deS_liK3_thaT???_1f773a748f102e217e7589006ab24797}";

    char input[64];

    printf("I just realised that i can hide the FLAG in the stack!\n");
    printf("Now you can't leak it anymore, haha!\n");

    printf("Guess the flag!\ninput> ");
    scanf("%63s", input);

    if (strcmp(input, FLAG))
    {
        printf("Haha, ");
        printf(input);
        printf(" is not the flag!");
    }
    else
    {
        printf("That is... correct... How did you do it!?\n");
    }
}