def sort_array(arr,n):
    sor_arr = sorted(arr)
    if sor_arr== arr:
        print("yes")
        print(1,1)
    else:
        left = 0
        right = n-1
        while left < n-1 and arr[left] < arr[left+1]:
            left += 1
        while right > 0 and arr[right] > arr[right-1]:
            right -= 1
        arr[left:right+1] = arr[left:right+1][::-1]
        if arr == sor_arr:
            print("yes")
            print(left+1,right+1)
        else:
            print("no")
n = int(input())
arr = list(map(int, input().split()))

sort_array(arr,n)