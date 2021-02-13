

def migratoryBirds(arr):
    
    return max(set(arr),key=arr.count)
    

if __name__ == '__main__':
   

    arr_count = int(input().strip())

    arr = list(map(int, input().strip().split()))

    result = migratoryBirds(arr)
    print(result)

   