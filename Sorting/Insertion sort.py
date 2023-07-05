def insertionsort(arr):
  length = len(arr)
  end = arr[0]
  for i in range(1, length):
    if arr[i] < end:
      x = arr.pop(i)
      for j in range(0,i):
        if x < arr[j]:
          arr.insert(j,x)
          break
    end = arr[i]
  return arr

arr = [6,5,3,1,8,7,2,4]
print(insertionsort(arr))




