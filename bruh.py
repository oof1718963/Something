from tkinter import *
from simplecrypt import encrypt, decrypt
from tkinter import filedialog as fd 
import os

root = Tk()
root.geometry("750x700")
root.configure(bg="#2F52E0")

file_name_entry = ''
encryption_text_data = ''
decryption_text_data = ''

def saveData():
    global file_name_entry
    global encryption_text_data
    file_name = file_name_entry.get()
    file = open(file_name + ".txt","w")
    data = encryption_text_data.get(1.0,END)
    
    ciphercode = encrypt('AIM',data)
    hex_data = ciphercode.hex()
    print(hex_data)
    
    file.write(hex_data)
    file_name_entry.delete(0,END)
    encryption_text_data.delete(1.0,END)
    messagebox.showinfo("Success!","Data is updated!")
    
def viewData():
    global decryption_text_data
    textFile = fd.askopenfilename(title="Open Text File", filetypes=(("Text Files","*.txt"),))
    name = os.path.basename(textFile)
    print(name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    byte_str = bytes.fromhex(paragraph)
    original = decrypt('AIM',byte_str)
    final_msg = original.decode("utf-8")
    decryption_text_data.insert(END,final_msg)
    text_file.close()

def start_encryption():
    global file_name_entry
    global encryption_text_data
    root.destroy()
    
    encryptionWindow = Tk()
    encryptionWindow.geometry("500x500")
    encryptionWindow.configure(bg="black")
    
    file_name_label = Label(encryptionWindow, text="File Name: ",font=("SF Pro display",9,"bold"),bg="#2F52E0",fg="black")
    file_name_label.place(relx=0.1,rely=0.15,anchor=CENTER)
    
    file_name_entry = Entry(encryptionWindow,font=("SF Pro display",9),fg="black")
    file_name_entry.place(relx=0.35,rely=0.15,anchor=CENTER)
    
    create_button = Button(encryptionWindow,text="Create",font=("SF pro display",9,"bold"),bg="##2F52E0",fg="black",relief=FLAT,command=saveData)
    create_button.place(relx=0.8,rely=0.15,anchor=CENTER)
    
    encryption_text_data = Text(encryptionWindow,width=75,height=22,relief=FLAT,bg="#2F52E0",fg="black",font=("sf pro display",9,"bold","italic"))
    encryption_text_data.place(relx=0.5,rely=0.6,anchor=CENTER)
    
    encryptionWindow.mainloop()
    
def start_decryption():
    global file_name_entry
    global decryption_text_data
    root.destroy()
    
    decryptionWindow = Tk()
    decryptionWindow.geometry("500x500")
    decryptionWindow.configure(bg="orange")
    
    decryption_text_data = Text(decryptionWindow,width=75,height=22,relief=FLAT,bg="#2F52E0",fg="black",font=("SF Pro display",12,"bold","italic"))
    decryption_text_data.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    openFileButton = Button(decryptionWindow,text="Choose File....",bg="#2F52E0",fg="black",relief=FLAT,font=("sf pro display",20,"bold"),command=viewData)
    openFileButton.place(relx=0.5,rely=0.8,anchor=CENTER)
    
heading_label = Label(root,text="new and simple",bg="#2F52E0",fg="black",font=("sf pro display",25,"bold"))
heading_label.place(relx=0.5,rely=0.2,anchor=CENTER)

encryption_btn = Button(root,text="Encryption",relief=FLAT,bg="#2F52E0",fg="black",font=("sf pro display",20,"bold"),command=start_encryption)
encryption_btn.place(relx=0.4,rely=0.5,anchor=CENTER)

decryption_btn = Button(root,text="Decryption",relief=FLAT,bg="#2F52E0",fg="black",font=("sf pro display",20,"bold"),command=start_decryption)
decryption_btn.place(relx=0.6,rely=0.5,anchor=CENTER)

root.mainloop()
