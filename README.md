# 🤖 CareerMate

### AI-Powered Career Discovery & Guidance System

## Overview

CareerMate is an AI-powered career discovery and guidance system built with Python.

It helps students and fresh graduates explore suitable career paths based on their **major, experience, skills, and interests**.

Python handles the application logic, data storage, and authentication, while **Ollama and Gemma 3** provide AI-powered career analysis, job title recommendations, and interview questions.

![CareerMate](/CareerMate Roadmap.png)

---

## Features

* 🔐 Create an account and log in securely
* 👤 Create and view a career profile
* 🤖 Get AI-powered career analysis
* 💼 Get five suitable job title suggestions
* 🎤 Generate interview questions for a specific job title
* 🚪 Log out of the account

---

## User Inputs

The user provides:

* **Email**
* **Password**
* **Name**
* **Major**
* **Experience**
* **Skills**
* **Interests**

Example:

```text
Name: Reema
Major: Computer Science
Experience: Fresh Graduate
Skills: Python, SQL, Git, HTML, CSS
Interests: Web Development, AI, Data
```

The user's **major, experience, skills, and interests** are used as inputs for the AI career analysis and job title recommendations.

---

## Usage

Run the application:

```bash
python3 main.py
```

The main menu will appear:

```text
==================================================
              🤖 CareerMate
   AI-Powered Career Discovery System
==================================================

1. 🔐 Login
2. 📝 Create Account
3. ❌ Exit
```

After logging in:

```text
========================================
              👩 MY CAREER
========================================

1. 👤 My Profile
2. 🤖 Career Analysis
3. 💼 Suitable Job Titles
4. 🎤 Interview Preparation
5. 🚪 Logout
```

---

## AI Features

### 🤖 Career Analysis

Provides:

* Suitable career paths
* Skills to improve
* A practical next step

### 💼 Suitable Job Titles

Generates five job titles based on the user's profile.

### 🎤 Interview Preparation

Generates five interview questions based on the selected job title and the user's experience level.

---

## Project Structure

```text
CareerMate/
│
├── main.py
├── ai.py
├── profile.py
├── storage.py
├── requirements.txt
├── README.md
│
├── careermate.png
│
└── data/
    └── candidates.json
```

---

## Technologies

* Python
* Ollama
* Gemma 3
* JSON
* hashlib
* getpass

---

## How to Run

### 1. Install Python packages

```bash
pip install -r requirements.txt
```

### 2. Run Gemma 3 with Ollama

```bash
ollama run gemma3
```

### 3. Run CareerMate

```bash
python3 main.py
```

---

## Requirements

Before submitting the project, update the requirements file:

```bash
pip freeze > requirements.txt
```

This records the Python packages used by the project.
