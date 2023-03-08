dot = '.'
def comparing_one_with_dot(num_with_dot, num_without_dot):
    temp1 = num_with_dot[0:num_with_dot.find(dot)]
    if len(temp1) > len(num_without_dot):
        return num_with_dot
    elif len(temp1) < len(num_without_dot):
        return num_without_dot
    elif len(temp1) == len(num_without_dot):
        if temp1 != num_without_dot:
            if temp1 == max(temp1, num_without_dot):
                return num_with_dot
            else:
                return num_without_dot
        else:
            return num_with_dot


def comparing(num1, num2):
    if len(num1) > len(num2) and dot not in num1 and dot not in num2:
        return num1
    elif len(num1) < len(num2) and dot not in num1 and dot not in num2:
        return num2
    elif len(num1) == len(num2) and dot not in num1 and dot not in num2:
        return max(num1, num2)
    elif dot in num1 and dot in num2:
        temp1 = num1[0:num1.find(dot)]
        temp2 = num2[0:num2.find(dot)]
        if len(temp1) > len(temp2):
            return num1
        elif len(temp1) < len(temp2):
            return num2
        elif len(temp1) == len(temp2):
            if temp1 != temp2:
                if temp1 == max(temp1, temp2):
                    return num1
                else:
                    return num2
            else:
                temp1 = num1[num1.find(dot) + 1:len(num1)]
                temp2 = num2[num2.find(dot) + 1:len(num2)]
                if temp1 == max(temp1, temp2):
                    return num1
                else:
                    return num2
    elif dot in num1:
        return comparing_one_with_dot(num1, num2)
    elif dot in num2:
        return comparing_one_with_dot(num2, num1)


n = input()
check = True
while check:
    string = input()
    num_array = string.split()
    if str(len(num_array)) == n:
        check = False
    else:
        print('Введите верное количество чисел')
maximum = comparing(num_array[0], num_array[1])
for i in range(2, len(num_array)):
    maximum = comparing(maximum, num_array[i])
print(maximum)
