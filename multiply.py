#this function gives the multiply values
def multiply (*a):
    result = 1
    for num in a:
        result  *= num
    return result
