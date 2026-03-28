# Overview

I am trying to further my learning as a software engineer by exploring web development and how web frameworks handle 
the full stack of a web application. My goal with this software was to learn how Django works and how it connects a 
backend, a database, and a frontend together in a clean and organized way.

The software is a simple event registration web app built with Django. Users can browse upcoming events and sign up for 
them with their name and email. To start a test server on your computer, navigate to the project folder and run the 
following command:

```commandline
python manage.py runserver
```

You also need to migrate the databases by running the following commands:

```commandline
python manage.py makemigrations events
python manage.py migrate
```

Then open your browser and go to `http://127.0.0.1:8000` to see the event list page. You will need to 
visit `http://127.0.0.1:8000/admin/` to add events before anything shows up on the main page. But you are required to 
create a superuser first before by running the following command:

```commandline
python manage.py createsuperuser
```

The purpose of writing this software was to learn how Django works and how it can be used to build real web 
applications that interact with a database.

[Software Demo Video](https://www.youtube.com/watch?v=6CB0frIw11A)

# Web Pages

**Event List Page** - This is the home page of the app at `/`. It displays all events stored in the database, 
showing the name, date, location, and how many spots are remaining. Each event name is a link that takes you to the 
detail page for that event. If no events have been added yet, the page tells you to add some through the admin panel. 
The list of events and their spot counts are generated dynamically from the database each time the page loads.

**Event Detail Page** - This page is reached by clicking an event from the list. It shows the full details of the 
event including the description and remaining capacity. Below the details is a registration form where users can 
enter their name and email to sign up. If the event is full, the form is hidden and a message is shown instead. After 
a successful registration the page reloads and shows a success message. The list of current registrants at the bottom 
of the page is also dynamically generated from the database.

**Admin Panel** - Django's built-in admin panel is available at `/admin/`. This is where events are created and 
managed, and where all registrations can be viewed. Access requires a superuser account.

# Development Environment

The project was built using Python and the Django web framework. The IDE used was PyCharm. The database is SQLite, 
which Django manages automatically with no extra setup required.

The programming language used was Python. The following tools and libraries were used:

* **Django** - The web framework that handles routing, templating, and the admin panel.
* **SQLite** - The file-based database (similar to MySQL) that Django uses by default for development.

# AI Disclosure

No use of AI was used during this project.

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/)
* [Django Girls Tutorial](https://tutorial.djangogirls.org/)
* [W3Schools Django Tutorial](https://www.w3schools.com/django/)

# Future Work

* Add user authentication so registrants can log in and view or cancel their own registrations
* Add the ability to send a confirmation email when someone registers
* Add an event image or banner to make the event pages more visually useful
* Allow admins to export the registration list for an event to a CSV file