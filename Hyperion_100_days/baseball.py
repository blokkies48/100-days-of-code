ops = ["5","2","C","D","+"]

def baseball(ops):
    return_list = []
    for  char in ops:
        if char.isdigit():
            return_list.append(int(char))
        elif char == "C":
            return_list.pop()
        elif char == "D":
            return_list.append(2*return_list[-1])
        elif char == "+":
            return_list.append(return_list[-2] + return_list[-1])
    return sum(return_list)


print(baseball(ops))