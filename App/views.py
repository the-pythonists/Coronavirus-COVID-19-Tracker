from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from App import worldData,indiaData
from django.http import JsonResponse
import requests,json


def index(request):
	return HttpResponseRedirect('/map/india')

def map(request,m):
	covidCases = worldData.data()
	data = covidCases['cases']
	worldList = ['country','totalCases','deaths','recovered']
	cases = []
	for j in data:
		k = [j[i] for i in worldList if i in j]
		cases.append(k)
		# print(len(cases))
	worldCases = cases[4]
	
	if m == 'india':
		indiaList = ['state','confirmed','active','recovered','deaths']
		cases1 = []
		indCases =indiaData.data()
		for p in indCases:
			r = [p[q] for q in indiaList if q in p]
			cases1.append(r)

		totalCases = cases1[0]
		totalConfirmed = totalCases[1]
		totalActive = totalCases[2]
		totalRecovered = totalCases[3]
		totalDead = totalCases[4]
		stateCases = cases1[1:]
	    # print(indiaCases)
		params = {"cases":cases[4:217],"total":worldCases[1],"dead":worldCases[2],
	    "recover":worldCases[3],"stateCases":stateCases,"totalCases":totalCases,
	    "totalConfirmed":totalConfirmed,"totalActive":totalActive,"totalRecovered":totalRecovered,
	    "totalDead":totalDead}
		return render(request,'india.html',params)
	
	elif m == 'world':
		indCases =indiaData.data()
		
		params = {"cases":cases[4:217],"total":worldCases[1],"dead":worldCases[2],"recover":worldCases[3]}

		return render(request,'worldmap.html',params)
	else:
		return HttpResponseRedirect('/')
	# return render(request,"map.html")

def worlddata(request):
	global covidCases
	covidCases = worldData.data()
	response = JsonResponse(covidCases)
	# print(covidCases)
	return HttpResponse(response)

def graphOne(request):
	global result
	'''url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
				headers = {
				    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
				    'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
				    }
				response = requests.request("GET", url, headers=headers)
				x = response.json()
				data = x["countries_stat"]
				worldList = ['country_name','cases','deaths','total_recovered','total_tests']
				countries = []; cases = []; deaths = []; total_recovered = []; total_tests = []
				for i in data:
					countries.append(i['country_name'])
					cases.append(i['cases'])
					deaths.append(i['deaths'])
					total_recovered.append(i['total_recovered'])
					total_tests.append(i['total_tests'])
				params = {"countries":countries,"cases":cases}
				result = json.dumps(params)'''
	countries =  ["USA", "Spain", "Italy", "France", "Germany", "UK", "Turkey", "Iran", "China", "Russia", "Brazil", "Belgium", "Canada", "Netherlands", "Switzerland", "Portugal", "India", "Peru", "Sweden", "Ireland", "Austria", "Israel", "Saudi Arabia", "Japan", "Chile", "Singapore", "Ecuador", "S. Korea", "Mexico", "Pakistan", "Poland", "Romania", "UAE", "Denmark", "Indonesia", "Qatar", "Norway", "Belarus", "Ukraine", "Czechia", "Serbia", "Philippines", "Australia", "Malaysia", "Dominican Republic", "Panama", "Colombia", "Finland", "Bangladesh", "Egypt", "Luxembourg", "South Africa", "Morocco", "Argentina", "Algeria", "Thailand", "Moldova", "Greece", "Kuwait", "Hungary", "Kazakhstan", "Bahrain", "Croatia", "Iceland", "Oman", "Uzbekistan", "Iraq", "Estonia", "Azerbaijan", "Armenia", "New Zealand", "Bosnia and Herzegovina", "Lithuania", "Slovenia", "Slovakia", "North Macedonia", "Afghanistan", "Cuba", "Cameroon", "Ghana", "Bulgaria", "Hong Kong", "Djibouti", "Ivory Coast", "Tunisia", "Nigeria", "Cyprus", "Latvia", "Guinea", "Andorra", "", "Diamond Princess", "Lebanon", "Costa Rica", "Bolivia", "Albania", "Niger", "Kyrgyzstan", "Burkina Faso", "Uruguay", "Honduras", "Channel Islands", "San Marino", "Palestine", "Senegal", "Malta", "Jordan", "Taiwan", "Georgia", "R\u00e9union", "DRC", "Guatemala", "Sri Lanka", "Mauritius", "Mayotte", "Montenegro", "Isle of Man", "Kenya", "Venezuela", "Mali", "Somalia", "Tanzania", "Vietnam", "Jamaica", "El Salvador", "Paraguay", "Faeroe Islands", "Congo", "Gabon", "Martinique", "Sudan", "Rwanda", "Guadeloupe", "Brunei", "Gibraltar", "Myanmar", "Cambodia", "Madagascar", "Ethiopia", "Trinidad and Tobago", "French Guiana", "Liberia", "Aruba", "Bermuda", "Monaco", "Maldives", "Togo", "Equatorial Guinea", "Cabo Verde", "Liechtenstein", "Barbados", "Zambia", "Sint Maarten", "Bahamas", "Guyana", "Cayman Islands", "Uganda", "Haiti", "Sierra Leone", "Libya", "French Polynesia", "Benin", "Guinea-Bissau", "Nepal", "Macao", "Syria", "Mozambique", "Eritrea", "Saint Martin", "Mongolia", "Malawi", "Chad", "Eswatini", "Zimbabwe", "Angola", "Antigua and Barbuda", "Timor-Leste", "Botswana", "Laos", "Belize", "Fiji", "New Caledonia", "Dominica", "Namibia", "Grenada", "Saint Lucia", "Saint Kitts and Nevis", "Cura\u00e7ao", "CAR", "St. Vincent Grenadines", "Falkland Islands", "Turks and Caicos", "Greenland", "Montserrat", "Seychelles", "Burundi", "Nicaragua", "Gambia", "Suriname", "Vatican City", "MS Zaandam", "Papua New Guinea", "Bhutan", "Mauritania", "St. Barth", "Western Sahara", "British Virgin Islands", "Caribbean Netherlands", "Sao Tome and Principe", "South Sudan", "Anguilla", "Saint Pierre Miquelon", "Yemen"]
	cases =  ["851193", "213024", "187327", "159877", "151175", "138078", "98674", "87026", "82798", "62773", "46348", "42797", "40190", "35729", "28496", "22353", "21797", "19250", "16755", "16671", "15002", "14592", "13930", "11950", "11296", "11178", "10850", "10811", "10702", "10544", "10346", "10096", "8756", "8073", "8022", "7775", "7764", "7361", "7276", "7170", "7136", "6981", "6661", "5603", "5300", "4992", "4356", "4284", "4186", "3659", "3654", "3635", "3537", "3288", "2926", "2910", "2839", "2408", "2399", "2284", "2251", "2098", "1981", "1789", "1735", "1716", "1631", "1592", "1548", "1523", "1451", "1413", "1398", "1366", "1325", "1300", "1279", "1189", "1163", "1154", "1097", "1036", "986", "952", "909", "873", "790", "778", "761", "723", "721", "712", "688", "681", "672", "663", "662", "631", "609", "549", "519", "519", "501", "480", "479", "445", "435", "427", "420", "410", "377", "342", "337", "329", "326", "320", "316", "307", "298", "293", "286", "284", "268", "252", "250", "213", "187", "186", "166", "164", "162", "153", "148", "138", "132", "132", "122", "121", "116", "115", "107", "101", "100", "99", "94", "94", "88", "84", "82", "81", "76", "74", "73", "70", "67", "66", "63", "62", "61", "60", "57", "54", "50", "47", "45", "42", "41", "39", "38", "35", "33", "33", "31", "28", "25", "24", "23", "22", "19", "18", "18", "18", "16", "16", "15", "15", "15", "14", "14", "13", "12", "11", "11", "11", "11", "11", "10", "10", "10", "9", "9", "8", "7", "7", "6", "6", "5", "5", "4", "4", "3", "1", "1"]
	td = [int(b) for b in cases]
	result = {"countries": countries[:10],"cases":td[:10]}
	return HttpResponse(json.dumps(result))

def graphTwo(request):
	global result
	'''url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
				headers = {
				    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
				    'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
				    }
			
				response = requests.request("GET", url, headers=headers)
				x = response.json()
				y = x['state_wise']
				confirmed = []; state = []
				for i in y.values():
				    stateName = i['state']
				    confirmedCases = i['confirmed']
				    state.append(stateName)
				    confirmed.append(confirmedCases)
				td = [int(b) for b in confirmed]
				params = {"states":state,"confirmedCases":td}
				result = json.dumps(params)'''
	state =  ["Maharashtra", "Gujarat", "Delhi", "Rajasthan", "Madhya Pradesh", "Tamil Nadu", "Uttar Pradesh", "Telangana", "Andhra Pradesh", "West Bengal", "Kerala", "Karnataka", "Jammu and Kashmir", "Punjab", "Haryana", "Bihar", "Odisha", "Jharkhand", "Uttarakhand", "Himachal Pradesh", "Chhattisgarh", "Assam", "Chandigarh", "Andaman and Nicobar Islands", "Ladakh", "Meghalaya", "Puducherry", "Goa", "Manipur", "Tripura", "Mizoram", "Arunachal Pradesh", "Nagaland", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Sikkim"]
	confirmed = [6427, 2624, 2376, 2000, 1687, 1683, 1510, 970, 893, 514, 447, 445, 434, 283, 270, 176, 90, 53, 47, 40, 36, 36, 27, 22, 18, 12, 7, 7, 2, 2, 1, 1, 0, 0, 0, 0, 0]
	result = {"states":state,"confirmedCases":confirmed}
	return HttpResponse(json.dumps(result))

def graphThree(request):
	'''url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
				headers = {
				    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
				    'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
				    }
				response = requests.request("GET", url, headers=headers)
				x = response.json()
				y = x['state_wise']
				recovered = []; state = []
				for i in y.values():
				    stateName = i['state']
				    recoveredCases = i['recovered']
				    state.append(stateName)
				    recovered.append(recoveredCases)
				td = [int(b) for b in recovered]
				params = {"states":state,"recovered":td}
				result = json.dumps(params)'''
	state = ["Maharashtra", "Gujarat", "Delhi", "Rajasthan", "Madhya Pradesh", "Tamil Nadu", "Uttar Pradesh", "Telangana", "Andhra Pradesh", "West Bengal", "Kerala", "Karnataka", "Jammu and Kashmir", "Punjab", "Haryana", "Bihar", "Odisha", "Jharkhand", "Uttarakhand", "Himachal Pradesh", "Chhattisgarh", "Assam", "Chandigarh", "Andaman and Nicobar Islands", "Ladakh", "Meghalaya", "Puducherry", "Goa", "Manipur", "Tripura", "Mizoram", "Arunachal Pradesh", "Nagaland", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Sikkim"]
	recovered = [957, 265, 808, 473, 210, 866, 226, 252, 145, 103, 152, 109, 331, 70, 186, 44, 33, 8, 25, 18, 30, 19, 15, 11, 16, 0, 4, 7, 2, 2, 0, 1, 0, 0, 0, 0, 0]
	result = {"states":state,"recovered":recovered}
	return HttpResponse(json.dumps(result))

def graphFour(request):
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
	headers = {
	    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
	    'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
	    }
	response = requests.request("GET", url, headers=headers)
	x = response.json()
	y = x['state_wise']
	active = []; state = []
	for i in y.values():
	    stateName = i['state']
	    activeCases = i['recovered']
	    state.append(stateName)
	    active.append(activeCases)
	td = [int(b) for b in active]
	params = {"states":state,"active":td}
	result = json.dumps(params)
	return HttpResponse(result)

def graphFive(request):
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
	headers = {
	    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
	    'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
	    }
	response = requests.request("GET", url, headers=headers)
	x = response.json()
	y = x['state_wise']
	dead = []; state = []
	for i in y.values():
	    stateName = i['state']
	    deathCases = i['deaths']
	    state.append(stateName)
	    dead.append(deathCases)
	td = [int(b) for b in dead]
	params = {"states":state,"deaths":td}
	result = json.dumps(params)
	return HttpResponse(result)

def globe(request):
	return render(request,"globe.html")

def Sort(allData): 
    allData.sort(key = lambda i: i["country_name"]) 
    return allData 

def globe_data(request):
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
	headers = {
		'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
		'x-rapidapi-key': "8a535ee783mshca57265aad44eb9p18617fjsnce3f1f61eb7c"
		}
	response = requests.request("GET", url, headers=headers)
	x = response.json()
	allData = x['countries_stat']
	countrywiseSort = Sort(allData)
	RemainingData = countrywiseSort[1:]
	confirmed = []; active = []; recovered = []; dead = []; states = []
	for k in RemainingData:
		statesName = k['country_name']
		confirmedCases = k['cases'].replace(",","")
		activeCases = k['active_cases'].replace(",","")
		recoveredCases = k['total_recovered'].replace(",","")
		deathCases = k['deaths'].replace(",","")
		states.append(statesName)
		confirmed.append(confirmedCases)
		active.append(activeCases)
		recovered.append(recoveredCases)
		dead.append(deathCases)
	con = [int(p) for p in confirmed]
	act = [int(q) for q in active]
	#rec = [int(r) for r in recovered]
	dea = [int(s) for s in dead]
	countries_iso = ["AF","AL","DZ","AD","AO","AI","AG","AR","AM","AW","AU","AT","AZ","BS","BH","BD","BB","BY","BE","BZ","BJ","BM","BT","BO","BA","BW","BR","VG","BN","BG","BF","BI","CF","CV","KH","CM","CA","BQ","KY","TD","GB","CL","CN","CO","CG","CR","HR","CU","CW","CY","CZ","CD","DK","DJ","DM","DO","EC","EG","SV","GQ","ER","EE","SZ","ET","FO","FK","FJ","FI","FR","GF","PF","TF","GA","GM","GE","DE","GH","GI","GR","GL","GD","GP","GT","GN","GW","GY","HT","HN","HK","HU","IS","IN","ID","IR","IQ","IE","IM","IL","IT","CI","JM","JP","JO","KZ","KE","KW","KG","LA","LV","LB","LR","LY","LI","LT","LU","","MO","MG","MW","MY","MV","ML","MT","MQ","MR","MU","YT","MX","MD","MC","MN","ME","MS","MA","MZ","MM","NA","NP","NL","NC","NZ","NI","NE","NG","MK","NO","OM","PK","PS","PA","PG","PY","PE","PH","PL","PT","QA","RO","RU","RW","RE","KR","KN","LC","MF","PM","SM","ST","SA","SN","RS","SC","SL","SG","SX","SK","SI","SO","ZA","SS","ES","LK","BL","VC","SD","SR","SE","CH","SY","TW","TZ","TH","TL","TG","TT","TN","TR","TC","AE","GB","US","UG","UA","UY","UZ","VA","VE","VN","EH","YE","ZM","ZW"]
	confirmedList = []; activeList = []; recoveredList = []; deadList = []
	for i in range(0,len(countries_iso)):
		confirmedList.append({""+countries_iso[i]+"" : con[i]})
	for i in range(0,len(countries_iso)):
		activeList.append({""+countries_iso[i]+"" : act[i]})
	for i in range(0,len(countries_iso)):
		deadList.append({""+countries_iso[i]+"" : dea[i]})
	mergedConfirmed={}; mergeActive = {}; mergeDead = {}
	for x1 in confirmedList:
		mergedConfirmed.update(x1)
	for x2 in activeList:
		mergeActive.update(x2)
	for x3 in deadList:
		mergeDead.update(x3)
	params = {"confirmed":mergedConfirmed,"active":mergeActive,"deaths":mergeDead}
	result = json.dumps(params)
	return HttpResponse(result)

def graph(request):
	return render(request,"graphs.html")