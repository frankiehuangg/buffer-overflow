#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 16

struct Notes
{
    char title[16];
    char content[64];
} notes[SIZE];

void win()
{
    printf("How did you get here!? It's not even leakable 😭😭\n");
    system("cat flag.txt");
}

void print_menu()
{
    printf("\n===========================\n");
    printf("=        Notes App        =\n");
    printf("= ----------------------- =\n");
    printf("= 1. Add Note             =\n");
    printf("= 2. View Note            =\n");
    printf("= 3. Change Name          =\n");
    printf("= 4. Exit                 =\n");
    printf("===========================\n");
}

void setup()
{
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    setvbuf(stderr, NULL, 2, 0);
}

int main()
{
    setup();

    printf("Let's start with an easy one!\n");

    char name[64];

    printf("[>] enter your name: ");
    fgets(name, 16, stdin);

    int uinput;
    while (1)
    {
        print_menu();

        printf("[>] user input: ");
        scanf("%d", &uinput);
        getchar();

        if (uinput == 1)
        {
            int index;
            do
            {
                printf("[>] enter note index: ");
                scanf("%d", &index);

                if (index >= 0 && index < SIZE)
                    break;

                printf("[x] invalid index\n");
            } while (1);

            getchar();

            printf("[>] enter note title: ");
            fgets(notes[index].title, 16, stdin);
            notes[index].title[strcspn(notes[index].title, "\n")] = '\0';

            printf("[>] enter note content: ");
            fgets(notes[index].content, 64, stdin);
            notes[index].content[strcspn(notes[index].content, "\n")] = '\0';
        }
        else if (uinput == 2)
        {
            int index;
            do
            {
                printf("[>] enter note index: ");
                scanf("%d", &index);

                if (index >= 0 && index < SIZE)
                    break;

                printf("[x] invalid index\n");
            } while (1);

            printf("===== %s =====\n", notes[index].title);
            printf("written by: ");
            printf(name);
            printf("\n");
            printf(notes[index].content);
            printf("\n");
        }
        else if (uinput == 3)
        {
            getchar();

            printf("[>] enter new author name: ");
            fgets(name, 64, stdin);
        }
        else if (uinput == 4)
        {
            printf("[v] thank you for using our program!\n");
            break;
        }
        else
        {
            printf("[x] unknown user input\n");
        }
    }

    exit(1);
}