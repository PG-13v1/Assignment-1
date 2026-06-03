# Assignment 1 – Python, FastAPI, Testing & CI

## Overview

This repository contains solutions for the following tasks:

| Task     | Description                                                           |
| -------- | --------------------------------------------------------------------- |
| Task 1.1 | Python environment setup, packaging, dependency management, Makefile  |
| Task 1.2 | OOP refactoring, type annotations, dataclasses, abstract base classes |
| Task 1.3 | FastAPI application with versioned APIs                               |
| Task 1.4 | JWT authentication and rate limiting                                  |
| Task 1.5 | Testing, coverage, and GitHub Actions CI                              |

Repository structure:



> Note:
>
> * Task 1.1 and Task 1.2 are implemented in separate folders called environment_replicate and OOPS_design.
> * Tasks 1.3, 1.4, and 1.5 are implemented together inside the `fastapi_modules` folder.

---

# Prerequisites

* Python 3.11+
* pip
* Git


# Task 1.1 – Environment Setup and Packaging

## Navigate to Task 1.1

```bash
cd environment_replicate
```


## Available Make Commands

```bash
make install
make lint
make test
make run
```

### Environment Recreation

```bash
make install
```


# Task 1.2 – OOP Refactoring and Typing

## Navigate to Task 1.2

```bash
cd OOPS_design
```

## Install Dependencies


```bash
python -m venv venv
./venv/Scripts/activate
```

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python main.py
```

## Type Checking

```bash
mypy --strict .
```

Expected result:

```text
Success: no issues found
```

## Acceptance Criteria Verification

Must produce zero errors.

All classes should contain docstrings.

---

# Tasks 1.3, 1.4 and 1.5 – FastAPI Application

## Navigate to FastAPI Project

```bash
cd fastapi_modules
```

## Create Virtual Environment

```bash
python -m venv venv
./venv/Scripts/activate
```

Activate environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Start API Server

```bash
fastapi dev main.py
```

Application:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Task 1.3 Verification

### Exploring and Testing the API Using Swagger UI

Swagger UI provides an interactive interface for exploring and testing all available API endpoints.

1. Open Swagger UI by navigating to `http://localhost:8000/docs`.
2. Browse the available endpoints grouped by their respective categories.
3. Select any endpoint to view:

   * Request parameters
   * Request body schema
   * Response models
   * Status codes and example responses
4. Click **Try it out** to provide input values and execute requests directly from the browser.
5. Review the generated request payload and inspect the returned response, including headers, status codes, and response body.
6. For protected endpoints, first authenticate using the **Authorize** feature before executing requests.

Swagger UI serves as both the API documentation and a testing interface, making it easy to verify endpoint behavior and validate request/response formats.

Verify:

* All routes visible
* Request schemas visible
* Response schemas visible

---

# Task 1.4 Verification

## Generate JWT Token

Authentication via Swagger UI

The API is protected using JWT-based authentication.

Open the Swagger UI at http://localhost:8000/docs.
Locate the Authorize Endpoint and execute it using the appropriate credentials.
Copy the generated access token from the response.
Click the Authorize button available at the top-right corner of the Swagger UI.
Paste the access token into the authorization field in the format expected by the API (typically Bearer <access_token>).
Click Authorize and then Close.

Once authorized, all protected endpoints can be accessed directly from Swagger UI without manually adding the token to each request.

## Verify Authentication Protection

Without token:

```bash
curl -X POST http://localhost:8000/v1/completions
```

Expected:

```text
401 Unauthorized
```

## Verify Expired Token

Use an expired JWT.

Expected:

```text
401 Unauthorized
```

Response body contains:

```text
token expired
```

## Verify Rate Limiting

Send repeated requests quickly.

Expected:

```text
429 Too Many Requests
```

---

# Task 1.5 Verification

## Run Tests

```bash
pytest
```

## Run Coverage

```bash
pytest --cov=. --cov-report=term
```

Required:

```text
Coverage >= 80%
```


## Verify GitHub Actions

Workflow file:

```text
.github/workflows/tests.yml
```

Push code to GitHub:

```bash
git push
```

Verify:

* Workflow starts automatically
* Tests execute successfully
* CI status is green

---

# Summary of Acceptance Criteria

## Task 1.1

* [ ] Environment recreated using Makefile
* [ ] Valid pyproject.toml
* [ ] .python-version present
* [ ] requirements.txt generated
* [ ] Uses pathlib

## Task 1.2

* [ ] mypy --strict passes
* [ ] Dataclass implemented
* [ ] Abstract base class implemented
* [ ] Full type annotations
* [ ] Class docstrings present

## Task 1.3

* [ ] Async FastAPI endpoints
* [ ] API versioning implemented
* [ ] RFC 7807 compliant errors
* [ ] Swagger docs available

## Task 1.4

* [ ] JWT authentication
* [ ] Token expiry implemented
* [ ] Protected endpoints
* [ ] Rate limiting returns 429

## Task 1.5

* [ ] Coverage > 80%
* [ ] Async tests implemented
* [ ] Mocking implemented
* [ ] GitHub Actions CI passes


  
