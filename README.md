# chatzilla
Chat app developed in django and python, deployed on heroku.

![Alt text](screenshot.png?raw=true "Chatzilla Demo")

### Features
* Web based chat application for small team, company.
* Best suited for LAN/Wifi based chat in small network, just deploy this on a local server in LAN.
* One to one chat with separate room/section for chat context with each person.

### Coming up
* Send file/s via web chat
* Chat rooms
* Bug fixes 

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
