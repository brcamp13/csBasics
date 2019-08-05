# Python binary search implementation sourced from geeksforgeeks

def binarySearch(arr, left, right, target):
    # Check base case
    if right >= left:

        mid = int(left + (right - left)/2)

        # If target is the middle element
        if arr[mid] == target:
            return mid

        # If target is smaller than mid, must be in left array
        elif arr[mid] > target:
            return binarySearch(arr, left, mid-1, target)

        # Otherwise element must be in right array
        else: 
            return binarySearch(arr, mid + 1, right, target)

    # Element is not present in the array
    else:
        return -1

if __name__ == "__main__":
    items = [1, 2, 3, 45, 47, 55, 66, 69, 125]
    targetItem = binarySearch(items, 0, len(items)-1, 2)
    print(targetItem)
