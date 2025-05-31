#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 16

extern char *gets(char *);

void setup()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    srand(time(NULL));
}

int main()
{
    char buf[64];
    uint64_t numbers[N];
    int n, i = 0, operation;
    uint64_t operand, guess;
    char ans;

    setup();

    for (int i = 0; i < N; i++)
    {
        numbers[i] = (uint64_t)rand() * (uint64_t)rand();
    }

    printf("Guess time!\n");
    printf("How many numbers can you guess?\n> ");
    scanf("%d%*c", &n);
    printf("Let's see if it's true!\n");

    while (i < n)
    {
        printf("Round %d\n", i + 1);
        printf("I can let you do math on the number. Do you want it?\n> ");
        scanf("%c%*c", &ans);
        if (ans == 'y' || ans == 'Y')
        {
            uint64_t temp = numbers[i];
            printf("Available operations:\n1. add\n2. subtract\n3. multiply\n4. divide\n> ");
            scanf("%d%*c", &operation);
            switch (operation)
            {
            case 1:
                printf("Give operand.\n> ");
                scanf("%lu%*c", &operand);
                temp += operand;
                break;
            case 2:
                printf("Give operand.\n> ");
                scanf("%lu%*c", &operand);
                temp -= operand;
                break;
            case 3:
                printf("Give operand.\n> ");
                scanf("%lu%*c", &operand);
                temp *= operand;
                break;
            case 4:
                printf("Give operand.\n> ");
                scanf("%lu%*c", &operand);
                temp /= operand;
                break;
            default:
                printf("Unknown operation\n");
                break;
            }
            printf("Now guess the result!\n> ");
            scanf("%lu%*c", &guess);
            if (guess == temp)
            {
                printf("Wow, You're correct!\n");
            }
            else
            {
                printf("Nope.\n");
            }
        }
        else
        {
            printf("Now guess the number!\n> ");
            scanf("%lu%*c", &guess);
            if (guess == numbers[i])
            {
                printf("Wow, You're correct!\n");
                i++;
            }
            else
            {
                printf("Nope.\n");
                break;
            }
        }
    }

    if (i == n)
    {
        printf("You win!\n");
        printf("Tell me your name.\n> ");
        gets(buf);
        printf("Congratulations, %s!\n", buf);
    }
    else
    {
        printf("You lose.\n");
    }

    return 0;
}
