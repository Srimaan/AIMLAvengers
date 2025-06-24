# Pydantic Tutorial with Examples

"""
Index:
1. Basic Model Creation
2. Field Types and Validation
3. Default Values and Optional Fields
4. Custom Field Validators
5. Root Validators
6. Pre-Validators and Each-Item Validators
7. Nested Models
8. List of Sub-Models
9. Aliases and Field Renaming
10. Model Config and Extra Fields Handling
11. Using `parse_obj` and `from_orm`
12. Immutability with `frozen`
13. Complex Data Structures
14. Error Handling and Custom Exceptions
15. Exporting Models (`.dict()`, `.json()`)
16. Integration with FastAPI
17. Advanced Use: Generic Models
18. Tips, Tricks, and Best Practices
19. Summary and Reference Links
"""

from pydantic import BaseModel, Field, validator, root_validator
from typing import List, Optional, Union, Dict, Any, Generic, TypeVar

# 1. Basic Model Creation
class User(BaseModel):
    id: int
    name: str
    email: str

# 2. Field Types and Validation
class Product(BaseModel):
    name: str
    price: float = Field(gt=0, description="Price must be positive")
    in_stock: bool

# 3. Default Values and Optional Fields
class Customer(BaseModel):
    id: int
    name: str = "Guest"
    phone: Optional[str] = None

# 4. Custom Field Validators
class Account(BaseModel):
    username: str

    @validator('username')
    def no_spaces(cls, value):
        if ' ' in value:
            raise ValueError("Username must not contain spaces")
        return value

# 5. Root Validators
class PasswordModel(BaseModel):
    password: str
    confirm_password: str

    @root_validator
    def check_passwords_match(cls, values):
        if values.get('password') != values.get('confirm_password'):
            raise ValueError("Passwords do not match")
        return values

# 6. Pre-Validators and Each-Item Validators
class TagModel(BaseModel):
    tags: List[str]

    @validator('tags', pre=True, each_item=True)
    def strip_and_lowercase(cls, value):
        return value.strip().lower()

# 7. Nested Models
class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class Employee(BaseModel):
    id: int
    name: str
    address: Address

# 8. List of Sub-Models
class Department(BaseModel):
    name: str
    employees: List[Employee]

# 9. Aliases and Field Renaming
class Profile(BaseModel):
    full_name: str = Field(..., alias='fullName')

# 10. Model Config and Extra Fields Handling
class FlexibleModel(BaseModel):
    class Config:
        extra = 'allow'

# 11. Using `parse_obj` and `from_orm`
data = {'id': 1, 'name': 'John', 'email': 'john@example.com'}
user = User.parse_obj(data)

# 12. Immutability with `frozen`
class ConfigModel(BaseModel):
    class Config:
        frozen = True

    key: str
    value: Any

# 13. Complex Data Structures
class Report(BaseModel):
    metadata: Dict[str, Any]
    records: List[Dict[str, Union[int, str]]]

# 14. Error Handling
try:
    Product(name="X", price=-10, in_stock=True)
except Exception as e:
    print("Validation Error:", e)

# 15. Exporting Models
print(user.dict())
print(user.json())

# 16. FastAPI Integration (Example Signature)
# from fastapi import FastAPI
# app = FastAPI()
#
# @app.post("/users")
# async def create_user(user: User):
#     return user

# 17. Generic Models
T = TypeVar('T')
class Wrapper(Generic[T], BaseModel):
    result: T

wrapped_user = Wrapper[User](result=user)

# 18. Best Practices
# - Use `Field` for constraints and descriptions
# - Use `@validator` for field-specific logic
# - Use `@root_validator` for cross-field logic
# - Use `Config` for model-wide behavior

# 19. Summary
# This tutorial covers basic to advanced use cases of Pydantic. Perfect for FastAPI, validation pipelines, and data modeling.