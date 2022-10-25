def A_B(a: str, b: str) -> bool:
    split = a.replace("",",").strip(",").split(",")
    for _ in range(len(a)):
        front = split.pop(0)
        split.append(front)
        if "".join(split) == b:
            return True
    return False

a = "amazon"
b = "azonam"

print(A_B(a,b))