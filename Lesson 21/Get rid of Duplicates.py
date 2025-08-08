studentdata = {
    "ID-1":{
        "Name" : "Aanya",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-2":{
        "Name" : "Aaradhay",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-3":{
        "Name" : "Aarav",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-4":{
        "Name" : "Aarya",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-5":{
        "Name" : "Aadhyan",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-6":{
        "Name" : "Aman",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-7":{
        "Name" : "Anishka",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-67":{
        "Name" : "Aarav",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-8":{
        "Name" : "Anjali",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-9":{
        "Name" : "Akansha",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-10":{
        "Name" : "Archit",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-19":{
        "Name" : "Aanya",
        "Class" : 8,
        "Subject" : ["Maths"]
    },
    "ID-14":{
        "Name" : "Aman",
        "Class" : 8,
        "Subject" : ["Maths"]
    }
}

result = {}
for key,value in studentdata.items():
    if value not in result.values():
        result[key] = value

print(result)