import requests

def Translate(message):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    
    payload = "q=" + message + "&source=en&target=es"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': "b9e8193e47msh9c1c5b4c6dee4e0p18a4ebjsn6bca5efc53ef",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return response.text