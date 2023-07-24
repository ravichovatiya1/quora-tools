# Quora-Inspired Website

This is a web application inspired by Quora that allows users to interact with a question and answer platform. The main functionality includes user authentication, posting questions, viewing questions, answering questions, liking answers, and logging out. Below is an `overview` of the `features`:

## Overview
The `Quora-Inspired website` aims to provide a platform where users can ask questions, provide answers, and engage in discussions with other users. The website will have user authentication to ensure that only registered users can access the features. Users will be able to post questions and view questions posted by others. They can also post answers to questions asked by others and like answers provided by other users. Users will have the option to log out when they are done using the website.

## Features
- User Authentication.
- Post Questions.
- View Questions.
- Answer Questions.
- Like Answers.
- Log Out.
- User Profiles.
- Responsive Design.
- User Interactions.

## Prerequisites

- Python version: 3.10.0
- Database: SQLite

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ravichovatiya1/quora-tools

```

2. Create a virtual environment:

```bash
python -m venv venv

```

3. Activate the virtual environment:

- For Windows

```bash
venv\Scripts\activate
```

- For Linux/macOS
```bash
source venv/bin/activate

```

4. Install requirements.txt file


```bash
pip install -r requirements.txt 
```


5. Make Migrations and migrate:

- Use below command to create the migrations file

```bash
python manage.py makemigrations
```

- Use Below command to reflect the changes to database of migrations.
```bash
python manage.py migrate

```

6. Runserver:

```bash
python manage.py runserver 0.0.0.0:8000
```














