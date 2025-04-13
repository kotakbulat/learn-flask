# Simple Flask Portfolio Example

This project is a basic portfolio website built using the Flask microframework for Python. Its primary purpose is to demonstrate several essential features of Flask in a simple, interactive web application.

## Features

*   **Homepage:** Basic welcome page.
*   **About Page:** Simple static content page.
*   **Projects Page:** Lists sample projects (data defined in `app.py`).
*   **Project Detail Page:** Dynamically generated page for each project using URL variables.
*   **Contact Page:** Includes a functional contact form (demonstrates POST requests, form handling, redirects, and flash messages).
*   **Visit Counter Page:** Demonstrates session usage to count page visits within a browser session.
*   **Custom 404 Error Page:** Handles "Not Found" errors gracefully.
*   Basic CSS styling using a static file.

## Prerequisites

*   Python 3.7+
*   `pip` (Python package installer)
*   Virtual Environment tool (`venv` - included with Python 3)
*   A Code Editor (like Visual Studio Code)
*   Web Browser

## Setup and Installation (Windows - VS Code Terminal)

1.  **Clone or Download:** Get the project files into a directory named `flask_portfolio`.
2.  **Open Terminal:** Open a terminal within VS Code (`Terminal` -> `New Terminal`).
3.  **Navigate to Project Directory:**
    ```bash
    cd path\to\your\flask_portfolio
    ```
4.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```
5.  **Activate the Virtual Environment:**
    ```bash
    .\venv\Scripts\activate
    ```
    *(Your terminal prompt should now start with `(venv)`)*
6.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  Ensure your virtual environment (`venv`) is activated.
2.  Make sure you are in the project's root directory (`flask_portfolio`).
3.  Run the Flask development server:
    ```bash
    flask run
    ```
    *(Alternatively, you can run `python app.py`)*
4.  Open your web browser and navigate to: `http://127.0.0.1:5000` (or the address provided in the terminal).

The application runs with `debug=True`, which means:
*   The server will automatically reload if you make code changes.
*   You will see detailed error pages (debugger) in the browser if something goes wrong.
*   **Important:** Never run with `debug=True` in a production environment!


## Flask Features Demonstrated

This application showcases the following core Flask features. You can interact with them by navigating the website:

1.  **Routing (`@app.route`)**: Defined in `app.py` for each page (`/`, `/about`, `/projects`, `/project/<id>`, `/contact`, `/visit-counter`). Interact by clicking the navigation links.
2.  **Template Rendering (`render_template`)**: Used in all route functions in `app.py` to display HTML from the `templates/` folder. Visible on every page load.
3.  **Static Files (`url_for('static', ...)`):** The CSS (`static/style.css`) is linked in `templates/base.html` and served by Flask. Visible through the page styling.
4.  **Request Handling (Methods GET/POST)**:
    *   **GET**: Loading any page initially uses GET.
    *   **POST**: Submitting the form on the `/contact` page uses POST. Handled within the `contact()` function in `app.py`.
5.  **Accessing Request Data (`request.form`)**: When the contact form is submitted (POST), `request.form.get(...)` is used in `app.py` to retrieve the entered name, email, and message.
6.  **URL Building (`url_for`)**: Used extensively:
    *   In `templates/base.html` for navigation links.
    *   In `templates/projects.html` to link to specific project detail pages.
    *   In `app.py` within `redirect(url_for('contact'))` after successful form submission. Prevents hardcoding URLs.
7.  **Sessions (`session` object)**: Used on the `/visit-counter` page. A counter is stored in the browser's session cookie (requires `SECRET_KEY` config). Interact by refreshing the Visit Counter page.
8.  **Message Flashing (`flash`, `get_flashed_messages`)**: Used on the `/contact` page to show success or error messages after form submission, and on the `/visit-counter` page for informational messages. Requires `SECRET_KEY`. Messages appear near the top of the content area.
9.  **Error Handling (`@app.errorhandler`, `abort`)**:
    *   A custom 404 page (`templates/404.html`) is shown via `@app.errorhandler(404)` in `app.py`. Trigger by visiting a non-existent URL (e.g., `/invalid-page`).
    *   `abort(404)` is used in the `/project/<id>` route if an invalid project ID is provided. Trigger by visiting `/project/999`.
10. **Configuration (`app.config`)**: `app.config['SECRET_KEY']` is set in `app.py`, necessary for sessions and flashing.
11. **Development Server (`app.run(debug=True)` / `flask run`)**: How the application is started for development (see "Running the Application" section).
12. **Dynamic Routes / URL Variables (`@app.route('/.../<variable>')`)**: The `/project/<int:project_id>` route in `app.py` captures the ID from the URL to display the correct project details. Interact by clicking project titles on the Projects page.
13. **Template Inheritance (`{% extends %}`, `{% block %}`)**: `templates/base.html` defines the main layout, and other templates (`index.html`, `about.html`, etc.) extend it, filling in specific `{% block %}` sections. Ensures a consistent look and feel.

## Technology Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML5, CSS3
*   **Templating:** Jinja2 (Flask's default)