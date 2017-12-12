from chatbot import Chat, reflections, multiFunctionCall
import urllib.parse
import urllib.request, re
from bs4 import BeautifulSoup

pairs = [
  ("(Show recently|Show recent|Display recent|Show) (.*)",
  ("{% call StackOver:%2 %}",))
]

def StackOver(search,sessionID="general"):
    types='' #for asking  question is not answered or questions
    view = '' #for recently question
    tag=''  #tag of url
    domain=''  #ypur domain like :- python, java etc.
    number = ''.join(x for x in search if x.isdigit()) # find number in questions

    if not number:
        number=5
    else:
        number = int(number)

    #tag for newwst or recent questions
    if 'recently' or 'recent' in search:
        view='newest'

    #for questions
    if 'questions' or 'question' in search:
        types='questions'
        tag='sort'

    # for not answered questions
    if 'not answered' in search:
        types='unanswered'
        tag='tab'

    # tag of domain
    if 'python' in search:
        domain='python'
    elif 'java' in search:
        domain='java'
    elif 'ace' in search:
        domain='ace'


    # to make url of your given question
    url = 'https://stackoverflow.com'+'/'+types+'/tagged' + '/' + domain

    #key of question
    key = {tag: view,
                 'pageSize': 15
               }

    # to concatenate with url and values(key)
    data = urllib.parse.urlencode(key)
    data = data.encode('utf-8')
    request  = urllib.request.Request(url, data)
    respounce = urllib.request.urlopen(url)
    respdata = respounce.read()


    #beautifulsoup
    soup = BeautifulSoup(respdata)
    c=1
    for hr in soup.find_all("h3")[3:number+3]:
        print("Question No:- %s "%(c), hr.text)
        c+=1
    return ''


call = multiFunctionCall({"StackOver":StackOver})
firstQuestion="Hi, how are you?"
Chat(pairs, reflections,call=call).converse(firstQuestion)
