import json
import datetime

def save():
    with open("library.json", "w+", encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False))


def load():
    try:
        with open("library.json", "r", encoding="utf-8") as file:
            data = json.load(file) 
            return data
    except:
        data = {"notes":[{"id":1, "note":"first note", "date":"12.03.2022"}, {"id":2, "note":"second note", "date":"12.03.2022"}]}
        return data
        save()

data=load()
def addNote(id, note, date):
    newnote={"id": id, "note":note, "date":date}
    data['notes'].append(newnote)
    print(data)

def edit(id, newNote):
        dataNotes = data["notes"]
        for n in dataNotes:
            if(n["id"]==id):                    
                n['note'] = newNote
                n['date'] = str(datetime.datetime.now())
        save()
        print(data)

def deleteNote(id):
    dataNotes = data["notes"]
    index=0
    while index<len(dataNotes):                
        if(dataNotes[index]["id"]==id):
            del dataNotes[index]
            break
        index=index+1
    save()
    print(data)        

def showAll():
    print(data)