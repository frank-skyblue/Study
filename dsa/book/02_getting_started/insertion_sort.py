def insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        cur_num = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > cur_num:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = cur_num

if __name__ == "__main__":
    arr1 = [2,1,3,5,7]
    print(arr1)
    insertion_sort(arr1)
    print(arr1)