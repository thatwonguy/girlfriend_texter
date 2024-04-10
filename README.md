# Girlfriend/Boyfriend/Anybody_texter
Send text to girlfriend (or really anyone with a phone number) on auto-pilot.

## 1. Configure your settings in `utils.py`.

```
phone_number = "+155555555"
# enter the target phone number inside the quotation marks. use the format "+15555555"
message = ['Good Morning Babe', 'Good morning my love', 'Good morning cutie 😘']
# just make sure the message is inside the quotation marks. An example is "did you sleep well?"
schedule_time = "08:00"
# make sure the hour has degits (24-hour standard)
```

Note: If you want to send a message everyday at 8:45 AM, you will need to set `schedule_time = "08:45"` in  `utils.py`.

## 2. Install requirements
```
pip install -r requirements.text
```

## 3. Run the script

```
python main.py
```

Note: if you want run in background

```
python main.py > pid.txt 2>&1 & 
```
*Jobs can be accessed with the `jobs` command. jobs will show you the running jobs, and number them. You could then talk about the jobs using a `%` followed by the number like `kill %1` or so.*