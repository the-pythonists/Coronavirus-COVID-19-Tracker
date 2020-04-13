from django.shortcuts import render
from django.http import HttpResponse
from App import Coronavirus_Cases
import requests
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
# Create your views here.

def index(request):
	'''case = Coronavirus_Cases.corona_world_cases()
				confirmed = case[0]
				death = case[1]
				recovered = case[2]
				newcases = case[3]
				newdeaths = case[4]'''
	confirmed = 10167932356
	death = 53245
	recovered = 213164
	newcases = 722
	newdeaths = 362
	casedetail = {'confirmed':confirmed,'death':death,'recovered':recovered,'newcases':newcases,'newdeaths':newdeaths}
	return render (request,'index.html',casedetail)

def searchbycountry(request):
	return render(request,'searchcountrycases.html')

def showcountrycases(request):
	if request.method == 'POST':
		countryName = request.POST.get('countryname')
		country = countryName.capitalize()
		data = Coronavirus_Cases.corona_countries_cases(country)
		param = {"detail":data,"country":country}
		return render(request,'showcountrycases.html',param)

def indiastatewise(request):
	data = Coronavirus_Cases.corona_in_india_statewise()
	param = {'detail':data}
	return render(request,'indiastatewise.html',param)

def countrywise(request):
	data = Coronavirus_Cases.corona_country_wise()
	param = {"detail":data}
	return render (request,'countrywise.html',param)

def indiadistrictwise(request,city):
	data = Coronavirus_Cases.corona_in_india_districtwise(city)
	param = {"detail":data}
	return render (request,'indiadistrictwise.html',param)

def contactus(request):
	return render(request,'contactus.html')

def map(request):
	return render(request,"map.html")

def graph(request):
	case = Coronavirus_Cases.TotalCasesGraph()
	Deathcases = Coronavirus_Cases.TotalDeathsGraph()
	total_cases = case[0]
	countries = case[1]
	total_cases.reverse()
	countries.reverse()
	tc = [int(b) for b in total_cases]
	col=['r','g','b','y','c']
	a=np.arange(len(countries[185:]))
	plt.bar(a,tc[185:],color=col,edgecolor='black')
	plt.xlabel('Countries')
	plt.title('Graph')
	plt.ylabel('Total Cases')
	plt.legend(col,countries[185:],loc=1,ncol=10,borderpad=1,shadow=True,framealpha=1,frameon=True,)
	plt.xticks(a,countries[185:],rotation=50,fontsize=8)
	#plt.savefig('D:\\Coronavirus-COVID-19-Tracker\\App\\static\\images\\photo.png')
	return render(request,"graphrepresentation.html")

def population(request):
	popu = Coronavirus_Cases.worldPopulation()
	param = {"detail":popu}
	return render(request,'population.html',param)

def futurecases(request):
	if request.method == 'POST':
		countryName = request.POST.get('countryname')
		country = countryName.capitalize()
		data = Coronavirus_Cases.possible_future_cases(country)
		param = {"detail":data}
		return render(request,"possiblefuturecases.html",param)
	return render(request,"possiblefuturecases.html")

def graph2(request):
	if request.method == 'POST':
		countryName = request.POST.get('countryname')
		country = countryName.capitalize()
		case = Coronavirus_Cases.WeeklyWiseGraph(country)
		total_cases = case[1]
		dates = case[0]
		dta = {'dates':dates,'total_cases':total_cases}
		df = pd.DataFrame(dta)
		g = sns.lineplot(x='dates', y='total_cases', data=df)
		g.set_title('Weekly Cases graph')
		plt.setp(g.get_xticklabels(), rotation=30)
		#g.figure.savefig("D:\\Coronavirus-COVID-19-Tracker\\App\\static\\images\\Weekly_Graph.png")
		return render(request,"graphrepresentation2.html")
	return render(request,"graphrepresentation2.html")

def graph3(request):
	if request.method == 'POST':
		countryName = request.POST.get('countryname')
		country = countryName.capitalize()
		case = Coronavirus_Cases.MonthlyWiseGraph(country)
		total_cases = case[1]
		dates = case[0]
		dta = {'dates':dates,'total_cases':total_cases}
		df = pd.DataFrame(dta)
		g = sns.lineplot(x='dates', y='total_cases', data=df)
		g.set_title('Monthly Cases graph')
		plt.setp(g.get_xticklabels(), rotation=45)
		#g.figure.savefig("D:\\Coronavirus-COVID-19-Tracker\\App\\static\\images\\Monthly_Graph.png")
		return render(request,"graphrepresentation3.html")
	return render(request,"graphrepresentation3.html")

def graph4(request):
	if request.method == 'POST':
		countryName = request.POST.get('countryname')
		country = countryName.capitalize()
		case = Coronavirus_Cases.YearlyWiseGraph(country)
		total_cases = case[1]
		dates = case[0]
		dta = {'dates':dates,'total_cases':total_cases}
		df = pd.DataFrame(dta)
		g = sns.lineplot(x='dates', y='total_cases', data=df)
		g.set_title('Yearly Cases graph')
		plt.setp(g.get_xticklabels(), rotation=45)
		#g.figure.savefig("D:\\Coronavirus-COVID-19-Tracker\\App\\static\\images\\Yearly_Graph.png")
		return render(request,"graphrepresentation4.html")
	return render(request,"graphrepresentation4.html")

def graph5(request):
	if request.method == 'POST':
		countryName = request.POST.get('countryname')
		country = countryName.capitalize()
		case = Coronavirus_Cases.DayWiseGraph(country)
		total_cases = case[1]
		time = case[0]
		date = case[2]
		dta = {'times':time,'total_cases':total_cases}
		df = pd.DataFrame(dta)
		g = sns.lineplot(x='times', y='total_cases', data=df)
		g.set_title('Day Cases graph')
		plt.setp(g.get_xticklabels(), rotation=45)
		#g.figure.savefig("D:\\Coronavirus-COVID-19-Tracker\\App\\static\\images\\Day_Graph.png")
		param = {'date':date[0]}
		return render(request,"graphrepresentation5.html",param)
	return render(request,"graphrepresentation5.html")