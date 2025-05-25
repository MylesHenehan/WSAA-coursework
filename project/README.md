# Web Services and Applications: Big Project
### Author: Myles Henehan

***
# Freelance Linguist Web App  

This is a full-stack web application developed as part of the final project in the Web Services and Applications module. The app allows users to manage a list of freelance linguists: viewing, adding, updating, and deleting linguist records through a user-friendly interface and a Flask-powered REST API.

---

## 🗂 Project Structure

| File | Description |
|------|-------------|
| `server.py` | The main Flask application. It defines the REST API routes and integrates with the DAO and HTML template. |
| `linguistDAO.py` | A Python Data Access Object (DAO) module that handles all interactions with the MySQL database. |
| `linguistfinder.html` | A front-end HTML template that provides a web interface for interacting with the linguist database using AJAX. |

---

## 🔧 Technologies Used

- **Python** & **Flask** – Backend and REST API
- **MySQL** – Database
- **HTML/CSS + Bootstrap** – Front-end styling
- **JavaScript (jQuery)** – AJAX requests and dynamic UI updates
- **PythonAnywhere** – Hosting environment

---

## 🚀 Features

- View all linguists in a styled table
- Create new linguists (auto-increment ID)
- Update existing linguist information
- Delete linguists
- Filter and load individual linguists via API route (`/linguists/<id>`)

---

## 📁 File Details

### `server.py`
- Starts a Flask server
- Serves the front-end HTML on `/`
- Provides RESTful routes for:
  - `GET /linguists` – Get all linguists
  - `GET /linguists/<id>` – Get a linguist by ID
  - `POST /linguists` – Add a new linguist
  - `PUT /linguists/<id>` – Update an existing linguist
  - `DELETE /linguists/<id>` – Delete a linguist
- Communicates with the MySQL database via `linguistDAO.py`

### `linguistDAO.py`
- Contains the `linguistDAO` class
- Connects to a MySQL database using credentials from `dbconfig.py`
- Implements CRUD operations:
  - `getAll()`, `findByID()`, `create()`, `update()`, and `delete()`
- Converts query results into dictionaries for easy JSON conversion

### `linguistfinder.html`
- Web UI for viewing and managing linguists
- Uses jQuery to make AJAX calls to the Flask backend
- Contains form inputs for Name, Email, and Target Locale
- Shows a table of all linguists
- Target locale dropdown includes hardcoded values like `fr-FR`, `es-LA`, `ru-RU`, etc.

---

## ✅ Setup Instructions

1. **Clone the repo / upload files to PythonAnywhere**
2. Ensure your MySQL DB has a `linguists` table with:
   ```sql
   CREATE TABLE linguists (
     LinguistID INT AUTO_INCREMENT PRIMARY KEY,
     LinguistName VARCHAR(100),
     LinguistEmail VARCHAR(100),
     TargetLocale VARCHAR(20)
   );
   ```
3. Add your DB credentials in `dbconfig.py`
4. Install required Python packages:
   ```bash
   pip install flask flask-cors mysql-connector-python
   ```
5. Run your app:
   ```bash
   python server.py
   ```

---

## 🌐 Live Demo

You can view and interact with the project here:  
👉 **[https://myleshenehan.pythonanywhere.com/](https://myleshenehan.pythonanywhere.com/)**

This is hosted on [PythonAnywhere](https://www.pythonanywhere.com/), where the Flask backend and MySQL database are deployed in a live environment.

---

## 👩‍🎓 Author

**Myles Henehan**  
Web Services and Applications  
Atlantic Technological University (ATU)

🔗 Live site: [https://myleshenehan.pythonanywhere.com/](https://myleshenehan.pythonanywhere.com/)


# References:
- Blog.finxter.com, 2023. 5 Best Ways to Convert a Python Tuple into a Dictionary. [online] Available at: https://blog.finxter.com/5-best-ways-to-convert-a-python-tuple-into-a-dictionary/ [Accessed 15 May 2025].
- Bootstrap, 2018. Buttons. [online] Available at: https://getbootstrap.com/docs/4.0/components/buttons/ [Accessed 25 May 2025].
- Bootstrap, 2018. Forms. Available at: https://getbootstrap.com/docs/4.1/components/forms/ (Accessed: 25 May 2025).
- Bootstrap, 2018. Jumbotron. Available at: https://getbootstrap.com/docs/4.0/components/jumbotron/ (Accessed: 25 May 2025).
- Bootstrap, 2018. Tables. [online] Available at: https://getbootstrap.com/docs/4.0/content/tables/ [Accessed 25 May 2025].
- GeeksforGeeks (n.d.) Data Access Object Pattern. [online] Available at: https://www.geeksforgeeks.org/data-access-object-pattern/ [Accessed 14 May 2025].
- Geeksforgeeks.org, 2023. JavaScript const. [online] Available at: https://www.geeksforgeeks.org/javascript-const/ [Accessed 16 May 2025].
- Geeksforgeeks.org, 2023a. Flask Tutorial. [online] Available at: https://www.geeksforgeeks.org/flask-tutorial/ [Accessed 15 May 2025].
- Geeksforgeeks.org, 2023b. JavaScript console.log() Method. [online] Available at: https://www.geeksforgeeks.org/javascript-console-log-method/ [Accessed 17 May 2025].
- MDN Web Docs, 2024. Optional chaining (?.) [online] Mozilla. Available at: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining [Accessed 23 May 2025].
- Medium.com, 2023. How to Deploy a Python App on PythonAnywhere. [online] Available at: https://medium.com/@cssjhnnamae/how-to-deploy-a-python-app-on-pythonanywhere-cf399f4bbc01 [Accessed 19 May 2025].
- OpenAI, 2025. ChatGPT. [online] Available at: https://chat.openai.com/ [Accessed 23 May 2025].
- Planetscale.com, 2023. Using cursors in Python with MySQL. [online] Planetscale. Available at: https://planetscale.com/learn/courses/mysql-for-python-developers/using-mysql-with-python/using-cursors?autoplay=1 [Accessed 15 May 2025].
- Sencha. (2023). Event Handling in JavaScript: A Practical Guide with Examples. [online] Available at: https://www.sencha.com/blog/event-handling-in-javascript-a-practical-guide-with-examples/ [Accessed 25 May 2025].
- TutorialsPoint.com, 2025. AJAX Tutorial. [online] Available at: https://www.tutorialspoint.com/ajax/index.htm [Accessed 18 May 2025].
- W3Schools.com, 2025a. HTML `<div>` Tag. [online] Available at: https://www.w3schools.com/tags/tag_div.ASP [Accessed 16 May 2025].
- W3Schools.com, 2025b. HTML `<h1>` to `<h6>` Tags. [online] Available at: https://www.w3schools.com/tags/tag_hn.asp [Accessed 16 May 2025].
- W3Schools.com, 2025c. HTML `<option>` Tag. [online] Available at: https://www.w3schools.com/TAgs/tag_option.asp [Accessed 16 May 2025].
- W3Schools. (n.d.). HTML DOM onkeyup Event. [online] Available at: https://www.w3schools.com/jsref/event_onkeyup.asp [Accessed 25 May 2025].
- W3Schools.com, 2025. HTML input type="hidden" Attribute. [online] Available at: https://www.w3schools.com/tags/att_input_type_hidden.asp [Accessed 23 May 2025].
- W3Schools.com, 2025d. HTML onClick Attribute. [online] Available at: https://www.w3schools.com/TAGs/att_onclick.asp [Accessed 16 May 2025].
- W3Schools.com, 2025e. jQuery - Get Started. [online] Available at: https://www.w3schools.com/jquery/jquery_get_started.asp [Accessed 19 May 2025].
- W3Schools.com, 2025f. Python Global Variables. [online] Available at: https://www.w3schools.com/python/python_variables_global.asp [Accessed 23 May 2025].
- YouTube, 2023. Deploy Python Flask Web App on PythonAnywhere. [video online] Available at: https://www.youtube.com/watch?v=Bx_jHawKn5A [Accessed 19 May 2025].
- YouTube, 2023. Flask Crash Course - Build a Simple Web App with Python. [video online] Available at: https://www.youtube.com/watch?v=jQjjqEjZK58 [Accessed 15 May 2025].





