from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str = "Ram"

# Optional and non-nullable 
# what happens when value is not provided in dict 
value = {
    "product_id" : "50"
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")


print("second one -------------------------")

value = {
    "product_id" : "50",
    "name": None
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")


print("third one -------------------------")
from pydantic import BaseModel, ValidationError 

class Product(BaseModel):
    product_id: int
    name: str | None = None

# Optional and nullable 
# what happens if value is None
value = {
    "product_id" : "50",
    
}

try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']}  , Type : {err['type']} ,  Message: {err['msg']}")

print("fifth one -------------------------")

class Product(BaseModel):
    product_id: int = "abc"

p = Product()
print(p)



# Question for students 

# Create an ExperimentRun(BaseModel) for an ML training tracker with:
# experiment_name: str (required, non-nullable)
# parent_run_id: str | None (required key, can be None)
# learning_rate: float = 0.001 (optional, non-nullable)
# run_id: UUID (auto-generated fresh UUID per instance via default_factory)
# metrics: dict[str, float] (defaults to a fresh empty dict {} via default_factory)
# Test creating 2 separate runs and verify run1.run_id != run2.run_id!

from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class ExperimentRun(BaseModel):

    experiment_name: str

    parent_run_id: str | None

    learning_rate: float = 0.001

    run_id: UUID = Field(default_factory=uuid4)

    metrics: dict[str, float] = Field(default_factory=dict)

run1 = ExperimentRun(
    experiment_name="Linear Regression",
    parent_run_id=None
)

run2 = ExperimentRun(
    experiment_name="Logistic Regression",
    learning_rate = 0.02,
    parent_run_id="RUN1"
)

print(run1)
print(run2)

print(run1.run_id != run2.run_id)