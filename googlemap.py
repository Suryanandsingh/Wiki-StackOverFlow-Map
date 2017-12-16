import googlemaps
from chatbot import Chat, reflections, multiFunctionCall

pairs=[
    ("(what is distance between|what is distance from|what is distance|direction from)(.*)",
    ("{% call Maps:%2 %}",))
]
gmaps = googlemaps.Client(key='AIzaSyDqJydghURg-1nNGI957AH7qTNIoZs2MCY')

def Maps(query, sessionID='general'):
    query = query.split('to')
    firstdirection = query[0]
    seconddirection = query[1]
    dirs = gmaps.directions(firstdirection, seconddirection)
    dirs = dirs[0]
    dirs = dirs['legs']
    dirs = dirs[0]
    print("Distance :- " + dirs['distance']['text'])
    print("start address : "+ dirs['start_address'])
    print("end address : "+ dirs['end_address'])
    return ''

call = multiFunctionCall({"Maps":Maps})

firstQuestion="Hi, how are you?"
Chat(pairs, reflections, call=call).converse(firstQuestion)
