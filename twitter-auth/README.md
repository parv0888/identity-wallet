# Tweepy Twitter Api
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ac554483fac462797ffa5a8b9adf2fa?style=flat-square)]()
[![Build Status](https://api.travis-ci.org/fossasia/badgeyay.svg?branch=development&style=flat-square)]()


Twitter authentication using Tweepy API using Django.
The application can do following functionalities:
  - Fetch tweets from home timeline of authenticated user containing URLs.
  - View all the tweets fetched till date using the following application.
  - Display the most shared Domain from the database.
  - Display the User who shared maximum URLs.

Link to the application - https://twitter-tweepy.herokuapp.com/

## Pre-requisites (to run App locally)
- Python 3.6 and pip should be preinstalled
- Twitter developer Credentials
- PostgreSQL database


## Technology Stack

- Programming Languages
    - Python 3.6
    
- Frameworks
  - Django 3.1.2

- Database
     - PostgreSQL

- Frontend
    - HTML 5
    - CSS 3
    - Jinja
    - Bootstrap 4

- APIs
    - Tweepy Api
        

## How To Use
1. Clone the repository
```sh
git clone https://github.com/tds-1/vouch-tweepy
```
2. Generate **CONSUMER_KEY** and **CONSUMER_KEY** from Twitter Developer console (https://developer.twitter.com/en/portal/projects-and-apps) and paste them in the .env file .
```
# Django Secret Key
# ------------------
SECRET_KEY=


# Database config
# ----------------
POSTGRES_DB_NAME=
POSTGRES_DB_USER=
POSTGRES_DB_PASSWORD=
POSTGRES_DB_HOST=
POSTGRES_DB_PORT=

# Application key
# ----------------
CONSUMER_KEY = 
CONSUMER_SECRET = 
```
3. Enter **Database credentials** in .env file along with the **seceret key**.
4. Create a **virtual environment**.
5. Install the dependenies
```sh
pip install -r requirements.txt
```
6. **Migrate** the tables to the database.
```sh 
python manage.py makemigrations
python manage.py migrate
```
7. **Run** the django server on local host.
```sh 
python manage.py runserver
```

## Project Folder Structure

- Sub-directories of the folders marked with ' * ' are not shown for clarity.


```bash
.
├── djangotweepy
│   ├── __init__.py
│   ├── __pycache__*
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── images*
├── manage.py
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── twitter_auth
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── home_timeline.py
    ├── __init__.py
    ├── migrations*
    ├── models.py
    ├── __pycache__*
    ├── static
    │   ├── css
    │   │   ├── achievements.css
    │   │   └── tweets.css
    │   └── media*
    ├── templates
    │   └── twitter_auth
    │       ├── achievements_domain.html
    │       ├── achievements.html
    │       ├── base.html
    │       ├── info.html
    │       ├── login.html
    │       ├── messages.html
    │       ├── post_tweet.html
    │       ├── public_tweets.html
    │       └── view_tweets.html
    ├── tests.py
    ├── urls.py
    ├── utils.py
    └── views.py

```


## Snapshots
- First page with which the interacts, here user will log himself in.
![alt text](https://github.com/tds-1/vouch-tweepy/blob/master/images/homepage.png)
- Home page where all the routes are shown.
![alt text](https://github.com/tds-1/vouch-tweepy/blob/master/images/main.png)
- Output of 1st and 2nd link.
![alt text](https://github.com/tds-1/vouch-tweepy/blob/master/images/tweets.png)
- Profile who has tweeted mmost number of URLs.
![alt text](https://github.com/tds-1/vouch-tweepy/blob/master/images/profile.png)
- Top Domains which have been tweeted maximum times.
![alt text](https://github.com/tds-1/vouch-tweepy/blob/master/images/domain.png)
