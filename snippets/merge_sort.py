 
def merge_down(left: list, right: list) -> list:

    out = []
    
    while left and right:
        if left[0] > right[0]:
            out.append(right.pop(0))
        else:
            out.append(left.pop(0))
    
    # Append any remaining elements
    out.extend(left)
    out.extend(right)
    
    return out


def merge_sort(nums: list) -> list:

    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge_down(left, right)


if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(nums))
