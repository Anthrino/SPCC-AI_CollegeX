#include <stdio.h>
#include <string.h>
#include <math.h>
void receiver(int a[],int n);
void main()
{	
    int code[10];
    int n,i; int checksum=0;
    char *str="8e";char input[10];
    printf("\n\n Enter the no. of code elements (4-bit) ..");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    { 
        printf("\n Enter code %d : ",i+1);
        gets(input);
        sscanf(str,"%x",&code[i]); 
        checksum=checksum+code[i];
    }
    checksum=~checksum;
    code[n++]=checksum;
    receiver(code,n);
}
void receiver(int data[],int n)
{	
    int sum=0,i;
    for(i=0;i<n;i++)
    {  sum>>sum+data[n]; }
    sum=~sum;
    if(sum==0)		
    {   
        printf("\n\n Code received. No error detected \n\n Data :- \n");
        for(i=0;i<n;i++)
        {  printf("\t\n %x",data[n]); }
    }
    else		 
        printf("\n\n Code received wih errors ");
}


