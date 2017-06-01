/*	JERIN J JOHN
	1411083
	SE - B2

	Exp 4 : Double Ended Queue using Arrays   */

#include<stdio.h>
#include<conio.h>
int front=-1,rear=-1;
int  deq[100];
void addfront()
{           int val,i;
	    printf("\n\n Enter the element to be added in the dequeue : ");
	    scanf("%d",&val);
	    if(front==-1)
	    {   deq[0]=val;
		front = 0;
		rear = 0; }
	    else
	    {   printf("\n\n The element has been added to the front of the dequeue..");
		for(i=rear;i>=front;i--)
		{ deq[i+1]=deq[i]; }
		rear++;
		deq[front]=val;
	    }
	    getch();

}
void addrear()
{           int val,i;
	    printf("\n\n Enter the element to be added in the dequeue : ");
	    scanf("%d",&val);
	    if(front==-1)
	    {   deq[0]=val;
		front=0;
		rear=0; }
	    else
	    {   printf("\n\n The element has been added to rear of the dequeue..");
		rear++;
		deq[rear]=val;
	    }
	    getch();
}
void deletefront()
{           int i;
	    if(front==-1)
	    {  printf("\n\n Dequeue Empty...deletion not possible "); }
	    else
	    {   printf("\n\n Element deleted = %d",deq[front]);
		for(i=front;i<=rear;i++)
		{ deq[i]=deq[i+1]; }
		rear--;
	    }
	    getch();
}
void deleterear ()
{           int i;
	    if(front==-1)
	    {  printf("\n\n Dequeue Empty...deletion not possible "); }
	    else
	    {  printf("\n\n Element deleted = %d",deq[rear]);
	       rear--;
	    }
	    getch();

}
void display ()
{           int i;
	    if(front==-1)
	    {  printf("\n\n Dequeue Empty..."); }
	    else
	    {   printf(" \n\n |");
		for(i=front;i<=rear;i++)
		{ printf(" %d |",deq[i]); }
	    }
	    getch();
}

void main()
{           int i,val,n,option;
	    clrscr();
	    printf("\n\n Enter the initial  no.of elements in the dequeue : ");
	    scanf("%d",&n);
	    printf("\n\n Enter the elements in the dequeue : ");
	    for(i=0;i<n;i++)
	    {   scanf("%d",&val);
		deq[i]=val; }
	    front=0;rear=n-1;
	    do
	    {   clrscr();
		printf("\n\n Double Ended Queue Operations Menu :- ");
		printf("\n 1. Add element to front end.");
		printf("\n 2. Add element to rear end.");
		printf("\n 3. Delete element from front end.");
		printf("\n 4. Delete element from rear end.");
		printf("\n 5. Display the dequeue.");
		printf("\n 6. Exit.");
		printf("\n\n Enter your option : ");
		scanf("%d",&option);
		switch(option)
		{   case 1: addfront();
				break;
		    case 2: addrear();
				break;
		    case 3: deletefront();
				break;
		    case 4: deleterear();
				break;
		    case 5: display();
				break;   }
	    }while(option!=6);
}



