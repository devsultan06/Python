def linear(array, num):
    while True:
        for i in range(len(array)+ 1):
            if array[i] == num:
                return "key found at index", i
        break
    return "key not found"
            
print(linear([1, 2, 3, 4, 5], 5)) # 2