import json
from datetime import datetime,date

diary=[]
def load_data():
    global diary
    try:
        with open('diary.json','r')as f:
            diary=json.load(f)
    except FileNotFoundError:
        return
def save_data():
    with  open('diary.json','w')as f:
        json.dump(diary,f,indent=4)

def menu():
    print("Your menu is here")
    print("\n1.Add Books\n2view boooks\n3Mark book today\n4view today\n5nexit")
def add():
    print("Give correct details to add books on diary")
    name=input("enter the name of book")
    author=input("enter the name of author")
    today_date=date.today().strftime("%Y-%m-%d")
    diary.append({"name":name,"author":author,"done":False,"date":today_date})
    save_data()
    
def view_all():
    if not diary:
        print("you not add any diary")
        add()
    else:
        for i,d in enumerate(diary):
            status="✓" if d.get("done",False) else "✗"
            print(f"{i+1} {status} {d['name'] }written by{d["author"]}")
def mark_book():
    view_all()
    try:
        choice=int(input("enter the number you wanna do done"))
        if 1<=choice<=len(diary):
            diary[choice-1]['done']=True
            save_data()
            load_data()
        else:
            print("enter the valid no")
    except:
        print("enter a valid no")
load_data()
def view_today():
    today_date=date.today().strftime("%Y-%m-%d")
    today_diary=[d for d in diary if d.get("date")==today_date]
    if not today_diary:
        print("you dont have any diary ")
        add()
    else:
        print("today diary on date",today_date)
        for i,d in enumerate(today_diary):
            status= "✓" if d.get("done",False) else "✗"
            print(f"{i+1}. {status} {d['name']} written by {d['author']}")
while True:
    menu()
    try:
        choice=int(input("enter the number you wanna do action"))
        if choice==1:
            add()
        elif choice==2:
            view_all()
        elif choice==3:
            mark_book()
        elif choice==4:
            view_today()
        elif choice==5:
            print("thanks for using our app on",date.today().strftime("%Y-%m-%d"))
            break
    except ValueError:
        print("enter a valid number")


    


        

    


