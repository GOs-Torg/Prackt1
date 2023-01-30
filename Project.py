def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

isGoing = True
result = None
while isGoing :
    if result == None:
        mathString = input("Введите простое выражение (пример: 1+1)\n")
        if mathString != "":
            if find_str(mathString, "-") >= 0:
                first = float(mathString[:find_str(mathString, "-")])
                second = float(mathString[find_str(mathString, "-")+1:])
                print(f"{first} - {second} = {first - second}")
                result = first - second
            elif find_str(mathString, "+") >= 0:
                first = float(mathString[:find_str(mathString, "+")])
                second = float(mathString[find_str(mathString, "+")+1:])
                print(f"{first} + {second} = {first + second}")
                result = first + second
            elif find_str(mathString, "**") >= 0:
                first = float(mathString[:find_str(mathString, "**")])
                second = float(mathString[find_str(mathString, "**")+2:])
                print(f"{first} ^ {second} = {first ** second}")
                result = first ** second
            elif find_str(mathString, "*") >= 0:
                first = float(mathString[:find_str(mathString, "*")])
                second = float(mathString[find_str(mathString, "*")+1:])
                print(f"{first} * {second} = {first * second}")
                result = first * second
            elif find_str(mathString, "/") >= 0:
                first = float(mathString[:find_str(mathString, "/")])
                second = float(mathString[find_str(mathString, "/")+1:])
                if(second != 0):
                    print(f"{first} / {second} = {first / second}")
                    result = first / second
                else:
                    print("Error")
        else:
            isGoing = False
    else:
        mathString = input(f"Введите простое выражение (пример: 1+1)\n {result}")
        if find_str(mathString, "-") >= 0:
            second = float(mathString[find_str(mathString, "-")+1:])
            print(f"{result} - {second} = {result - second}")
            result = result - second
        elif find_str(mathString, "+") >= 0:
            second = float(mathString[find_str(mathString, "+")+1:])
            print(f"{result} + {second} = {result + second}")
            result = result + second
        elif find_str(mathString, "**") >= 0:
            second = float(mathString[find_str(mathString, "**")+2:])
            print(f"{result} ^ {second} = {result ** second}")
            result = result ** second
        elif find_str(mathString, "*") >= 0:
            second = float(mathString[find_str(mathString, "*")+1:])
            print(f"{result} * {second} = {result * second}")
            result = result * second
        elif find_str(mathString, "/") >= 0:
            second = float(mathString[find_str(mathString, "/")+1:])
            if(second != 0):
                print(f"{result} / {second} = {result / second}")
                result = result / second
            else:
                print("Error")
        else:
            isGoing = False
