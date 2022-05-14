url = "http://www.google.com"
city = "tpe"
type = "school"
print(url + "&city=" + city + "&type=" + type)
# below is the better way
print("{}?city={}&type={}".format(url,city,type))