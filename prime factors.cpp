# include <stdio.h>
# include <math.h>

// A function to print all prime factors of a given number n
void primeFactors(int n)
{
    printf("1 ");
    // Print the number of 2s that divide n
    while (n%2 == 0)
    {
        printf("X %d ", 2);
        n = n/2;
    }

    // n must be odd at this point.  So we can skip one element (Note i = i +2)
    for (int i = 3; i <= sqrt(n); i = i+2)
    {
        // While i divides n, print i and divide n
        while (n%i == 0)
        {
            printf("X %d ", i);
            n = n/i;
        }
    }

    // This condition is to handle the case whien n is a prime number
    // greater than 2
    if (n > 2)
        printf ("X %d ", n);
}

/* Driver program to test above function */
int main()
{
    while (true)
    {
        int n;
        scanf("%d",&n);
        primeFactors(n);
        printf("\n");
    }
    return 0;

}
