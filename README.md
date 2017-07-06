# Odds Bot

This is live dashboard which execute odds from providers, and shows odds/probability directly into dashboard.

## Install

From you python3 virtualenvironment run:

```pip install -r requirements.txt```

After requirements would be installed, run migrations for DB by running:

```python manage.py migrate```

Then you need to load information about races from fixtures that I already prepared:

```pythno manage.py loaddata fixtures.json```

## Update odds
After that you can either update information from providers by running 

``` python manage.py update_providers --race_id <id for race, e.g. 1> ```

Or add cron task into your cron file
Example:

``` */5 * * * * /path/to/virtualenv/python /path/to/manage.py update_providers --race_id 1 ```

this cron command will update odds from providers every 5 minutes.

## Prerequisites
* For message exchanging in dashboard I use WebSockets, so you will see live updates if they any in database.
* In fixtures I add two events, so you can test events execution by getting on index page, and add `race_id` to parameters e.g. `http://localhost:800/?race_id=2`

