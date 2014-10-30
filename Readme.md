Install
=======

1. Clone the project with GitHub for Windows.
2. Change directory to project repository.
3. Oepn git bash.

```
cd Catalog
pip install -r requirements.txt
```
4. [install mongodb](http://www.mongodb.org/downloads)

```
sh start_db.sh
python catalog.py
```

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

The Joel Test
=============

Do you use source control?
Can you make a build in one step?
Do you make daily builds?
Do you have a bug database?
Do you fix bugs before writing new code?
Do you have an up-to-date schedule?
Do you have a spec?
Do programmers have quiet working conditions?
Do you use the best tools money can buy?
Do you have testers?
Do you do hallway usability testing?

Other
=====

This project uses virtualenv

[Read about it](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)

```shell
virtualenv venv
. venv/bin/activate
```

TLDR - this will isolate your python instalation