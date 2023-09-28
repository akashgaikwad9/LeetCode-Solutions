# Input:"onezeropluseight"
# Output: oneeight

obj = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
        "plus": "+",
        "minus": "-"
    }

def stringCn(res, req):
    if req == "value":
        if res in obj.keys():
            return obj[res]
    elif req == "key":
        if res in obj.values():
            return list(obj.keys())[list(obj.values()).index(res)]
    return -1
        
def stringExpression(s):
    opr=""
    nums=""
    for i in s:
        opr+=i
        result = stringCn(opr, "value")
        # print("opr :: ", opr, "####", result)
        if result != -1:
            nums += str(result)
            opr=""
    
    # print("nums : ", nums)
    res = str(eval(nums))
    nums=""
    for i in res:
        if i == '-':
            nums += "negative" #list(obj.keys())[list(obj.values()).index(i)]
        else:
            result = stringCn(int(i), "key")
            if result != -1:
                nums+= result

    print(nums)

stringExpression("zerominuszero")
