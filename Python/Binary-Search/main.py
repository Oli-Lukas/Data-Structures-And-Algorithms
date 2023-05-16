def binary_search(array, left, right, x):
  while (left <= right):
    mid = left + (right - left) // 2

    if array[mid] == x:
      return mid
    
    elif array[mid] < x:
      left = mid + 1
    
    else:
      right = mid - 1
  
  return -1


if __name__ == '__main__':
  array = [2, 3, 4, 10, 40]
  x = 10

  result = binary_search(array, 0, len(array) - 1, x)

  if result != -1:
    print("Element is present at index", result)
  else:
    print("Element is not present in array")