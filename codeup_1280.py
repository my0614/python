
#include <stdio.h>

int main()
{
    int a,b;
    int cnt = 0;
    scanf("%d %d",&a,&b);
    for(int i=a;i<=b;i++)
    {
        if(i%2 == 0)
        {
            cnt+= -1 * i;
            printf("-%d",i);
        }
        else
        {
            cnt += i;
            printf("+%d",i);
        }
    }
    printf("=%d",cnt);

    return 0;
}
