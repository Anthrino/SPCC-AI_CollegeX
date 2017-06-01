#include<stdio.h>
#include<time.h>
#include<conio.h>
void knapsack(float capacity,int n, float weight[], float profit[], float ratio[] ,int choice)
{
	float x[20],totalprofit,y,t1,t2,t3;
	int i,j,wtindex[20][2],temp;
	y=capacity;
	totalprofit=0;
	for(i=0;i<n;i++)
	{  wtindex[i][2]=weight[i];  }
	switch(choice)
	{  case 1:for(i=0;i<n;i++)
		  {  for(j=0;j<n;j++)
		     {  if(profit[i]>profit[j])
			{ t2=weight[i];
			  weight[i]=weight[j];
			  weight[j]=t2;
			  t3=profit[i];
			  profit[i]=profit[j];
			  profit[j]=t3;
			}
		     }
		  }
	   case 2:for(i=0;i<n;i++)
		  {  for(j=0;j<n;j++)
		     {  if(weight[i]<weight[j])
			{ t2=weight[i];
			  weight[i]=weight[j];
			  weight[j]=t2;
			  t3=profit[i];
			  profit[i]=profit[j];
			  profit[j]=t3;
			}
		     }
		  }
	   case 3:for(i=0;i<n;i++)
		  {  for(j=0;j<n;j++)
		     {  if(ratio[i]>ratio[j])
			{ t1=ratio[i];
			  ratio[i]=ratio[j];
			  ratio[j]=t1;
			  t2=weight[i];
			  weight[i]=weight[j];
			  weight[j]=t2;
			  t3=profit[i];
			  profit[i]=profit[j];
			  profit[j]=t3;
			}
		     }
		  }
	   }
	for(i=0;i<n;i++)
	{ x[i]=0.0; }
	for(i=0;i<n;i++)
	{  if(weight[i]>y)
	     break;
	   else
	   {
	     x[i]=1.0;
	     totalprofit=totalprofit+profit[i];
	     y=y-weight[i];
	   }
	}
	if(i<n)
	{ x[i]=y/weight[i]; }
	totalprofit=totalprofit+(x[i]*profit[i]);
	for(i=0;i<n;i++)
	{  t1=wtindex[i][2];
	   j=0;
	   while(weight[j]==t1)
	   {  j++; }
	   wtindex[i][1]=x[j];
	}
	printf("\n\n The selected elements are : \n ");
	for(i=0;i<n;i++)
	{  if(x[i]==1.0)
	     printf("\n Object with Profit %.2f and weight %.2f ", profit[i], weight[i]);
	   else if(x[i]>0.0)
	     printf("\n %.2f fraction of object with Profit %.2f with weight %.2f", x[i], profit[i], weight[i]);
	}
	printf("\n\n Total profit for %d objects with capacity %.2f = %.2f\n\n", n, capacity,totalprofit);
	printf("\n\n Vector Soln is :- \n\t");
	for(i=0;i<n;i++)
	{  printf("| %.1f |",x[i]); }

}
void main()
{
	float weight[20],profit[20],ratio[20];
	int n,i,j,choice;
	time_t start,stop;
	float capacity;
	clrscr();
	printf("\n Enter number of objects: ");
	scanf("%d", &n);
	printf("\n Enter the capacity of knapsack: ");
	scanf("%f", &capacity);
	for(i=0;i < n;i++)
	{
		printf("\n Enter profit for Obj %d: ", (i+1));
		scanf("%f", &profit[i]);
		printf(" Enter weight for Obj %d: ", (i+1));
		scanf("%f", &weight[i]);
		ratio[i]=profit[i]/weight[i];
	}
	printf("\n Enter case for calculation : ");
	printf("\n\n 1. Maximum Profit case ");
	printf("\n 2. Minimum Weight case ");
	printf("\n 3. Profit/Weight ratio ");
	printf("\n\n Enter option : ");
	scanf("%d",&choice);
	start=time(NULL);
	knapsack(capacity,n,weight,profit,ratio,choice);
	stop=time(NULL);
	printf("\n\n\n Time taken for Knapsack Algorithm = %f\n", difftime(stop,start));
	getch();
}