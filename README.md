# Voting System Microservices

This repository contains two independent microservices forming a voting platform backend:

- **User Service** – Manages users and their registration status.  
- **Answer Service** – Handles voting logic, answers, and vote tallies.

---

## Table of Contents

- [Architecture](#architecture)  
- [User Service](#user-service)  
- [Answer Service](#answer-service)  
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

| Method | Endpoint            | Description                      |
|--------|---------------------|--------------------------------|
| POST   | `/users/`           | Create a new user               |
| GET    | `/users/{user_id}`  | Retrieve user by ID             |
| PUT    | `/users/{user_id}`  | Update user info                |
| PUT    | `/users/{user_id}/register` | Register a user          |

**Validation Logic:**  
- Prevent creation of duplicate users by ID.  
- Only registered users are allowed to vote.

---

## Answer Service

**Responsibilities:**  
- Manage votes (create, update, delete).  
- Aggregate votes per option/question/user.  
- Enforce voting rules (one vote per question per user).  
- Return vote summaries and counts.

**Key Endpoints:**

| Method | Endpoint                 | Description                          |
|--------|--------------------------|------------------------------------|
| POST   | `/answers/`              | Create a new vote                   |
| GET    | `/answers/{answer_id}`   | Retrieve a vote by ID               |
| PUT    | `/answers/{answer_id}`   | Update an existing vote             |
| DELETE | `/answers/{answer_id}`   | Delete a specific vote              |
| GET    | `/answers/{option_id}/option_votes` | Count votes for an option |
| GET    | `/answers/{question_id}/most_voted` | Get most voted option for question |
| GET    | `/answers/{user_id}/user_votes_count` | Count votes by a user          |
| DELETE | `/answers/{user_id}/user_votes` | Delete all votes by user       |

**Validation Logic:**  
- Confirm user existence and registration before voting.  
- Validate that option voted on belongs to the question.  
- Prevent multiple votes by same user on one question.

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
