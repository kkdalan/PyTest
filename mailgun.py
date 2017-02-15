import requests

def send_simple_message(API_BASE_URL, API_KEY):
    return requests.post(
        API_BASE_URL,
        auth=("api", API_KEY),
        data={"from": "Developer <postmaster@sandbox7d50e6cbfd3e43e7bcb41ded0b42bdd0.mailgun.or0un.org>",
        "to": ["andbox7d50e6cbfd3e43e7bcb41ded0b42bdd0.mailgun.org"],
        "subject": "Hello! Alan",
        "text": "Thanks for signing up with us!."})

send_simple_message('https://api.mailgun.net/v3/sandbox7d50e6cbfd3e43e7bcb41ded0b42bdd0.mailgun.org',"key-701b8c16091b70198653a3da7f676edc")
print("sent by mailgun!")
