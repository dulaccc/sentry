# Sentry instance

> Shit happens — Be on top of it.


## Automatic Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/dulaccc/sentry/tree/develop)

Then just create the superuser

```sh
$ heroku run sentry createsuperuser --app <your-app-name>
$ heroku run sentry repair --owner=<username> --app <your-app-name>
```


## Manual Deploy

### Create the Heroku app

Create the app in the region you want

```sh
$ heroku create --region <region> y-sentry
```

Then set the proper buildpack

```sh
$ heroku config:set BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git
```

### Push the code

```
$ git push heroku master
```

### Set the required settings

> NB: using a protocol-less url like `//my-sentry.herokuapp.com` allows you to access the interface with both `http` and `https`.

```sh
$ heroku config:set SENTRY_URL_PREFIX="//my-sentry.herokuapp.com"
$ heroku config:set SENTRY_KEY=`openssl rand -base64 32`
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
