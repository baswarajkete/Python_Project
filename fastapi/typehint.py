str = "ram"
print(type(str))

def addition(a:int, b:int) -> int:
    return a+b
print(addition(3,7))
print(addition('3','4'))
print(addition('3a','4'))

def rev_fun(param: list):
    return param.reverse()