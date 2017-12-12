# from chatbot import Chat,reflections,multiFunctionCall
import wikipedia
from chatbot import Chat, reflections, multiFunctionCall


pairs = [
  ("(Do you know about|what is|who is|tell me about)(.*)",
  ("{% call whoIs:%2 %}",))
]


def whoIs(query,sessionID=2):
    try:
        return wikipedia.summary(query)
    except:
        for newquery in wikipedia.search(query):
            try:
                return wikipedia.summary(newquery)
            except:
                pass
    return "I don't know about "+query
    

call = multiFunctionCall({"whoIs":whoIs})
firstQuestion="Hi, how are you?"
Chat(pairs, reflections,call=call).converse(firstQuestion)

