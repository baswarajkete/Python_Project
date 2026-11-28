##Pydantic
##before pydantic
class Student:
    def __init__(self,name: str,age: int,gpa:float):
        self.name = name
        self.age = age
        self.gpa = gpa
s = Student("Ram",'Twenty',10)
print(s.name, s.age, s.gpa)

#----------------------------------------------------------------------------------------
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class Student(BaseModel):
    #def __init__(self,name: str,age: int,gpa:float):
        name: str
        age: int
        gpa: float

        #model_config = {"strict": True}

s = Student(name="Ram",age=23,gpa=10) 
print(s.name)
print(s.age)

row_data = {
    "name": "Ram",
    "age": '23',
    "gpa": 10
}
s3 = Student(**row_data)
print(type(s3.name), type(s3.age), type(s3.gpa))

#----------------------------------------------------------------------------
#ValidationError
from pydantic import BaseModel, ValidationError

raw_data = {
    "name": "Ram",
    "age": '23',
    "gpa": 10
}

try:
     s4= Student(**raw_data)
     print(s4)
except ValidationError as e:
     print(f"Total validation errors: {e.error_count()}")
     for err in e.errors():
          print(f"Fields: {err['loc']} , Type: {err['type']} , Message: {err['msg']}")

#----------------------------------------------------------------------------------
"""Question
Try writing a small Product(BaseModel) in your notebook with fields: 
product_id: int, name: str, price: float, in_stock: bool, 
and test it with:

Valid coerced inputs (product_id="50", price="199.99", in_stock="1").
A broken input inside try / except ValidationError as e: and print e.error_count().
"""
from pydantic import BaseModel, ValidationError
class Product(BaseModel):
    product_id: int
    name: str
    price: float
    in_stock: bool

row_data = {
    "product_id": "50",
    "price": "199.99",
    "in_stock": "9"
}

try:
     p1 = Product(**row_data)
     print(p1)
except ValidationError as e:
     print(f"Total numbers of erros found: {e.error_count()}")
     print(f"Errors are: {e.errors()}")

#-----------------------------------------------------------------------------------
from pydantic import BaseModel, ValidationError
#Case 1: Optional and non-nullable
class Product(BaseModel):
    product_id: int
    name: str = "Ram"

row_data = {
    "product_id": "50"
}
try:
     p1 = Product(**row_data)
     print(p1)
except ValidationError as e:
     print(f"Total numbers of erros found: {e.error_count()}")
     print(f"Errors are: {e.errors()}")

#Case 2: Optional and nullable
class Product(BaseModel):
    product_id: int
    name: str | None = None

row_data = {
    "product_id": "50"
}
try:
     p1 = Product(**row_data)
     print(p1)
except ValidationError as e:
     print(f"Total numbers of erros found: {e.error_count()}")
     print(f"Errors are: {e.errors()}")

#Case 3: Non-optional and non-nullable
class Product(BaseModel):   
    product_id: int
    name: str       
row_data = {
    "product_id": "50" 
}
try:
     p1 = Product(**row_data)
     print(p1) 
except ValidationError as e:
     print(f"Total numbers of erros found: {e.error_count()}")
     print(f"Errors are: {e.errors()}")

#Case 4: Non-optional and nullable
class Product(BaseModel):   
    product_id: int
    name: str | None   
row_data = {
    "product_id": "50" ,
    "name": None
}
try:
     p1 = Product(**row_data)
     print(p1)
except ValidationError as e:
     print(f"Total numbers of erros found: {e.error_count()}")
     print(f"Errors are: {e.errors()}")

#Case 5: Non-optional and non-nullable with default value
class Product(BaseModel):
    product_id: int
    name: str = "Ram"
row_data = {
    "product_id": "50",
    "name": "Shyam"
}
try:
     p1 = Product(**row_data)
     print(p1) 
except ValidationError as e:
     print(f"Total numbers of erros found: {e.error_count()}")
     print(f"Errors are: {e.errors()}")

## pydantic does not validate default value by itself.
class Product(BaseModel):
    product_id: int = 'Ram'

p = Product(product_id='55')
print(p)

#=------------------------------------------------------------------------------
from pydantic import validate_call

@validate_call
def addition(a: int, b: int) -> int:
    return a + b
     

print(addition(10, 20))
print(addition("10", "20"))

#---------------------------------------------------------------------------------
from pydantic import validate_call, ConfigDict

@validate_call(config=ConfigDict(strict=True))
def addition(a: int, b: int) -> int:
    return a + b
print(addition(10, 20))
#print(addition("10", "20")) # will raise ValidationError
#----------------------------------------------------------------------------------

from pydantic import TypeAdapter

adapter = TypeAdapter(list[int])

data = adapter.validate_python([1, 2, 3])

print(data)
'''
Quick comparison
Approach	Purpose
BaseModel	Validate structured data using classes
TypeAdapter	Validate individual types, lists and dictionaries
@validate_call	Validate function arguments and return values
'''
#-------------------------------------------------------------------------------------------
from datetime import datetime, UTC
import time
class Badexample(BaseModel):
     createdat: datetime = datetime.now(UTC)

b1 = Badexample()
time.sleep(2)
b2 = Badexample()

print(b1)
print(b2)
#--------------------------------------------------------------------------
from uuid import UUID, uuid4
import time
class Goodexample(BaseModel):
     request_id: UUID = Field(default_factory=uuid4)
     created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

g1 = Goodexample()
time.sleep(2)
g2 = Goodexample()
print(g1)
print(g2)
print(g1.created_at == g2.created_at) # always false
#------------------------------------------------------------------------------------------
from pydantic import BaseModel,Field 
from uuid import UUID, uuid4
from datetime import datetime,UTC

class LLMChatRequest(BaseModel):
    # Required
    prompt: str

    # Optional with sensible production defaults
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int | None = None          # None = let provider use model default
    system_prompt: str | None = None       # Optional system instruction
    stop_sequences: list[int] = Field(default_factory=list)

    # Auto-generated metadata per request
    trace_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
req = LLMChatRequest(prompt="Explain RAG in 2 sentences.", stop_sequences=[1,'2',3])
#req = LLMChatRequest(prompt="Explain RAG in 2 sentences.", stop_sequences=[1,'hi',3])
print(req)

req.stop_sequences.append('hi')
req.stop_sequences=['hi']

print(req)
'''Interview takeaway: Pydantic validates data at model creation and can 
validate attribute assignment, but it does not automatically 
intercept in-place mutations of mutable objects such as lists and dictionaries.'''
#to avoid this, you can use immutable types (like tuples) or create new instances of mutable objects instead of modifying them in place.
class LLMChatRequest(BaseModel):
    # Required
    prompt: str
    model_config = ConfigDict(validate_assignment=True)
    # Optional with sensible production defaults
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int | None = None          # None = let provider use model default
    system_prompt: str | None = None       # Optional system instruction
    stop_sequences: list[int] = Field(default_factory=list)

    # Auto-generated metadata per request
    trace_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))



#req = LLMChatRequest(prompt="Explain RAG in 2 sentences.", stop_sequences=[1,'2',3])
req = LLMChatRequest(prompt="Explain RAG in 2 sentences.", stop_sequences=[1,'2',3])
print(req)

#req.stop_sequences = ['hi'] # this wont allow, because validate_assignment is True and 'hi' is not an int

print(req)
print('-'*50)
#------------------------------------------------------------------------------------------

class Prompt(BaseModel):
    text: str = Field(description="User text value")
    user_id: str = Field(...,description="Caller user id")
    value: str | None = Field(default=None, description="randome value")

print(Prompt(text="abc",user_id="pqr"))
print('-'*50)
#------------------------------------------------------------------------------------------
# How to validate default value
class validatedefault(BaseModel):
    product_id: int = Field(default = "abc", validate_default=True)

try:
     p = validatedefault()
     print(p)
except ValidationError as e:
     print(e.errors()[0]['msg'])

print('-'*50)   
#------------------------------------------------------------------------------------------
# Dynamic data assign
class ModelData(BaseModel):
     model_name : str
     version: int = 1
     attribute_val: str = Field(default_factory=lambda data: f"{data['model_name']} : {data['version']}")

a = ModelData(model_name="gpt", version=2)
print(a)
#------------------------------------------------------------------------------------------
print('-'*50)


# Question for students 
"""
Create an ExperimentRun(BaseModel) for an ML training tracker with:

experiment_name: str (required, non-nullable)
parent_run_id: str | None (required key, can be None)
learning_rate: float = 0.001 (optional, non-nullable)
run_id: UUID (auto-generated fresh UUID per instance via default_factory)
metrics: dict[str, float] (defaults to a fresh empty dict {} via default_factory)

Test creating 2 separate runs and verify run1.run_id != run2.run_id!
"""
class ExperientRun(BaseModel):
     experient_name: str
     paraent_run_id: str | None
     learning_rate: float = 0.001
     run_id: UUID = Field(default_factory=uuid4)
     metrics: dict[str, float] = Field(default_factory=dict)

r1 = ExperientRun(experient_name="Experiment 1", paraent_run_id=None)
r2 = ExperientRun(experient_name="Experiment 2", paraent_run_id=None)
print(r1)
print(r2)
print(r1.run_id != r2.run_id)
#------------------------------------------------------------------------------------------
#Numeric constraints
from pydantic import BaseModel, Field, ValidationError

class Trainingdetails(BaseModel):
     id: int = Field(gt=0, lt=1000)
     batch_size: int = Field(gt=0,multiple_of=2)
     learning_rate: float = Field(gt=0.0, lt =1.0, allow_inf_nan=False)
     fees: Decimal = Field(max_digits=7, decimal_places=2)
s1= Trainingdetails(id=10, batch_size=32, learning_rate=0.01, fees=13499.99)
print(s1)

try:
     s2= Trainingdetails(id=1001, batch_size=33, learning_rate=0.01, fees=133499.99)
     print(s2)
except ValidationError as e:
     print(f"Total numbers of errors found: {e.error_count()}")
     for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")
print('-'*50)
#-------------------------------------------------------------------------------------
# String Contraints 
from typing import Annotated
from pydantic import BaseModel, Field, ValidationError, StringConstraints

clean_data = Annotated[str, StringConstraints(strip_whitespace=True,min_length=1)]
RollidConstraints = Annotated[str, StringConstraints(strip_whitespace=True, to_upper=True, pattern = "^[A-Za-z]{2,5}-[0-9]{5}$")]

class Student(BaseModel):
     name: clean_data
     roll_id: RollidConstraints
     email: Annotated[str, StringConstraints(strip_whitespace=True, to_lower=True, pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")]

s1 = Student(name="  Ram  ", roll_id="abc-12345", email="baswaraj@example.com")
print(s1)

try:
     s2 = Student(name="  ", roll_id="abc-1234", email="baswarajexample.com")
     print(s2)
except ValidationError as e:
     print(f"Total numbers of errors found: {e.error_count()}")
     for err in e.errors():
        print(f"Fields: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")
#-------------------------------------------------------------------------------------
print('-'*50)

#List and Dict constraints
from typing import Annotated
from pydantic import BaseModel, Field, ValidationError, PositiveInt

ProbVal = Annotated[float, Field(gt=0.0,lt=1.0,allow_inf_nan=False)]

class NewClass(BaseModel):
     request_id: PositiveInt
     class_prob: list[ProbVal] = Field(min_length=2, max_length=10)
     embadding: list[ProbVal] = Field(min_length=3,max_length=6, repr=False)


p = NewClass(request_id=101,class_prob=[0.1,0.2], embadding=[0.3,0.6,0.4])
print(p)

try:
    p2 = NewClass(request_id=101,class_prob=[1.1,0.2], embadding=[0.6,0.4])
except ValidationError as e:
     print(f"Total numbers of errors found: {e.error_count()}")
     for err in e.errors():
          print(f"Field: {err['loc']}, Type: {err['type']}, Message: {err['msg']}")

print('-'*50)
#--------------------------------------------------------------------------------------
#Strict and frozen

from pydantic import BaseModel, Field, ValidationError

class Strict_user(BaseModel):
     user_id: int=Field(strict=True)
     emp_id: int=Field(frozen=True)

p1 = Strict_user(user_id=10, emp_id=10)
p2 = Strict_user(user_id=20, emp_id=20)
print(p1)
print(p2)
