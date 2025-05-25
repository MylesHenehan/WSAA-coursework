# Web Services and Applications: Big Project
### Author: Myles Henehan
### Student Number: G00439446

***
# Freelance Linguist Web App  
This full-stack web application was developed as the final project for the Web Services and Applications module. It demonstrates the integration of front-end and back-end technologies to build a dynamic, database-driven system. The application enables users to manage a list of freelance linguists, supporting core CRUD operations: viewing, adding, updating, and deleting records. The front end is built using HTML, Bootstrap, and jQuery, providing a responsive and user-friendly interface. The back end is powered by a Flask-based REST API, which handles data transactions and communicates with a MySQL database via a custom Data Access Object (DAO) layer. AJAX is used to enable asynchronous interaction between the client and server. The application is deployed on PythonAnywhere, showcasing practical skills in full-stack development, RESTful API design, and cloud-based deployment.

This project extends the sample code provided in the module by incorporating additional features. It utilises two tables instead of one - a linguists table and a rates table - which are joined using LinguistID as the primary key. Additionally, a search bar has been added to enable users to filter the results. Finally, Bootstrap is used to enhance the webpage’s design, creating a more cohesive and polished appearance.

I chose the theme of a linguist database because I work as a Translation Project Manager. Currently, when selecting linguists for projects, we use Google Sheets to query the information we have on record. However, I believe we would greatly benefit from using a dedicated database — albeit a much more detailed one than the example showcased here. Using a theme related to my everyday work helped me view the application from a user’s perspective and better understand the features and functionalities that would be needed.

---

## 🗂 Project Structure

| File | Description |
|------|-------------|
| `server.py` | The main Flask application. It defines the REST API routes and integrates with the DAO and HTML template. |
| `linguistDAO.py` | A Python Data Access Object (DAO) module that handles all interactions with the MySQL database. |
| `linguistfinder.html` | A front-end HTML template that provides a web interface for interacting with the linguist database using AJAX. |
| `dbconfig.py` | Contains database configuration details such as connection parameters, used by the DAO to establish database connections. |
| `requirements.txt`| Lists all Python dependencies needed to run the application (used for quick setup in virtual environments or deployment). |
| `db-backup.sql`| The database to import if you are running the application locally. |



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
- Filter and load individual linguists via API route (`/linguists/<id>`) or through the search box

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
- Contains form inputs for Name, Email, Target Locale, Per-Word Rate and Hourly Rate.
- Shows a table of all linguists
- Target locale dropdown includes a hardcoded list of accepted languages `fr-FR`, `es-LA`, `ru-RU`, etc.

---

## ✅ Setup Instructions for Running the Application Locally.

1. **Clone the repo**
2. Import the database file db-backup.sql from the repo to MySQL
3. Add your DB credentials in `dbconfig.py`
4. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run your app:
   ```bash
   python server.py
   ```

---

## 🌐 Live Demo

You can also view and interact with the project here:  
👉 **[https://myleshenehan.pythonanywhere.com/](https://myleshenehan.pythonanywhere.com/)**

This is hosted on [PythonAnywhere](https://www.pythonanywhere.com/), where the Flask backend and MySQL database are deployed in a live environment.

## 🔮 Areas for Further Development
- Add authentication and user roles (e.g., Admin vs Viewer).
- Add more restrictions around input values and provide warnings to users if the inputs don't align with the schema of the database.
- - Improve search filtering with autocomplete or advanced filters (e.g., by rate or language).


---

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





