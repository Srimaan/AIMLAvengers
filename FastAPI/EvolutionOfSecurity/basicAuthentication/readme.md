# 🔐 Basic Username-Password Authentication in FastAPI (In-Memory)

This project demonstrates the evolution of authentication from basic plaintext login to JWT-based token authentication using an in-memory database (Python dictionary).

---

## 🚀 How to Run the App

### 1. Clone or Save the Project

Save your FastAPI file as: `auth_app.py`

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install FastAPI and Uvicorn
```bash 
pip install fastapi uvicorn bcrypt pyjwt
```

### 3. Run the Application
```bash
uvicorn auth_app:app --reload
```

### 5. Open Swagger UI
Open your browser and navigate to:
```http://127.0.0.1:8000/docs
```

## ❌ Disadvantages of Username-Password Authentication (Even with DB)

| #  | 🔍 Problem                               | 📉 Description                                                                 |
|----|------------------------------------------|--------------------------------------------------------------------------------|
| 1  | Passwords stored in plain text           | If the database is compromised, attackers get full credentials.               |
| 2  | No password hashing or salting           | Even if hashed, common algorithms like SHA1 are crackable; without a salt, rainbow table attacks succeed. |
| 3  | Susceptible to brute-force attacks       | Without rate limiting or account lockout, attackers can guess credentials via automated scripts. |
| 4  | No HTTPS → MITM attacks                  | Without TLS, credentials can be intercepted over the network.                 |
| 5  | No MFA/2FA support                       | If the password is stolen, there's no second layer of security.              |
| 6  | Poor password hygiene by users           | Users often reuse weak passwords across multiple systems. A leak from one app can affect others. |
| 7  | No session/token expiration              | Users stay logged in indefinitely unless manually logged out.                |
| 8  | Manual token/session logic needed        | Developers have to implement login/session/token expiration and invalidation manually. |
| 9  | Scalability issues in distributed systems| Sessions stored locally don’t scale across multiple servers or containers.   |
| 10 | Lack of centralized auth (no SSO)        | Each app manages its own user accounts — poor user experience and security.  |
| 11 | Tightly coupled to application logic     | Any change in authentication requires code changes, making refactoring harder. |
| 12 | No standard for identity claims          | Can’t easily share identity between services (unlike JWT/OAuth2).            |
| 13 | No audit logging or tracking             | Hard to track login history, suspicious login attempts, etc.                 |
| 14 | No role-based access control (RBAC)      | Every user is treated the same unless additional logic is added.             |
| 15 | High attack surface for login endpoint   | Login is the most attacked endpoint; without proper protections, it's a major vulnerability. |
