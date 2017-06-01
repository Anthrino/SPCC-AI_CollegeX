#include<stdio.h>
#include<conio.h>
int n, cost, i,j,v,s,pos,min,count;
int d[10];
int varr[10];
int w[10][10];
void comp_cost();
int cal_src();
void display_soln();
int main()
{
 //clrscr();
 printf("Enter the no. of vertices\n");
 scanf("%d",&n);
 printf("Enter the cost of the path. If there is no path enter -1");
 for(i=1;i<=n;i++)
 {  d[i] = -1;
 varr[i]= -1;
  for(j=1;j<=n;j++)
   {
     printf("\nEnter the weight of path from %d to %d: ",i,j);
     scanf("%d", &w[i][j]);
     }
   }
  printf("Enter the source vertex index\n");
  scanf("%d",&v);
  count = n;
  s = v;
  comp_cost();
  display_soln();
  getch();
}
void comp_cost()
{
	while(count != 0)
	{

		for(i=1;i<=n;i++)
		{

		if(w[s][i] != -1)
		{
			if(d[i] == -1)
			{
			if(d[s] == -1)
			d[i] = w[s][i] ;
			else
			d[i] = d[s] + w[s][i];
			}
			else
			 if(d[i] > (d[s]+w[s][i]))
			 d[i] = d[s] + w[s][i];
		}
      }
      varr[s] = 1;
		s = cal_src();
		count--;

	}
}
int cal_src()
{
	for(i=1;i<=n;i++)
	{
		if(varr[i] != 1)
		{       if(d[i] != -1)
			 {
				min = d[i];
				pos = i;
				break;
			 }

		}
	}
	for(i = 1; i<=n;i++)
	{
		if( varr[i] != 1 && d[i] != -1 )
		 {
			if ( min>d[i])
			 {
			  min = d[i];
			 pos = i;
		     }
	 }

    }
    return pos;
}
void display_soln()
{
	for(i = 1;i <= n; i++)
	{

		printf("%d ",d[i]);

	}
}
