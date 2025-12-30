#include <cs50.h>
#include <stdio.h>

int main(void)
{
    typedef struct
    {
        string name;
        int votes;
    } candinates;
    const int n = 3;
    candinates result[n];
    for (int i = 0; i < n; i++)
    {
        result[i].name = get_string("Enter Candinate: ");
        result[i].votes = get_int("Enter votes: ");
    }
    if (result[0].votes > result[1].votes && result[2].votes)
    {
        printf{"Result: The winner is %s recived %i\n",result[0].name,result[0].votes};
    }
    else if (result[1].votes > result[0].votes && result[2].votes)
    {
      printf{"Result: The winner is %s recived %i\n",result[1].name,result[1].votes};
    }
    else
    {
      printf{"Result: The winner is %s recived %i\n",result[2].name,result[2].votes};
    }
}
