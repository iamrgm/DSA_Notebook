#include<stdio.h>
int search(int arr[],int n,int s) 
{ 	
	int i; 
	for (i=0;i<n;i++) 
        if (arr[i]==s) 
            return i; 
    return -1; 
} 
  
int main() 
{ 
	int n,i,s,res;
    int arr[] = { 2, 3, 4, 10, 40 }; 
    printf("Enter Number of Elements:");
	scanf("%d",&n);
	printf("Enter Elements: ");
	for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
	printf("Enter Search Element:");
	scanf("%d",&s);
    res=search(arr,n,s); 
    if (res==-1)
		printf("Element is not Present in the Array");
	else
		printf("Element is Present at Index %d", res); 
    return 0; 
} 
