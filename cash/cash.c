#include <cs50.h>
#include <stdio.h>
int get_cents(void);
int calculate_ten(int cents);
int calculate_five(int cents);
int calculate_two(int cents);
int calculate_one(int cents);
// main function
int main(void)
{
    int cents = get_cents();

    int ten = calculate_ten(cents);
    cents = cents - ten * 25;

    int five = calculate_five(cents);
    cents = cents - five * 10;

    int two = calculate_two(cents);
    cents = cents - two * 5;

    int one = calculate_one(cents);
    cents = cents - one * 1;

    int coins = ten + five + two + one;

    printf("%i\n", coins);
}
int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Change Owned: ");
    }
    while (cents < 0);
    return cents;
}
int calculate_ten(int cents)
{
    int ten = 0;
    while (cents >= 25)
    {
        cents = cents - 25;
        ten++;
    }
    return ten;
}
int calculate_five(int cents)
{
    int five = 0;
    while (cents >= 10)
    {
        cents = cents - 10;
        five++;
    }
    return five;
}
int calculate_two(int cents)
{
    int two = 0;
    while (cents >= 5)
    {
        cents = cents - 5;
        two++;
    }
    return two;
}
int calculate_one(int cents)
{
    int one = 0;
    while (cents >= 1)
    {
        cents = cents - 1;
        one++;
    }
    return one;
}
