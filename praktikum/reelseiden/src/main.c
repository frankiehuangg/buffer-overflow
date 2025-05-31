#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 16
#define MAX_NAME_LEN 40

extern char *gets(char *);

void win()
{
    printf("Wow, you actually managed to understand these messy code? Impressive!\n");
    system("/bin/sh");
}

void print_menu()
{
    printf("\n==========================================\n");
    printf("=           Debt Tracker Program         =\n");
    printf("=                                        =\n");
    printf("= 1. Add debtee                          =\n");
    printf("= 2. Add debt                            =\n");
    printf("= 3. Count debts                         =\n");
    printf("= 4. Quit Program                        =\n");
    printf("==========================================\n\n");
}

int add_debtee(char **names, unsigned *debts, int index, unsigned size)
{
    if (index >= size)
    {
        printf("[x] you have reaced the maximum amount of debtee!\n");
        return 0;
    }

    getchar();

    char name[MAX_NAME_LEN];

    printf("[>] enter debtee's name: ");
    scanf("%39[^\n]", name);

    names[index] = strdup(name);

    printf("[v] debtee %s has been successfully added on index %d!\n", name, index);

    printf("[>] enter debt amount: ");
    scanf("%u", &debts[index]);

    return 1;
}

void add_debt(char **names, unsigned *debts, unsigned size)
{
    int index;
    do
    {
        printf("[>] enter debtee's index: ");
        scanf("%d", &index);

        if (index >= 0 && index < size && names[index] != NULL)
            break;

        if (!names[index])
            printf("[x] debtee not found!\n");
        else
            printf("[x] invalid index\n");
    } while (1);

    int debt;

    printf("[>] enter debt amount: ");
    scanf("%u", &debt);

    debts[index] += debt;
}

void count_debts(char **names, unsigned *debts, unsigned size)
{
    unsigned index;
    do
    {
        printf("[>] enter last index: ");
        scanf("%u", &index);

        if (index >= 0 && index < size)
            break;

        printf("[x] invalid index\n");
    } while (1);

    getchar();

    char c;
    do
    {
        printf("[>] use compact mode? (y/n): ");
        scanf("%c", &c);

        if (c == 'y' || c == 'n')
            break;

        printf("[x] invalid input\n");
    } while (1);

    if (c == 'n')
        printf("=           Debt Lists         =\n");

    unsigned long long total = 0;
    for (int i = 0; i < index; i++)
    {
        if (c == 'n')
            printf("%d. %s - %d\n", i, names[i], debts[i]);

        total += debts[i];
    }

    printf("Total debt to be paid: %llu\n", total);
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

    int size;
    do
    {
        printf("[>] input array size (smaller than %d): ", MAX_SIZE);
        scanf("%d", &size);
    } while (size > MAX_SIZE);

    char *names[MAX_SIZE] = {NULL};

    unsigned debts[MAX_SIZE] = {0};

    int index = 0;

    int uinput;
    while (1)
    {
        print_menu();

        printf("[>] user input: ");
        scanf("%d", &uinput);

        if (uinput == 1)
        {
            index += add_debtee(names, debts, index, size);
        }
        else if (uinput == 2)
        {
            add_debt(names, debts, index);
        }
        else if (uinput == 3)
        {
            count_debts(names, debts, size);
        }
        else if (uinput == 4)
        {
            printf("[v] thank you for using our program!\n");
            break;
        }
        else if (uinput == 0x1337)
        {
            getchar();
            printf("[v] you've found the secret stage!\n");
            gets((char *)&names);
        }
        else
        {
            printf("[x] unknown user input\n");
        }
    }
}
