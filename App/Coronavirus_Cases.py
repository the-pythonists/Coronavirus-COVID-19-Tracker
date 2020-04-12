import requests
from matplotlib import pyplot as plt
import numpy as np

def corona_world_cases():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"
    headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    confirmed = x['total_cases']
    death = x['total_deaths']
    recovered = x['total_recovered']
    new_cases = x['new_cases']
    new_deaths = x['new_deaths']
    return confirmed,death,recovered,new_cases,new_deaths

def corona_countries_cases(country):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring = {"country":country}
    headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    x = response.json()
    y = x['data']['covid19Stats']
    
    l = []
    select_list = ['province','country','confirmed','deaths','recovered']
    for j in y:
        k = [j[i] for i in select_list if i in j]
        l.append(k)
    return l

def corona_in_india_statewise():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    y = x['state_wise']
    keys = ['state','active', 'confirmed','deaths','recovered']
    data = []
    for i in y.values():
        values = list( map(i.get, keys) )
        data.append(values)
    d = data[:-1]
    new_data = [[int(k) if k.isdigit() else k for k in j] for j in d]
    return new_data

def corona_in_india_districtwise(city):
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
    headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    y = x['state_wise']
    keys = ['state','district']
    data = []
    l = []
    for i in y.values():
        values = list( map(i.get, keys) )
        data.append(values)
    d = data[:-1]
    state = city
    print('state is',city)
    l = []
    for lst in d:
        if lst[0] == state:
            for ii in lst[1:]:
                for a,b in ii.items():
                    l.append([a,b['confirmed']])
    return l

def corona_country_wise():
    url = "https://covid19-data.p.rapidapi.com/all"
    headers = {
    'x-rapidapi-host': "covid19-data.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    l = []
    select_list = ['country','confirmed','active','deaths','recovered']
    for j in x:
        k = [j[i] for i in select_list if i in j]
        l.append(k)
        l.sort(key=lambda t: t[1],reverse=True)
    return l

def TotalCasesGraph():
    global total_deaths
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    y = x['countries_stat']
    total_cases = []; countries = []; total_deaths = []
    for i in y:
        country_name = i['country_name']
        cases = i['cases'].replace(",","")
        deaths =i['deaths'].replace(",","")
        total_cases.append(cases)
        countries.append(country_name)
        total_deaths.append(deaths)
    return total_cases,countries,total_deaths

def TotalDeathsGraph():
    countries_name = TotalCasesGraph()[1]
    tot_deaths = TotalCasesGraph()[2]
    countries_name.reverse()
    tot_deaths.reverse()
    td = [int(b) for b in tot_deaths]
    col=['r','g','b','y','c']
    d=np.arange(len(countries_name[185:]))
    plt.bar(d,td[185:],color=col,edgecolor='black')
    plt.xlabel('Countries')
    plt.title('Graph')
    plt.ylabel('Total Deaths')
    plt.legend(col,countries_name[185:],loc=1,ncol=10,borderpad=1,shadow=True,framealpha=1,frameon=True,)
    plt.xticks(d,countries_name[185:],rotation=50,fontsize=8)
    #plt.savefig('D:\\Coronavirus-COVID-19-Tracker\\App\\static\\images\\photo1.png')

def worldPopulation():
    url = "https://ajayakv-rest-countries-v1.p.rapidapi.com/rest/v1/all"
    headers = {
    'x-rapidapi-host': "ajayakv-rest-countries-v1.p.rapidapi.com",
    'x-rapidapi-key': "Your API Key"
    }
    response = requests.request("GET", url, headers=headers)
    x = response.json()
    select_list = ['name','population']
    population = []
    for j in x:
        k = [j[i] for i in select_list if i in j]
        population.append(k)  
    return population