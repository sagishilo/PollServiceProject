# Voting System Microservices

This repository contains two independent microservices forming a voting platform backend:

- **User Service** – Manages users and their registration status.  
- **Poll Service** – Handles voting logic, answers, and vote tallies.

---

## Table of Contents

- [Architecture](#architecture)  
- [User Service](#user-service)  
- [Poll Service](#poll-service)  
- [Common](#common)  
- [Installation](#installation)  
- [Running the Services](#running-the-services)  
- [API Documentation](#api-documentation)  
- [Contribution](#contribution)  
- [License](#license)

---

## Architecture

The system is split into microservices to allow separation of concerns, scalability, and maintainability.  
Each service exposes REST APIs and uses asynchronous Python (FastAPI) for performance.

---

## User Service

**Responsibilities:**  
- Create, update, and retrieve users.  
- Register users (mark as registered).  
- Validate user existence and registration status.

**Key Endpoints:**

| Method | Endpoint                 | Description                      |
|--------|--------------------------|--------------------------------|
| POST   | `/users/`                | Create a new user               |
| GET    | `/users/{user_id}`       | Retrieve user by ID             |
| PUT    | `/users/{user_id}`       | Update user info                |
| PUT    | `/users/{user_id}/register` | Register a user              |

---

## Poll Service

**Responsibilities:**  
- Manage votes (create, update, delete).  
- Aggregate votes per option/question/user.  
- Enforce voting rules (one vote per question per user).  
- Return vote summaries and counts.

**Key Endpoints:**

| Method | Endpoint                                         | Description                                |
|--------|------------------------------------------------|--------------------------------------------|
| POST   | `/answers/`                                     | Create a new vote                         |
| GET    | `/answers/{answer_id}`                          | Retrieve a vote by ID                     |
| PUT    | `/answers/{answer_id}`                          | Update an existing vote                   |
| DELETE | `/answers/{answer_id}`                          | Delete a specific vote                    |
| GET    | `/answers/option/{option_id}/count`             | Count votes for an option                  |
| GET    | `/answers/question/{question_id}/most_voted`    | Get most voted option for question         |
| GET    | `/answers/user/{user_id}/count`                  | Count votes by a user                      |
| DELETE | `/answers/user/{user_id}`                        | Delete all votes by user                   |
| GET    | `/answers/user/{user_id}`                        | Get all votes for a specific user          |
| GET    | `/answers/question/{question_id}/summary`       | Get vote summary for a question            |
| GET    | `/answers/all_questions/summary`                 | Get vote summaries for all questions       |

---

## Question Service (if applicable)

**Responsibilities:**  
- Manage questions and their options.  
- Retrieve questions and associated options.  
- Create, update, and delete questions.

**Key Endpoints:**

| Method | Endpoint                      | Description                          |
|--------|-------------------------------|------------------------------------|
| POST   | `/questions/`                | Create a new question               |
| GET    | `/questions/{question_id}`  | Retrieve a question by ID           |
| GET    | `/questions/`                | Retrieve all questions              |
| PUT    | `/questions/{question_id}`  | Update a question                   |
| DELETE | `/questions/{question_id}`  | Delete a question                   |
| GET    | `/questions/text/`           | Get question by text (query param) |

---

## Option Service (if applicable)

**Responsibilities:**  
- Manage options related to questions.  
- Retrieve, create, update, and delete options.

**Key Endpoints:**

| Method | Endpoint                  | Description                          |
|--------|---------------------------|------------------------------------|
| POST   | `/options/`              | Create a new option                 |
| GET    | `/options/{option_id}`   | Retrieve an option by ID            |
| GET    | `/options/`              | Retrieve all options                |
| PUT    | `/options/{option_id}`   | Update an option                   |
| DELETE | `/options/{option_id}`   | Delete an option                   |
| GET    | `/options/text/`          | Get options by text (query param)  |
| DELETE | `/options/question/{question_id}` | Delete all options for a question |

---

## Common

- Both services communicate asynchronously.  
- The system uses a relational database (e.g., MySQL) for persistence.  
- Services employ structured error handling with clear exception messages.  
- Data models and DTOs (Pydantic models) are used for validation and serialization.

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/voting-microservices.git
cd voting-microservices
pip install -r requirements.txt
