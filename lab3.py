def array_diff(a, b):
    result = []
    for elem in a:
     if elem not in b:
      result.append(elem)
    return result
    
a = [1, 2,  2, 3]
b = [2]
print(array_diff(a, b))