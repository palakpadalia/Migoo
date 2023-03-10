import requests

url = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"

querystring = {"agencies":"12,16","routes":"4000421,4000592,4005122","geo_area":"35.80176,-78.64347|35.78061,-78.68218","callback":"call"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "transloc-api-1-2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)