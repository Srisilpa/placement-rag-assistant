def calculate(expr):
    try:
        return str(eval(expr))
    except:
        return "Invalid expression"