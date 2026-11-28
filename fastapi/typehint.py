#str = "ram"
print(type(str))

def addition(a:int, b:int) -> int:
    return a+b
print(addition(3,7))
print(addition('3','4'))
print(addition('3a','4'))
print('-'*50)

def rev_fun(param: list[str]) -> list[str]:
    param.reverse()
    return param

print(rev_fun(['1','2','3','4','5']))

print('-'*50)

def get_items(item_a: str, item_b: int, item_c: bool, item_d: bytes, item_e: float):
    return item_a, item_b, item_c, item_d, item_e

print(get_items('Ram', 100.999, True, b"a", 'wrong'))

print('-'*50)

from typing import Any

def get_data(data: Any):
    return data
print(get_data('Ram'))
print(get_data(100.00))

def get_items(param: list[str]):
    for i in param:
        print(i)

l1 = [1,2,3,4,5]
l2 = ['1','2','3']

get_items(l1)
get_items(l2)

print('-'*50)

def get_items(param: dict[str, int]):
    for k,v in param.items():
        print(k,'-->', v)

get_items({'Ram': 100, 'Shyam': 200, 'Mohan': 300})

print('-'*50)

def bwt_hi(name: str | None=None):
    if name is not None:
        print("Hello ",name)
    else:
        print("Hello BWT Class...!")

bwt_hi("Ram")
bwt_hi()

print('-'*50)

from typing import Literal

def get_status(name: str, role: Literal["Hr","TA","Head"]):
    return f'{name} --> {role}'

print(get_status('ram','dev'))

print('-'*50)

from enum import Enum

class Role(Enum):
    Hr = 1
    TA = 2
    Head = 3

def get_status(name: str, role: Role):
    return f'{name} --> {role.name} --> {role.value}'

print(get_status('ram', Role.Hr))
print(get_status('shyam', Role.TA))
print(get_status('mohan', Role.Head))

