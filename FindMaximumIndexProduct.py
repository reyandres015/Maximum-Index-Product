arr = [4,7,2,8,5,1,6]
def solve(arr):
    n = len(arr)
    stack= []
    left_indices = [0] * n
    right_indices = [0] * n

    for i in range(n):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            left_indices[i] = stack[-1] +1 if stack else 0
            stack.append(i)
            
    print(left_indices)



    stack = []

    # Calculate Right(i) for each element
    for i in range(n - 1, -1, -1):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        right_indices[i] = stack[-1] +1 if stack else 0
        stack.append(i)
        
    print(right_indices)

    indexProduct = [x * y for x, y in zip(right_indices,left_indices)]
    print(indexProduct)

    maximumIndexProduct = max(indexProduct)
    return maximumIndexProduct


print(solve(arr))
