## Make your link shorter!

This is a simple app using Flask, SQLAlchemy, apscheduler for cron job, zlib for make hash data and the connecting Flask-SQLAlchemy library.

### Clone repository

```
git clone https://github.com/htkachuk/shortLink.git
cd shortLink
```

### Installing Dependencies

```
pip install -r requirements.txt
```

### Running the App
To run the app, first run the models.py file directly to create the database tables:

```
python3 models.py
```

You only need to do this once, unless you change your model definitions.

Then run the app itself:

```
python3 app.py
```

## Api routes

Post: http://127.0.0.1:5000/create_short_url

BODY PARAMS: url - required, expiration 90 days as default value
example:

{
"url": "https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2",
"expiration": "10"
}

answer:

{
"expiration": "Tue, 10 Nov 2020 00:00:00 GMT",
"result": "ok",
"short_url": "7c0cecda"
}

Get: http://127.0.0.1:5000/7c0cecda

Will redirect to: https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2

if not found: Error url not found
