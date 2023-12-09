# LittleLemon
Capstone project for Meta's Back-End Developer Professional Certificate through Coursera 
# Setup(MacOS)
## Structure
This is a back-end prject using the Django Framework.  The project is called `littlelemon` and is split into 2 apps:
- `api` handles all of the relevant api endpoints
- `restaurant` handles all of the front-end endpoints and templates/files. ***(This is currently under construction)***
  - Note: this part is for my own experimentation since I have limited front-end experience. The core of this project concerns the api app and it's interaction with the database. Not all of the restaurant endpoints work and I am aware, so don't focus there. 
## Initial Project Setup
### Terminal
```
# Enter project folder
cd <littlelemon project folder>
# Install Dependancies
pipenv install
# Activate virtual environment
pipenv shell
# At this point, make sure you select the correct python interpreter
```
## Database Setup (Please install MySQL and configure for your device before proceeding
### Terminal
```
# Enter MySQL shell and input credidentials
mysql -u root -p
# create database and user
create database littlelemon;
use littlelemon;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
exit;
```
### settings.py
```
# Configure this file for your system
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': '<your_username>',
        'PASSWORD': '<your_password>',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}
```
### Terminal
```
# make migrations
python3 manage.py makemigrations
python3 manage.py migrate
```
## Endpoints
### Admin
The django framework provides a number of endpoints through the `admin` class to provide a gui for managing the database and users.  These endpoints can be found in [django documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
### Djoser
The djoser library provides a number of endpoints for the purposes of token-authentication.  These endpoints can be found in [djoser documentation](https://djoser.readthedocs.io/en/latest/base_endpoints.html)
### API
To use these API endpoints, you are required to use `tokens`.

These `tokens` can be created through these endpoints
- **/auth/token/login** 
- **/admin/authtoken/tokenproxy/add/**

Here are the API endpoints
```
api/menu
api/menu/{ID}
api/bookings
api/bookings/{ID}
```
additional endpoints exist thanks to the DRF

(TBC)
