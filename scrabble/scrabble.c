#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
int merge(string name);
int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int main(void)
{
    string name_1 = get_string("Enter a name 1: ");
    string name_2 = get_string("Enter a name 2: ");
    int player_1 = merge(name_1);
    int player_2 = merge(name_2);
    if (player_1 > player_2)
    {
        printf("Player 1 wins!\n");
    }
    else if (player_1 < player_2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
int merge(string name)
{
    int score = 0;
    int length = strlen(name);
    for (int i = 0; i < length; i++)
    {
        if (isupper(name[i]))
        {
            score += points[name[i] - 'A'];
        }
        else if (islower(name[i]))
        {
            score += points[name[i] - 'a'];
        }
    }
    return score;
}
