'''
for countdown in 5,4,3,2,1, "hey!":
    print(countdown)
cliches=[
    "At the end of the day",
    "Having said that",
    "The fact of the matter is",
    "Be that as it may",
    "The bottom line is",
    "If you will",
]
print(cliches[3])
quotes = {
    "Moe": "A wise guy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk Nyuk!",
}
stooge = "Curly"
print(stooge,"says:",quotes[stooge])
'''
#This code does not work
'''
import webbrowser
import requests

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
'''
