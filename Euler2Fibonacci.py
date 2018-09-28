def fibonacci():
    add_on = 0
    result = 0
    i = 1
    while i <= 4000000:
        temp = i
        i += add_on
        add_on = temp
        if i%2 == 0:
            result += i
    return result
        
print(fibonacci())
