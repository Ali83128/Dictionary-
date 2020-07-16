import json
from difflib import get_close_matches
data=json.load(open('data.json'))

def translate(word):
	if word in data:
		return data[word]
	elif word.lower() in data:
		return data[word.lower()]
	elif word.upper() in data:
		return data[word.upper()]
	elif word.title() in data:
		return data[word.title()]
	elif  get_close_matches(word,data.keys()):
		print("Do you mean %s "%get_close_matches(word,data.keys())[0])
		decide=input("Press Y for Yes and N for No\n")
		if decide=='y':
			return data[get_close_matches(word,data.keys())[0]]
		elif decide=='Y':
			return data[get_close_matches(word, data.keys())[0]]
		elif decide=='N':
			return("Nothing Found")

		elif decide=='n':

			return("Nothing found")

		else:
			return("You didn't press Y or N \n")


	else:
		print("No Search Found")



word=input("Enter something you want to search \n ")
x=translate(word)
if type(x)==list:
	for s in x:
		print(s)
else:
	print(x)



