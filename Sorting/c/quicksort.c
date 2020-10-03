#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}
int partition(int arr[], int low, int high)
{
    int key = arr[low];
    int i = low + 1;
    int j = high;

    while (1)
    {
        while (key >= arr[i] && i <= high)
            i++;
        while (key < arr[j] && j >= low)
            j--;
        if (i < j)
            swap(&arr[i], &arr[j]);
        else
        {
            swap(&arr[j], &arr[low]);
            return j;
        }
    }
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now 
           at right place */
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

int main()
{
    int arr[10], n, i;
    printf("Enter No of Elements: ");
    scanf("%d", &n);
    printf("Enter Elements: ");
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    quickSort(arr, 0, n - 1);

    printf("Sorted array: ");
    printArray(arr, n);
    return 0;
}

