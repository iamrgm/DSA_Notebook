def merge_sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        left_arr = arr[:mid]  
        right_arr = arr[mid:] 
        merge_sort(left_arr) 
        merge_sort(right_arr)  
  
        left_iter = right_iter = merge_iter = 0
        while left_iter < len(left_arr) and right_iter < len(right_arr): 
            if left_arr[left_iter] < right_arr[right_iter]: 
                arr[merge_iter] = left_arr[left_iter] 
                left_iter+= 1
            else: 
                arr[merge_iter] = right_arr[right_iter] 
                right_iter+= 1
            merge_iter+= 1
        while left_iter < len(left_arr): 
            arr[merge_iter] = left_arr[left_iter] 
            left_iter+= 1
            merge_iter+= 1
          
        while right_iter < len(right_arr): 
            arr[merge_iter] = right_arr[right_iter] 
            right_iter+= 1
            merge_iter+= 1
def main():
    print("Enter an array of numbers")
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print("After sorting the array")
    print(arr)
if __name__=="__main__":
    main()