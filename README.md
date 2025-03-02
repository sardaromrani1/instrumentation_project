# Instrumentation Project
This is a Django web application to store and manage instrumentation data. The application allows an admin to input and
store various data related to instruments, such as Manufacturer, Model, Part Number and Range.

# Features
* Admin panel for managing instrumentation data.
* Fields for Manufacturer, Model, Part Number, and Range.
* User-friendly interface for data input and viewing.

# Installation
1. Clone the repository
   git clone https://github.com/sardaromrani1/instrumentation_project.git
2. Set up a virtual environment
   python -m venv venv
   source venv/bin/activate  # On windows: venv\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt
4. Set up the database:
   python manage.py migrate
5. Create a superuser (admin)
   python manage.py createsuperuser
6. Run the development server
   python manage.py runserver
7. Access the admin panel
   Go to http://127.0.0.1:8000/admin/ in your browser, and log in using the superuser

# Project Structure
* instrumentation_project/: The main project directory
      * models.py: Defines the model for storing instrument data.
      * views.py: Handles views and responses for the application.
      * urls.py: URL routing for the application
      * admin.py: Registers models in the Django admin interface
* requirements.txt: Lists the Python packages required for the project.
* manage.py: The Django management script for running the application.

# Technologies Used
* Django: Python web framework for building the application.
* SQLite: Default database (can be configured to use other databases).
* HTML/CSS: For rendering the admin interface.

# Contributing
1. Fork the repository.
2. Create a new branch ( git checkout -b feature-name ).
3. Commit your changes ( git commit -am 'Add new feature' ).
4. Push to the branch ( git push origin feature-name ).
5. Open a pull request.

# License
The project is licensed under the MIT License.
