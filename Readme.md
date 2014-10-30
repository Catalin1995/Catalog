Install
=======

This project uses virtualenv

[Read about it](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)

```shell
virtualenv venv
. venv/bin/activate
```

TLDR - this will isolate your python instalation

Deployment
==========

# Install [heroku toolbelt](https://toolbelt.heroku.com/)
# Change directory to project repository.
# Add heroku remote

```
git remote add heroku git@heroku.com:agile-ridge-5265.git
```

# Push code to heroku

```
git push heroku master
```