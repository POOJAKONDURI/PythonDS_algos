'''

    @Author:pooja
    @Date:09-10-2024
    @last modified by:
    @last modified time:
    @title:program to find bubble sort

'''
def selection_sort(array):  
    length = len(array)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  
                  
        array[i], array[minIndex] = array[minIndex], array[i]  
          
          
    return array  

def main():    
    array = [21,6,9,33,3]  
    
    print("The sorted array is: ", selection_sort(array))  
if __name__ == "__main__":
    main()