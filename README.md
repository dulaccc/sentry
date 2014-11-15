# Sentry instance

> Shit happens — Be on top of it.


## Deploy

### Create the Heroku app

```sh
$ heroku create --region <region> y-sentry
```

### Push the code

```
$ git push heroku master
```

### Set the required settings

```sh
$ heroku config:set SENTRY_URL_PREFIX="https://y-sentry.herokuapp.com"
$ heroku config:set SENTRY_KEY="a-great-unique-secret-string"
$ heroku config:set SENTRY_CONF="sentry.conf.py"
```

### Add the services

```sh
$ heroku addons:add newrelic
$ heroku addons:add mandrill
$ heroku addons:add rediscloud
$ heroku addons:add heroku-postgresql:hobby-dev
```

### Run the migrations

```sh
$ heroku run sentry upgrade
```

### Create the superuser

```sh
$ heroku run sentry createsuperuser
$ heroku run sentry repair --owner=<username>
```
