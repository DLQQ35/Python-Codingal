import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "I am"    :  "you are",
    "I was"   :  "you were",
    "I"       :  "you",
    "I'm"     :  "you're",
    "I'd"     :  "you would",
    "I've"    :  "you have",
    "I'll"    :  "you will",
    "my"      :  "your",
    "You are" :  "I am",
    "You were":  "I was",
    "You've"  :  "I have",
    "You'll"  :  "I will",
    "Your"    :  "My",
    "Yours"   :  "Mine",
    "You"     :  "Me",
    "Me"      :  "You"
}

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"Hi|Hey|Hello",
        ["Hello", "Hey there",]
    ],
    [
        r"What is your name ?",
        ["I am a chatbot created by Codingal. You can call me Jarvis.",]
    ],
    [
        r"How are you ?",
        ["I'm doing good. How about you ?",]
    ],
    [
        r"Sorry (.*)",
        ["Its alright", "No problem","It's OK", "Nevermind",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"I am doing good",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"(*) age?",
        ["I'm a computer program dude, so I don't have an age.",]
    ],
    [
        r"What (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I was created by Codingal.","TOP SECRET ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am based on the cloud.',]
    ],
    [
        r"How is the weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot here in %1", "Too cold here in %1", "Never even heard about %1"]
    ],
    [
        r"I work in (.*)?",
        ["%1 is an amazing company, I have heard about it.", "I have heard about %1, but I don't know much about it.", "I don't know anything about %1."]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in %2", "Damn it's raining in %2", "It's perfect weather in %2"]
    ],
    [
        r"How (.*) health(.*)?",
        ["Health is very important, but I am a computer program, so I don't have health.", "I'm a computer program dude, SERIOUSLY.","You are making me feel the FOMO",]
    ],
    [
        r"(.*)(sports|game|sportsperson|athlete)?",
        ["I'm a very big fan of Football", "I'm a very big fan of Cricket", "I'm a very big fan of Basketball"]
    ],
    [
        r"Who (.*) sportsperson ?",
        ["Messi", "Ronaldo", "Neymar"]
    ],
    [
        r"Who (.*) (moviestar|actor)?",
        ["Brad Pitt", "Leonardo DiCaprio", "Tom Cruise"]
    ],
    [
        r"I am looking for online guides and courses to learn data science, can you suggest?",
        ["Jarvis_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ]
]

def chat():
    print("Hi! I'm Jarvis and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()