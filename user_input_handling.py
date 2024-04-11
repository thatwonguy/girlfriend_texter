"""Module allowing user a single location to make necessary modifications to affect output."""

import random
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


def get_schedule() -> str:
    """Enter what schedule time in "24-hour format."""
    schedule = config["schedule"]
    return schedule


# Enter you email address
def get_sender_email() -> str:
    """Enter your gmail address

    Returns:
        str: your gmail address
    """
    sender_email = config["sender_email"]
    return sender_email


def get_sender_password() -> str:
    """
    Enter Your gmail app password created from your google
    account --> https://myaccount.google.com/apppasswords
    """
    sender_gmail_app_password = config["sender_gmail_app_password"]
    return sender_gmail_app_password


def get_recipient_number() -> str:
    """
    Enter your targets cellphone
    """
    recipient_number = config["recipient_number"]
    return recipient_number


def get_carrier() -> str:
    """Provide your targets carrier address.

    Returns:
        str: carrier address
    """
    recipient_carrier_gateway = config["recipient_carrier_gateway"]
    return recipient_carrier_gateway


def get_messages() -> list:
    """
    Enter a list of messages that will be chose and
    sent randomly on that schedule basis.
    Add and remove as you see fit.
    """
    message = list(config["message"])
    return message


def get_random_message() -> str:
    """
    This will randomly select a message
    from the list of messages to be sent off each time.
    """
    messages = get_messages()
    return random.choice(messages)
