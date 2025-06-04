# import requests
#
# url = "https://instagram-scraper-20252.p.rapidapi.com/v1.2/posts"
#
# querystring = {"username_or_id_or_url":"watchstyle_uz"}
#
# headers = {
#   "x-rapidapi-key": "22bbcfaf16msh6ff33c352478181p1d164djsn67b305c8fc5d",
#   "x-rapidapi-host": "instagram-scraper-20252.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

# followers

# import requests
#
# url = "https://instagram-scraper-20252.p.rapidapi.com/v1/followers"
#
# querystring = {"username_or_id_or_url":"watchstyle_uz"}
#
# headers = {
# 	"x-rapidapi-key": "7ad5068454mshaed8c5eb11195d4p11cd3ajsn16881094d120",
# 	"x-rapidapi-host": "instagram-scraper-20252.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())


# reels
import requests

url = "https://instagram-scraper-20252.p.rapidapi.com/v1.2/reels"

querystring = {"username_or_id_or_url":"watchstyle_uz"}

headers = {
	"x-rapidapi-key": "7ad5068454mshaed8c5eb11195d4p11cd3ajsn16881094d120",
	"x-rapidapi-host": "instagram-scraper-20252.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())