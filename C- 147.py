from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = "snow")

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name is Ascii : ", bg="light yellow", fg="black")
label_2 = Label(root, text = "Encrypted Name : ", bg="light blue", fg="black") 

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) +" "
        
def encryptedName():
    encrypted = ascii - 1
    
    label_2["text"] += str(chr(encrypted))
        

btn=Button(root, text="Show name in Ascii",command=asciiConverter, bg='gold', fg='black')        
btn.place(relx=0.5, rely=0.5,anchor=CENTER)

btn=Button(root, text="Show name in Encrypted name",command=encryptedName, bg='red', fg='black')
btn.place(relx=0.5, rely=0.7,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label_2.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()

