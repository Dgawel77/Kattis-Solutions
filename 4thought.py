def solve(equation):
    if len(equation) == 7:
        if float(eval(equation)).is_integer() and eval(equation) >= 0:
            result[int(eval(equation))] = equation
        return
    for operand in ("+","-","*","/"):
        solve(equation + operand + "4")

result = {}
solve("4")
while(True):
    want = input()
    if want == "":
        break 
    try:
        print(result[int(want)] + " = " + str(want))
    except:
        print("no solution")