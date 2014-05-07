def karatsuba(x, y):

    x_len = len(x)
    y_len = len(y)

    if max(x_len, y_len) <= 2: 
        return int(x) * int(y)
    
    x_mid = x_len // 2
    x_left, x_right = x[:x_mid], x[x_mid:]

    y_mid = y_len // 2
    y_left, y_right = y[:y_mid], y[y_mid:]

    p_1 = str(karatsuba(x_left, y_left))
    p_2 = str(karatsuba(x_right, y_right))

#    print(x_left, x_right)
#    print(y_left, y_right)
    a_1 = add(x_left, x_right)
    a_2 = add(y_left, y_right)
    p_3 = str(karatsuba(a_1, a_2))
    s_1 = sub(p_3, p_1)
    s_2 = sub(s_1, p_2)
    temp = add(add_zeroes(p_1, 2), add_zeroes(s_2, 1))
    temp = add(temp, p_3)
    return temp

def add_zeroes(x, count):
    return x + '0'*count

def sub(x, y):
    x_r = x[::-1]
    y_r = y[::-1]

    x_len = len(x)
    y_len = len(y)
    c = False
    out = ''

    for i in range(0, max(x_len, y_len)):
        x_cur = int(x_r[i]) if i < x_len else 0
        y_cur = int(y_r[i]) if i < y_len else 0

        if c:
            if x_cur > 0:
                x_cur -= 1
                c = False
            else:
                x_cur = 9

        if x_cur < y_cur:
            x_cur += 10
            c = True

        out += str(x_cur-y_cur)
    
    return out[::-1]

def add(x, y):
    x_r = x[::-1]
    y_r = y[::-1]
    x_len = len(x)
    y_len = len(y)
    out = ''
    c = False

    for i in range(0, max(x_len, y_len)):
        if i > x_len - 1:
            temp = int(y_r[i])
        elif i > y_len - 1:
            temp = int(x_r[i])
        else:
            temp = int(x_r[i]) + int(y_r[i])

        if c:
            temp += 1
            c = False

        if temp >= 10:
            temp = temp % 10
            c = True

        out += str(temp)

    if c:
        out += '1'

    return out[::-1]

if __name__ == "__main__":
    '''    
    x = input()
    y = input()
    result = karatsuba(x, y)
    '''
    x = '23903023903056617'
    y = '56617956617923930'

    result = karatsuba(x, y)

    print(result)
