#include <stdio.h>

int main(void)
{
    int n = 5;
    int *p = &n;
    printf("%i\n", *p);
    *p = 2;
    n =  n-n;
    printf("%i\n", *p);
    printf("%i\n", n);
}
