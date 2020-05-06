#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //creating an integer n value to use for the number of stairs up/down
    int n;
    //do while loop will ask the question once, then perform an action til the while loop is complete
    do
    {
        n = get_int("How many blocks do you want to build?");
    }
    while(n < 1);
    for (int i = 1; i <= n; i++)
    {
        for(int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

//this current block of code is my "finisher"
//i need to first write the code to input n-1 spacesbefore the line, then i need the code to put n hashes
//code to put two spaces every time
//the i need this code for the last hashes and the new line
