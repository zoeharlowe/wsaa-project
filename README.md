# wsaa-project
by Zoe McNamara Harlowe

# Irish Vocabulary Web Application

### Welcome to my project submission for the Web Services and Applications module. This module is provided by ATU (Atlantic Technological University) as part of the HDip in Computing in Data Analytics.

For this project, I created a simple Flask web application for storing, managing, and testing Irish–English vocabulary.  
Users can add, edit, delete, search, and quiz themselves on random Irish words.  
Built with Flask, SQLite, Bootstrap, and JavaScript.

---

## Features

### Browse & Add Words
- View all Irish–English word pairs stored in the database.
- Clean, searchable layout for quick reference.
- Add or update words in Irish and English, as well as their synonyms.

### Test Yourself
- Randomly generated quiz questions.
- Accepts multiple correct English translations.
- Normalises user input (case, punctuation, spacing).
- Saves every quiz attempt to the database for later analysis.

### Stats Page
- Displays total quiz attempts and number of correct answers.
- Shows your most-missed words to guide revision.
- Lists your 10 most recent attempts with timestamps.
- Automatically shows a “No data yet” message for new users.
- Powered by a dedicated `/stats_data` JSON API endpoint.

---

## Project Structure

wsaa_project/
- app.py               
- words.html           
- test.html
- stats.html            
- words.db             
- createdb.py          
- requirements.txt     
- README.md            

---

## Accessing the Web Application
The site is currently live at:
```bash
https://zoeharlowe.pythonanywhere.com/
```

I deployed it to PythonAnywhere using the following steps:

### 1. Create an account and create new Web App called wsaa_project.
Upload project files to: /home/zoeharlowe/wsaa_project

### 2. Ensure WSGI configuration is as follows:
```bash
import sys
import os

path = '/home/zoeharlowe/wsaa_project'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from app import app as application
```
### 3. Reload web app
The site will be live at [zoeharlowe.pythonanywhere.com](https://zoeharlowe.pythonanywhere.com/)

---

## Running Locally

### 1. Clone the repository and change directory to the repo
```bash
git clone https://github.com/zoeharlowe/wsaa_project.git
cd wsaa_project
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create the database
```
python createdb.py
```
### 4. Run the Flask app
```bash
python app.py
```
### 5. Open in browser
```bash
http://127.0.0.1:5000/
```
---

## Technologies Used
- **Flask** — backend framework
- **SQLite** — lightweight relational database
- **HTML/CSS/Bootstrap** — frontend layout
- **JavaScript** — quiz logic and stats fetching
- **PythonAnywhere** — deployment platform

---

## Libraries & Packages
- flask: https://flask.palletsprojects.com/en/stable/quickstart/
- sqlite3: https://docs.python.org/3/library/sqlite3.html
- os: https://docs.python.org/3/library/os.html
- random: https://docs.python.org/3/library/random.html

---

## Bibliography
- I used Copilot primarily to help me develop the frontend of this webapp as well as the 'test yourself' feature and 'your stats' page. See conversations with Copilot: https://copilot.microsoft.com/shares/5d82dokXWCe5WZnnZdMcj, https://copilot.microsoft.com/shares/nGVnTN9Tnyx7wD67YsvNH, https://copilot.microsoft.com/shares/mDGYheR9CPi9PYQgUDo3q
- I used the Web Services and Applications module video lectures (by Andrew Beatty) to write the HTML/Flask with CRUD operations. Also followed the lecturer's guidance to deploy the webapp to Python Anywhere. 
- GeeksForGeeks helped with creating a SQLite database: https://www.geeksforgeeks.org/python/python-sqlite-creating-a-new-database/

---

### Author
Zoe McNamara Harlowe

G00473469

Higher Diploma in Computing in Data Analytics

Atlantic Technological University (ATU)