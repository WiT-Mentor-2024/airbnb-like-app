# FastAPI Application

## Description

This is a FastAPI application that can be run locally for development and testing purposes.

## Prerequisites

- Python 3.10 or higher
- Virtual environment 

## Installation

Follow these steps to set up your environment and install dependencies:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment

```
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

# For Windows Bash
```
source .venv/Scripts/activate
```

# For macOS/Linux
```
source .venv/bin/activate
```

Every time you install new dependencies activate the environment again.

### 4. Install Dependencies

```
pip install -r requirements.txt
```

### 5. Verify Installation

```
pip list
```

### 6. Start the Server

```
uvicorn main:app --reload
```
or

```
fastapi dev main.py
```

### 7. Open the browser 

http://127.0.0.1:8000

For accessing the docs: 

http://127.0.0.1:8000/docs

### 8. Stopping the Server 

```
CTRL + C
```

### 9. Deactivate the virtual environment

```
deactivate
```

