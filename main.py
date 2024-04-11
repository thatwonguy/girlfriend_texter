"""Main Module that texts your gf/bf/whoever you target"""

import time
import smtplib
from email.mime.text import MIMEText
import schedule
import user_input_handling

SCHEDULE_TIME = user_input_handling.get_schedule()


def send_text_message() -> None:
    """_summary_
    Get user-defined settings from modify_me.py
    and carry out the texting function on
    a set schedule until program is stopped.
    """
    sender_email = user_input_handling.get_sender_email()
    sender_app_password = user_input_handling.get_sender_password()
    recipient_number = user_input_handling.get_recipient_number()
    message = user_input_handling.get_random_message()
    gateway_address = user_input_handling.get_carrier()

    # Compose the message in correct text messaging format
    msg = MIMEText(_text=message)

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()
    server.login(user=sender_email, password=sender_app_password)

    # Try sending the message with each gateway address until successful
    try:
        # Send the message
        server.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_number + "@" + gateway_address,
            msg=msg.as_string(),
        )
        print(
            "Message sent successfully to",
            recipient_number,
            "via",
            gateway_address,
            msg,
        )
    except Exception as e:
        print("Failed to send message to", recipient_number, "via", gateway_address)
        print("Error:", e)
    finally:
        # Add a potential delay to prevent overloading the gateways
        time.sleep(0)

    # Quit the server
    server.quit()


# Schedule the message to be sent every day at the specified time
schedule.every().day.at(SCHEDULE_TIME).do(send_text_message)

# Run the scheduler with a longer interval for checking the schedule
while True:
    schedule.run_pending()
    time.sleep(1)  # Check the schedule every minute
