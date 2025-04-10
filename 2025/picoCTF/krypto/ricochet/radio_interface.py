import requests

# TODO: you will need to fill this in with the URL of the challenge
SERVER_URL = "http://127.0.0.1:5000"

# Returns a list of messages seen on the air since the last time this function
# was called
def receive_radio_messages():
    messages = requests.get(SERVER_URL+"/radio_rx").json()

    for msg in messages:
        print("DEBUG: Received message", msg)

    return messages

# [message] argument should be a Python dict object
def inject_radio_message(message):
    requests.post(SERVER_URL+"/radio_tx", json=message)

def start_robot():
    requests.get(SERVER_URL+"/start")

def stop_robot():
    requests.get(SERVER_URL+"/stop")

# Get the location of the robot and the obstacles on the grid
def get_board_state():
    return requests.get(SERVER_URL+"/state").json()
