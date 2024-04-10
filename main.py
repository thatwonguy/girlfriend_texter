import schedule
import time
import smtplib
from email.mime.text import MIMEText
from carrier_gateways import carrier_gateways  # Import the list of carrier gateway addresses

def send_text_message():
    # Set up your email and password
    email = "your_email@gmail.com"
    password = "your_password"

    # Recipient's phone number
    recipient_number = "1234567890"

    # Compose the message
    message = "Hello! This is a scheduled text message."

    # Set up SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    # Try sending the message with each gateway address until successful
    for gateway_address in carrier_gateways:
        try:
            # Send the message
            server.sendmail(email, recipient_number + "@" + gateway_address, message)
            print("Message sent successfully to", recipient_number, "via", gateway_address)
            break  # Exit loop if message sent successfully
        except Exception as e:
            print("Failed to send message to", recipient_number, "via", gateway_address)
            print("Error:", e)

    # Quit the server
    server.quit()

# Schedule the message to be sent every day at 9:00 AM
schedule.every().day.at("09:00").do(send_text_message)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
