'''
Input: a List of integers
Returns: a List of integers
'''
# find the zeros *** use for loop if x = 0 then pop() then append()

def moving_zeroes(arr):
    # Your code here
    new_arr = [0]*len(arr)
    count = -1
    for i in range(len(arr))[::1]:
        if arr[i] != 0:
            count += 1
            value = arr[i]
            new_arr[count]=value
    return new_arr
        
    # for item in arr:
    #     if item != 0:
    #         arr.remove(item)
    #         arr.insert(0, item)

    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")