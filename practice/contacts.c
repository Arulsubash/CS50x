#include <cs50.h>
#include <stdio.h>
int main(void)
{
    string First_name = get_string("First Name:");
    string Second_name = get_string("Second Name:");
    
    string Number = get_string("Phone number:");
    printf("Contact... %s %s %s\n", First_name, Second_name, Number);
}
