from django.shortcuts import render
from django.http import HttpResponse
#from App import Coronavirus_Cases
# Create your views here.

def index(request):
	'''case = Coronavirus_Cases.corona()
				confirmed = case[0]
				death = case[1]
				recovered = case[2]
				newcases = case[3]
				newdeaths = case[4]'''
	confirmed = 2356
	death = 7326
	recovered = 82
	newcases = 722
	newdeaths = 762
	casedetail = {'confirmed':confirmed,'death':death,'recovered':recovered,'newcases':newcases,'newdeaths':newdeaths}
	return render (request,'index.html',casedetail)