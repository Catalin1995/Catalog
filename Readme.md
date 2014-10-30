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

1. Install [heroku toolbelt](https://toolbelt.heroku.com/)
2. Change directory to project repository.
3. Add heroku remote

```
git remote add heroku git@heroku.com:agile-ridge-5265.git
```

4. Push code to heroku

```
git push heroku master
```