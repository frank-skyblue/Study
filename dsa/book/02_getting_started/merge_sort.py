def merge(nums, p, q, r):
    n_left = q - p + 1
    n_right = r - q

    left_nums = []
    right_nums = []

    # copy over left array
    for i in range(n_left):
        left_nums.append(nums[p + i])
    # copy over right array
    for i in range(n_right):
        right_nums.append(nums[q + 1 + i])
    
    i = 0
    j = 0
    k = p
    # as long as both left and right arrays still contain value, copy over to nums
    while i < n_left and j < n_right:
        if left_nums[i] < right_nums[j]:
            nums[k] = left_nums[i]
            i += 1
        else:
            nums[k] = right_nums[j]
            j += 1
        k += 1
    
    # copy over remainder of left, if any
    while i < n_left:
        nums[k] = left_nums[i]
        i += 1
        k += 1
    # copy over remainder of right, if any
    while j < n_right:
        nums[k] = right_nums[j]
        j += 1
        k += 1

def merge_sort(nums, p, r):
    # zero or 1 element
    if p >= r:
        return

    q = (p + r) // 2
    merge_sort(nums, p, q)
    merge_sort(nums, q + 1, r)
    merge(nums, p, q, r)

if __name__ == "__main__":
    arr1 = [2,1,3,5,7,0]
    print(arr1)
    merge_sort(arr1, 0, 5)
    print(arr1)