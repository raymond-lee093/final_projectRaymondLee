### INF601 - Advanced Programming in Python
### Raymond Lee
### Final Project


# Final Project

## Description


This project combines the Django web framework with the Spoonacular API to create a recipe search and management 
application. Users can search for recipes based on ingredients, cuisine type, dietary restrictions, and meal type. 
The application fetches recipe information from the Spoonacular API and displays the results to the user.
User Authentication and Authorization: Users can register, log in, log out, and reset their passwords.
User Profile Management: Users have profile pages where they can update their email addresses.
Recipe Search: Users can search for recipes based on ingredients, cuisine type, dietary restrictions, and meal type.
Detailed Recipe Information: Users can view detailed information about a specific recipe, including ingredients and 
their prices. PostgreSQL is used for storing user information and recipe data.
Spoonacular API provides recipe data and information about ingredients. For frontend styling and design, HTML, CSS, and 
are used.


## Getting Started

### Dependencies

* [Django Documentation](https://docs.djangoproject.com/en/5.0/)
* [Django Github Docs](https://github.com/django/django/tree/main)
* [Python](https://automatetheboringstuff.com/#toc)
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Jinja2](https://flask.palletsprojects.com/en/3.0.x/templating/#jinja-setup)
* [Spoonacular API docs](https://spoonacular.com/food-api/docs)

### Pip install instructions

Please run the following:
```
pip install -r requirements.txt
```

### Executing program

Configure the PostgreSQL database in settings.py.
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Database name",
        "USER": "user name",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

```
In a terminal window, please type the following: <br>
This will create any SQL entries that need to go into the database

```
python manage.py makemigrations 
```

This will apply the migrations
```
python manage.py migrate
```

This will create the administrator login info for your /admin side of your project
```
python manage.py createsuperuser 
```

Start Django server

```
python manage.py runserver

```
## Help

Link to visit admin site, administrator login info must be created first
```
http://localhost:8000/admin/login/?next=/admin/
```

### Password reset
To password reset, complete within project. In the console you will receive an email with
the subject as 'Password reset on 127.0.0.1:8000', from 'webmaster@localhost', and to 
the email associated with the created account. Within the subject of email, you are to copy the link 
that is sent and paste it in the browser url to complete the password reset.

## Authors

Contributors names and contact info

ex. Raymond Lee 

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License.

## Acknowledgments

Inspiration, code snippets, etc.
* [Django Tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
* [Google Icon Images](https://fonts.google.com/icons)











