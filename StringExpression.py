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

def stringExpression(s):
    opr=""
    nums=""
    for i in s:
        opr+=i
        # print("before if : ", opr)
        if opr in obj.keys():
            nums+=str(obj[opr])
            opr=""               # opr1 = e, opr2 = ei, opr3 = eig, opr4 = eigh, opr5 = eight, 
        # else:
        #     opr += i             # 

        # print("after if : ", opr)

    # print("OPR : ", eval(nums))
    res = str(eval(nums))
    nums=""
    for i in res:
        if i == '-':
            nums += "negative" #list(obj.keys())[list(obj.values()).index(i)]
        else:
            nums+= list(obj.keys())[list(obj.values()).index(int(i))]
    
    print(nums)


        




stringExpression("zerominuszero")
