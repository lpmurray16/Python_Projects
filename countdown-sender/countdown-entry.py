import time
from twilio.rest import Client
from datetime import datetime, timedelta

# Twilio account information
account_sid = "AC5efd42b3799fb7096cff94a9f370988e"
auth_token = "e0bc5b0a361a589004d5615dbc7662cc"

# Set the date that the user provided
target_date = datetime(2023, 2, 4)

# Create a new Twilio client
client = Client(account_sid, auth_token)

# Function to send a text message using Twilio


def send_text_message(to, body):
    message = client.messages.create(to=to, from_="+13854626503", body=body)

# Function to calculate the number of days until the target date


def days_until_target_date():
    # Get the current date
    now = datetime.now()

    # Calculate the difference between the current date and the target date
    delta = target_date - now

    # Return the number of days until the target date
    return delta.days


# Main loop
while True:
    print("Sending text message...\n\nProgram currently running...\n\nSends again in 24 hours...")
    # Calculate the number of days until the target date
    days = days_until_target_date()

    # Send a text message to the user with the number of days until the target date
    send_text_message(
        "+18155271977", "\n\nThere are {} days until Quill is better!".format(days))

    # Wait for 24 hours before sending the next message
    time.sleep(24 * 60 * 60)
