import os
from flask import (Flask, render_template, request, redirect,
                   url_for, flash, session, abort)

# --- Application Setup ---
app = Flask(__name__)

# **Essential Feature: Configuration**
# A secret key is needed for session management and flash messages.
# In production, use a strong, random key and keep it secret (e.g., environment variable).
app.config['SECRET_KEY'] = os.urandom(24) # Generates a random key each time app starts (ok for demo)
# More robust for dev: app.config['SECRET_KEY'] = 'your_very_secret_dev_key_here'


# --- Sample Data (Replace with database later if needed) ---
PROJECTS_DATA = [
    {'id': 1, 'title': 'Project Alpha', 'description': 'A web app for managing tasks.', 'tech': 'Python, Flask, HTML'},
    {'id': 2, 'title': 'Project Beta', 'description': 'Data analysis visualization tool.', 'tech': 'Python, Pandas, Matplotlib'},
    {'id': 3, 'title': 'Gamma Website', 'description': 'A responsive marketing website.', 'tech': 'HTML, CSS, JavaScript'}
]

# --- Routes ---

# **Essential Feature: Routing**
# Defines the URL endpoints for different pages.
@app.route('/')
def index():
    """Home Page Route"""
    # **Essential Feature: Template Rendering**
    # Uses render_template to process Jinja2 templates.
    page_title = "My Portfolio"
    return render_template('index.html', title=page_title)

@app.route('/about')
def about():
    """About Page Route"""
    return render_template('about.html', title="About Me")

@app.route('/projects')
def projects():
    """Projects Page Route"""
    # Passing data to the template
    return render_template('projects.html', title="My Projects", projects=PROJECTS_DATA)

# **Essential Feature: Dynamic Routes / URL Variables**
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Displays details for a single project."""
    project = next((p for p in PROJECTS_DATA if p['id'] == project_id), None)
    if project is None:
        # **Essential Feature: Error Handling (abort)**
        # Trigger a 404 Not Found error if project doesn't exist.
        abort(404)
    return render_template('project_detail.html', title=project['title'], project=project)


# **Essential Feature: Request Handling (Methods GET/POST)**
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Page Route - Handles GET (display form) and POST (process form)"""
    if request.method == 'POST':
        # **Essential Feature: Accessing Request Data**
        # Access form data submitted via POST.
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation (in a real app, use libraries like WTForms)
        if not name or not email or not message:
            # **Essential Feature: Message Flashing**
            # Store a message to show to the user on the *next* request. Requires SECRET_KEY.
            flash('All fields are required!', 'error') # 'error' is an optional category
        else:
            # Process the form data (e.g., send email, save to database)
            print(f"Received message from {name} ({email}):\n{message}") # Simulate processing
            flash('Thank you for your message!', 'success')

            # **Essential Feature: Redirecting**
            # Redirect the user after successful form submission (Post/Redirect/Get pattern)
            # **Essential Feature: URL Building (url_for)**
            # Generates URLs dynamically based on the function name. More robust than hardcoding URLs.
            return redirect(url_for('contact')) # Redirect back to the contact page

    # For GET requests or if POST validation fails, render the form template.
    return render_template('contact.html', title="Contact Me")


# **Essential Feature: Sessions**
@app.route('/visit-counter')
def visit_counter():
    """Demonstrates session usage."""
    # **Essential Feature: Session Object**
    # Access the session dictionary. Requires SECRET_KEY.
    count = session.get('visit_count', 0) # Get value or default to 0
    count += 1
    session['visit_count'] = count # Store updated value back in session
    flash(f"This page has been visited {count} times during your session.", "info")
    return render_template('visit_counter.html', title="Session Counter", count=count)

# **Essential Feature: Custom Error Handling**
@app.errorhandler(404)
def page_not_found(error):
    """Custom handler for 404 Not Found errors."""
    # You can log the error here: app.logger.error(f'Page not found: {request.path}')
    return render_template('404.html', title="Page Not Found"), 404 # Return tuple with status code


# --- Run the App ---
if __name__ == '__main__':
    # **Essential Feature: Development Server**
    # app.run() starts Flask's built-in server.
    # debug=True enables auto-reloading on code changes and provides a debugger in the browser for errors.
    # NEVER use debug=True in production!
    app.run(debug=True)