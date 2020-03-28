import requests

def corona():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"
    headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    confirmed = x['total_cases']
    death = x['total_deaths']
    recovered = x['total_recovered']
    new_cases = x['new_cases']
    new_deaths = x['new_deaths']
    return confirmed,death,recovered,new_cases,new_deaths