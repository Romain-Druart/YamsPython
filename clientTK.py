try:
    from client import Client
    import tkinter as tk               
    from tkinter import scrolledtext 
except ImportError :  
  print("exception in importing module")

class ClientApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageMain):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def setTextView(self, textView):
        self.textView= textView

    def connectClient(self, username, server, port):
        self.client= ClientSocket(username, server, int(port), self.callBackMessage)
        self.client.listen()

    def callBackMessage(self, message):
        self.textView.config(state="normal") 
        self.textView.insert(tk.INSERT, message+"\n")
        self.textView.config(state="disabled") 

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Messagerie config:"); label.grid(row = 0, column = 0)
        l1 = tk.Label(self, text = "username:"); l1.grid(row = 1, column = 0)
        l2 = tk.Label(self, text = "server:"); l2.grid(row = 2, column = 0)
        l3 = tk.Label(self, text = "port:"); l3.grid(row = 3, column = 0)
        
        self.entryUsername = tk.Entry(self)
        self.entryUsername.grid(row = 1, column = 1)
        self.entryServer = tk.Entry(self)
        self.entryServer.grid(row = 2, column = 1)
        self.entryPort = tk.Entry(self)
        self.entryPort.grid(row = 3, column = 1)
        button = tk.Button(self, text="validate", command=self.validateConfig)
        button.grid(row = 4, column = 0, columnspan=2)
        
    def validateConfig(self):
        self.controller.connectClient(self.entryUsername.get(), self.entryServer.get(), self.entryPort.get())
        self.controller.show_frame("PageMain")


class PageMain(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Go back", command=self.goBack)
        button.grid(row = 0, column = 0, sticky="e", columnspan=2)

        textes = scrolledtext.ScrolledText(self, wrap = tk.WORD, width = 40,height = 10)
        textes.insert(tk.INSERT, "Welcome!\n")
        textes.config(state="disabled")
        textes.grid(row = 1, column = 0, columnspan=2)
        controller.setTextView(textes)  

        self.entryMessage= tk.Entry(self)
        self.entryMessage.grid(row = 2, column = 0, sticky="e")

        buttonSend= tk.Button(self, text="send", command=self.sendMessage)
        buttonSend.grid(row = 2, column = 1, sticky="w")
    
    def goBack(self):
        self.controller.client.send("QUIT")
        self.controller.show_frame("StartPage")

    def sendMessage(self):
        self.controller.client.send(self.entryMessage.get())
        self.entryMessage.delete(0, tk.END)
        
class ClientSocket(Client):

    def __init__(self, username, server, port, callback):
        super(ClientSocket,self).__init__(username, server, port)
        self.callback=callback

    def handle_msg(self, data):
        if data=="QUIT":
            self.tidy_up()
        elif data=="":
            self.tidy_up()
        else:
            self.callback(data)



if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()