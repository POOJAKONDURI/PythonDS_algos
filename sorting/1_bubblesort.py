
'''

    @Author:pooja
    @Date:09-10-2024
    @last modified by:
    @last modified time:
    @title:program to find bubble sort

'''


def bubble_sort(arr):  
    n = len(arr)  
  
    # Traverse through all array elements  
    for i in range(n):  
        # Last i elements are already sorted, so we don't need to check them  
        for j in range(0, n-i-1):  
            # Swap if the element found is greater than the next element  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
  
def main():  
    # Sample list to be sorted  
    sample_list = [64, 34, 25, 12, 22, 11, 90]  

    print("Original List:", sample_list)  
    bubble_sort(sample_list) 
    print("Sorted List:", sample_list)  

if __name__ == "__main__": 
    main()