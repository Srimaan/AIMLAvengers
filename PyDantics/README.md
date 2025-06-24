# 🐍 Pydantic Tutorial with Examples

This tutorial provides a comprehensive guide to Pydantic, covering beginner to advanced topics with clear examples.

---

## 📚 Index

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

---

## 🚀 Getting Started

Install Pydantic with:

```bash
pip install pydantic
```

---

## ✅ Highlights

### 1. Basic Model

```python
class User(BaseModel):
    id: int
    name: str
    email: str
```

### 4. Custom Validator

```python
@validator('username')
def no_spaces(cls, value):
    if ' ' in value:
        raise ValueError("Username must not contain spaces")
    return value
```

### 5. Root Validator

```python
@root_validator
def check_passwords_match(cls, values):
    if values.get('password') != values.get('confirm_password'):
        raise ValueError("Passwords do not match")
    return values
```

### 6. Each Item Validator

```python
@validator('tags', each_item=True)
def clean_tags(cls, value):
    return value.strip().lower()
```

### 7. Nested Models

```python
class Address(BaseModel):
    city: str

class Employee(BaseModel):
    name: str
    address: Address
```

---

## ⚙️ FastAPI Integration

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
async def create_user(user: User):
    return user
```

---

## 💡 Best Practices

- Use `Field` for type constraints
- Use `@validator` and `@root_validator` for custom validation
- Use nested models for complex data
- Use `Config` to control behavior like immutability or extra fields

---

## 📦 Exporting

```python
user.dict()
user.json()
```

---

## 🔗 Reference

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
