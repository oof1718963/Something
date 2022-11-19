from tkinter import *
from simplecrypt import encrypt,decrypt
from firebase import firebase
firebase = firebase.FirebaseApplication("https://py-chat-app-58e83-default-rtdb.firebaseio.com/",None)

login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='#AB92BF')

username=""
yourcode=""
friendcode=""
message_text=""
message_entry=""
last_value=""
def getdata():
    global last_value
    global yourcode
    global message_text
    global friendcode
    getyourdata=firebase.get("/",yourcode)
    print(getyourdata)
    byte_str=bytes.fromhex(getyourdata)
    original=decrypt("message",byte_str)
    print(original)
    finalmessage=original.decode("utf_8")
    message_text.insert(END,finalmessage+"\n")
    getyourfrienddata=firebase.get("/",friendcode)
    if (getyourfrienddata != None):
        byte_str=bytes.fromhex(getyourfrienddata)
        original=decrypt("message",byte_str)
        finalmessage=original.decode("utf_8")
        if (finalmessage not in lastvalue): 
            message.text.insert(finalmessage+"\n")
            last_value=final_message
        
        
        
        
def senddata():
    global username
    global yourcode
    global message_entry
    message=username+":"+message_entry.get()
    ciphertext=encrypt("message",message)
    hexstring=ciphertext.hex()
    print(hexstring)
    put_date=firebase.put("/",yourcode,hexstring)
    getdata()
def enterRoom():
    
    global username
    global yourcode
    global friendcode
    global message_text
    global message_entry
    username = username_entry.get()
    yourcode = your_code_entry.get()
    friendcode = friends_code_entry.get()
    login_window.destroy()
    
    message_window = Tk()
    message_window.config(bg='#AFC1D6')
    message_window.geometry("600x500")
    
    message_text = Text(message_window, height=20, width=72)
    message_text.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    
    message_label = Label(message_window, text="Message " , font = 'arial 13', bg='#AFC1D6', fg="white")
    message_label.place(relx=0.3,rely=0.8, anchor=CENTER)
    
    message_entry = Entry(message_window, font = 'arial 15')
    message_entry.place(relx=0.6,rely=0.8, anchor=CENTER)
    
    btn_send = Button(message_window, text="Send", font = 'arial 13', bg="#D6CA98", fg="black", padx=10, relief=FLAT,command=senddata)
    btn_send.place(relx=0.5,rely=0.9, anchor=CENTER)
    
    message_window.mainloop()
    

username_label = Label(login_window, text="Username : " , font = 'arial 13', bg ='#AB92BF', fg="white")
username_label.place(relx=0.3,rely=0.3, anchor=CENTER)

username_entry = Entry(login_window)
username_entry.place(relx=0.6,rely=0.3, anchor=CENTER)

your_code_label = Label(login_window, text="Your code :  " , font = 'arial 13', bg ='#AB92BF', fg="white")
your_code_label.place(relx=0.3,rely=0.4, anchor=CENTER)

your_code_entry = Entry(login_window)
your_code_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

friends_code_label = Label(login_window, text="Your Friends code :  " , font = 'inter', bg ='#AB92BF', fg="white")
friends_code_label.place(relx=0.22,rely=0.5, anchor=CENTER)

friends_code_entry = Entry(login_window)
friends_code_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_start = Button(login_window, text="Start" , font = 'inter' , bg="#CEF9F2", fg="black", command=enterRoom, relief=FLAT, padx=10)
btn_start.place(relx=0.5,rely=0.65, anchor=CENTER)

login_window.mainloop()
