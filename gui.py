from tkinter import *
import time
import tkinter.messagebox
from bot import chat
import pyttsx3
import threading

saved_username = ["You"]

window_size="400x400"

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#574B74"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=3)
# Menu bar

    # File

        menu.add_cascade(label="Clear", command=self.clear_chat)

        menu.add_cascade(label="Exit",command=self.chatexit)
        menu.add_command(label="About Tikku", command=self.msg)
        menu.add_command(label="Develpoers", command=self.about)


        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        # self.users_message = self.entry_field.get()

        # frame containing send button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        # send button
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='#c0c0c0',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#cccccc",
                                  activeforeground="#373737")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)
        
        self.last_sent_label(date="No messages sent.")

        

    def playResponce(self,responce):
        x=pyttsx3.init()

        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')
                #print(b)
                 
        x.setProperty('rate',120)
        x.setProperty('volume',100)
        x.say(responce)
        x.runAndWait()

        
        
    def last_sent_label(self, date):

        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("Tikku",'Tikku is a chatbot for answering python queries\nIt is based on retrival-based NLP using pythons NLTK tool-kit module\nGUI is based on Tkinter\nIt can answer ')

    def about(self):
        tkinter.messagebox.showinfo("Tikku Developers","1.Bigyan Timilsina\n2.Gurjeet Singh\n3.Aditya \n4.Sekhar ")
    
    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        pr1 = "Human : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

        ob=chat(user_input)
        pr="Tikku : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.entry_field.delete(0,END)
        time.sleep(0)
        t2 = threading.Thread(target=self.playResponce, args=(ob,))
        t2.start()
        #return ob

root=Tk()

a = ChatInterface(root)
root.geometry(window_size)
root.title("Tikku- Exam Chatbot")
root.iconbitmap('icon.ico')
root.mainloop()
