# Girlfriend/Boyfriend/Anybody_texter
*Show your signficant others that you care! Send text messages to your girlfriend (or really anyone with a phone number) on auto-pilot!*

*This app is designed to use a google gmail account that you create or already have to send text* *messages to your girlfriend/boyfriend/hubby/wifey/friend or anyone else with a cell phone. This app*
*is currently designed to be run on your local machine. Once you have it running, it will continue* *to send text messages for as long as it is running on schedule until it is stopped or interrupted.*

## 1. Configure your settings in `config.yaml`.

1. Enter the time within 24 hour period you'd like to message your target.  
Enter the value in '00:00' (which is hour:minutes format) between the single qoutes.  
As an example '08:00' would be 8:00am, and '23:00' would be 11:00pm.  
`schedule: '08:00'`

2. Enter the gmail account you will use to send these texts messages.  
Your target will see this email when they recieve the text message.  
Enter the value between the single quotes.  
`sender_email: 'enter your own gmail here'`

3. You must sign in to your google account, go to your google account settings and create your temporary and restricted app password which you can revoke at anytime, in order to use this app. Found here --> [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords). 

    This allows for usage of a separate, temporary, and restricted app password to be able to use this app to send off the text messages without having to provide your actual gmail credentials.
    Enter the value between the single quotes.  
`sender_gmail_app_password: 'copy paste your temporary app password here'`

4. Enter your targets phone number here. Country code etc not needed, only the 10 main digits.  
Enter the value between the single quotes.    
`recipient_number: '1234567890'`

5. Google search your targets sms carrier gateway and enter it here. Do not include the @ symbol.  
T-mobiles carrier gateway is provided as an example ---> 'tmomail.net'. Replace as necessary for your target.  
Enter the value between the single quotes.  
`recipient_carrier_gateway: 'xxxxxxxx.xxxxxxxx.com'`

6. Enter a single message or any number of messages and they will be randomly sent on that schedule you set everyday.  
Enter the value between the single quotes.  
    ```
    message: 
    - 'This is message 1.'
    - 'This is message 2.'
    - 'This is message 3.'
    ```

## 2. Install requirements
> [!NOTE]
> Preferrably you will create a virtual environment dedicated to this app and then activate that venv and install the requirements file in there with the following line in bash terminal, or alternatively write this command in bash terminal:
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
*Jobs can be accessed with the `jobs` command. Jobs will show you the running jobs, and number them. You could then talk about the jobs using a `%` followed by the number like `kill %1` or so to stop it from running in the background, or restart your computer.*
