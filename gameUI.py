try:
    from client import Client
    import tkinter as tk               
    from tkinter import scrolledtext, ttk, messagebox
    from PIL import Image, ImageTk
    from dices import Dice
    from gameRules import GameRules
    import random
except ImportError :  
  print("exception in importing module in gameUI")

######################## ClientApp ################################

class ClientApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GamePage):
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


######################## End ClientApp ################################

######################## StartPage ################################
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
        self.controller.show_frame("GamePage")

######################## End StartPage ################################

######################## ClientSocket ###############################

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

################## END ClientSocket ######################

##################### GAMEPAGE ###########################

class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Dice = Dice()
        self.GameRules = GameRules()
        self.dicesUI = [0,0,0,0,0]
        self.dicesNumbers = [0,0,0,0,0]
        #allow the player to choose witch dice he wants to throw
        self.isOneChecked = tk.IntVar()
        self.isTwoChecked = tk.IntVar()
        self.isThreeChecked = tk.IntVar()
        self.isFourChecked = tk.IntVar()
        self.isFiveChecked = tk.IntVar()


        #allow the player to only toss dices 3 times
        self.numberOfToss = 0

        ################### GamePageUI #####################
        #Champs d'inforamtion sur les point et le nom des joueurs
        self.label_player_name = tk.Label(self, text = "Player :"); self.label_player_name.grid(row = 1, column = 0, sticky ='w')
        self.label_one = tk.Label(self, text = "1 :"); self.label_one.grid(row = 2, column = 0, sticky ='w')
        self.label_two = tk.Label(self, text = "2 :"); self.label_two.grid(row = 3, column = 0, sticky ='w')
        self.label_three = tk.Label(self, text = "3 :"); self.label_three.grid(row = 4, column = 0, sticky ='w')
        self.label_four = tk.Label(self, text = "4 :"); self.label_four.grid(row = 5, column = 0, sticky ='w')
        self.label_five = tk.Label(self, text = "5 :"); self.label_five.grid(row = 6, column = 0, sticky ='w')
        self.label_six = tk.Label(self, text = "6 :"); self.label_six.grid(row = 7, column = 0, sticky ='w')
        self.label_top_sub_total = tk.Label(self, text = "Sous Total :"); self.label_top_sub_total.grid(row = 8, column = 0, sticky ='w')
        self.label_bonus = tk.Label(self, text = "Bonus (Si > 63pts):"); self.label_bonus.grid(row = 9, column = 0, sticky ='wn')
        self.label_brelan = tk.Label(self, text = "Brelan :"); self.label_brelan.grid(row = 10, column = 0, sticky ='w')
        self.label_carre = tk.Label(self, text = "Carre :"); self.label_carre.grid(row = 11, column = 0, sticky ='w')
        self.label_full = tk.Label(self, text = "Full :"); self.label_full.grid(row = 12, column = 0, sticky ='w')
        self.label_small_suite = tk.Label(self, text = "Petite Suite :"); self.label_small_suite.grid(row = 13, column = 0, sticky ='w')
        self.label_great_suite = tk.Label(self, text = "Grande Suite :"); self.label_great_suite.grid(row = 14, column = 0, sticky ='w')
        self.label_yams = tk.Label(self, text = "Yams :"); self.label_yams.grid(row = 15, column = 0, sticky ='w')
        self.label_chance = tk.Label(self, text = "Cahnce :"); self.label_chance.grid(row = 16, column = 0, sticky ='w')
        self.label_sub_total = tk.Label(self, text = "Sous Total :"); self.label_sub_total.grid(row = 17, column = 0, sticky ='w')
        self.label_total = tk.Label(self, text = "Total :"); self.label_total.grid(row = 18, column = 0, sticky ='w')

        # Affichage des points du joueur 1
        self.label_player1_name = tk.Label(self, text = "player1_name"); self.label_player1_name.grid(row = 1, column = 1)
        self.label_player1_one = tk.Label(self, text = "player1_one"); self.label_player1_one.grid(row = 2, column = 1)
        self.label_player1_two = tk.Label(self, text = "player1_two"); self.label_player1_two.grid(row = 3, column = 1)
        self.label_player1_three = tk.Label(self, text = "player1_three"); self.label_player1_three.grid(row = 4, column = 1)
        self.label_player1_four = tk.Label(self, text = "player1_four"); self.label_player1_four.grid(row = 5, column = 1)
        self.label_player1_five = tk.Label(self, text = "player1_five"); self.label_player1_five.grid(row = 6, column = 1)
        self.label_player1_six = tk.Label(self, text = "player1_six"); self.label_player1_six.grid(row = 7, column = 1)
        self.label_player1_top_sub_total = tk.Label(self, text = "player1_top_sub_total"); self.label_player1_top_sub_total.grid(row = 8, column = 1)
        self.label_player1_bonus = tk.Label(self, text = "player1_bonus"); self.label_player1_bonus.grid(row = 9, column = 1, sticky="n")
        self.label_player1_brelan = tk.Label(self, text = "player1_brelan"); self.label_player1_brelan.grid(row = 10, column = 1)
        self.label_player1_carre = tk.Label(self, text = "player1_carre"); self.label_player1_carre.grid(row = 11, column = 1)
        self.label_player1_full = tk.Label(self, text = "player1_full"); self.label_player1_full.grid(row = 12, column = 1)
        self.label_player1_small_suite = tk.Label(self, text = "player1_small_suite"); self.label_player1_small_suite.grid(row = 13, column = 1)
        self.label_player1_great_suite = tk.Label(self, text = "player1_great_suite"); self.label_player1_great_suite.grid(row = 14, column = 1)
        self.label_player1_yams = tk.Label(self, text = "player1_yams"); self.label_player1_yams.grid(row = 15, column = 1)
        self.label_player1_chance = tk.Label(self, text = "player1_chance"); self.label_player1_chance.grid(row = 16, column = 1)
        self.label_player1_sub_total = tk.Label(self, text = "player1_sub_total"); self.label_player1_sub_total.grid(row = 17, column = 1)
        self.label_player1_total = tk.Label(self, text = "player1_total"); self.label_player1_total.grid(row = 18, column = 1)

        # Affichage des points du joueur 2
        self.label_player2_name = tk.Label(self, text = ""); self.label_player2_name.grid(row = 1, column = 2)
        self.label_player2_one = tk.Label(self, text = ""); self.label_player2_one.grid(row = 2, column = 2)
        self.label_player2_two = tk.Label(self, text = ""); self.label_player2_two.grid(row = 3, column = 2)
        self.label_player2_three = tk.Label(self, text = ""); self.label_player2_three.grid(row = 4, column = 2)
        self.label_player2_four = tk.Label(self, text = ""); self.label_player2_four.grid(row = 5, column = 2)
        self.label_player2_five = tk.Label(self, text = ""); self.label_player2_five.grid(row = 6, column = 2)
        self.label_player2_six = tk.Label(self, text = ""); self.label_player2_six.grid(row = 7, column = 2)
        self.label_player2_top_sub_total = tk.Label(self, text = ""); self.label_player2_top_sub_total.grid(row = 8, column = 2)
        self.label_player2_bonus = tk.Label(self, text = ""); self.label_player2_bonus.grid(row = 9, column = 2, sticky = "n")
        self.label_player2_brelan = tk.Label(self, text = ""); self.label_player2_brelan.grid(row = 10, column = 2)
        self.label_player2_carre = tk.Label(self, text = ""); self.label_player2_carre.grid(row = 11, column = 2)
        self.label_player2_full = tk.Label(self, text = ""); self.label_player2_full.grid(row = 12, column = 2)
        self.label_player2_small_suite = tk.Label(self, text = ""); self.label_player2_small_suite.grid(row = 13, column = 2)
        self.label_player2_great_suite = tk.Label(self, text = ""); self.label_player2_great_suite.grid(row = 14, column = 2)
        self.label_player2_yams = tk.Label(self, text = ""); self.label_player2_yams.grid(row = 15, column = 2)
        self.label_player2_chance = tk.Label(self, text = ""); self.label_player2_chance.grid(row = 16, column = 2)
        self.label_player2_sub_total = tk.Label(self, text = ""); self.label_player2_sub_total.grid(row = 17, column = 2)
        self.label_player2_total = tk.Label(self, text = ""); self.label_player2_total.grid(row = 18, column = 2)
        
        #shuffle dices and choose/apply combine
        self.btnShuffleDices = tk.Button(self, text="Suffle Dices", command=self.shuffleDicesUI); self.btnShuffleDices.grid(row = 14, column = 6)
        self.comboChooseCombine = ttk.Combobox(self, 
            values=["1", "2", "3","4", "5", "6", "Brelan", "Carré", "Full", "Petite Suite", "Grande Suite", "Yams", "Chance"],
            state="readonly"); self.comboChooseCombine.grid(row = 16, column = 6)
        self.btnValidateDices = tk.Button(self, text="Sauve", command=self.validateDices); self.btnValidateDices.grid(row = 18, column = 6)
        #Dice 1
        diceOne = (Image.open('./assets/dices/de6.png')).resize((100,100)); renderDiceOne = ImageTk.PhotoImage(diceOne); imgDiceOne = tk.Label(self, image=renderDiceOne)
        imgDiceOne.image = renderDiceOne; imgDiceOne.grid(row = 9, column = 4, rowspan=4)
        self.checkDiceOne = tk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isOneChecked); self.checkDiceOne.grid(row = 13, column = 4)
        #Dice 2
        diceTwo = (Image.open('./assets/dices/de6.png')).resize((100,100)); renderDiceTwo = ImageTk.PhotoImage(diceTwo); imgDiceTwo = tk.Label(self, image=renderDiceTwo)
        imgDiceTwo.image = renderDiceTwo; imgDiceTwo.grid(row = 9, column = 5, rowspan=4)
        self.checkDiceTwo = tk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isTwoChecked); self.checkDiceTwo.grid(row = 13, column = 5)
        #Dice 3
        diceThree = (Image.open('./assets/dices/de6.png')).resize((100,100)); renderDiceThree = ImageTk.PhotoImage(diceThree); imgDiceThree = tk.Label(self, image=renderDiceThree)
        imgDiceThree.image = renderDiceThree; imgDiceThree.grid(row = 9, column = 6, rowspan=4)
        self.checkDiceThree = tk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isThreeChecked); self.checkDiceThree.grid(row = 13, column = 6)
        #Dice 4
        diceFour = (Image.open('./assets/dices/de6.png')).resize((100,100)); renderDiceFour = ImageTk.PhotoImage(diceFour); imgDiceFour = tk.Label(self, image=renderDiceFour)
        imgDiceFour.image = renderDiceFour; imgDiceFour.grid(row = 9, column = 7, rowspan=4)
        self.checkDiceFour = tk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isFourChecked); self.checkDiceFour.grid(row = 13, column = 7)
        #Dice 5
        diceFive = (Image.open('./assets/dices/de6.png')).resize((100,100)); renderDiceFive = ImageTk.PhotoImage(diceFive); imgDiceFive = tk.Label(self, image=renderDiceFive)
        imgDiceFive.image = renderDiceFive; imgDiceFive.grid(row = 9, column = 8, rowspan=4)
        self.checkDiceFive = tk.Checkbutton(self, onvalue=1, offvalue=0, variable=self.isFiveChecked); self.checkDiceFive.grid(row = 13, column = 8)
        ################## END PAGEGAME #####################

        #################### Interface Messagerie #######################

        btnReturn = tk.Button(self, text="Go back", command=self.goBack); btnReturn.grid(row = 0, column = 8, sticky="e", columnspan=2)

        textes = scrolledtext.ScrolledText(self, wrap = tk.WORD, width = 40,height = 10)
        textes.insert(tk.INSERT, "Welcome!\n"); textes.config(state="disabled"); textes.grid(row = 1, column = 4, columnspan=6, rowspan=6 )
        controller.setTextView(textes)  

        self.entryMessage= tk.Entry(self); self.entryMessage.grid(row = 7, column = 6, sticky="e")

        buttonSend= tk.Button(self, text="send", command=self.sendMessage); buttonSend.grid(row = 7, column = 7, sticky="w")
        
        ################# End PageMain ####################

    # Game Functions

    def validateDices(self): #add data to json file and display changes
        if (self.comboChooseCombine.get() == ''):
            tk.messagebox.showwarning(title="Alerte", message="Veuillez selectionner une combinaison valide")
        else:
            comboBoxSelectedValue = self.comboChooseCombine.get()
            self.btnShuffleDices.config(state="normal")
            self.btnValidateDices.config(state="disable")
            self.ReturnScore(comboBoxSelectedValue)
        #reset count for dice toss and clear checkboxs
        self.numberOfToss = 0
        self.isOneChecked.set(value=0); self.isTwoChecked.set(value=0); self.isThreeChecked.set(value=0); self.isFourChecked.set(value=0); self.isFiveChecked.set(value=0)
        

    def shuffleDicesUI(self): #shuffle dices, send data to json to display dices for oppennent
        print('1 : ' + str(self.isOneChecked.get()) + ' | 2 : ' + str(self.isTwoChecked.get()) + ' | 3 : ' + str(self.isThreeChecked.get()) +' | 4 : ' + str(self.isFourChecked.get()) + ' | 5 : ' + str(self.isFiveChecked.get()))
        if self.isOneChecked.get() == 0:
            print('shuffleDicesUI : dans le premier check')
            self.dicesNumbers[0]= random.randint(1, 6)
        elif self.isTwoChecked.get() == 0:
            self.dicesNumbers[1]= random.randint(1, 6)
        elif self.isThreeChecked.get() == 0:
            self.dicesNumbers[2]= random.randint(1, 6)
        elif self.isFourChecked.get() == 0:
            self.dicesNumbers[3]= random.randint(1, 6)
        elif self.isFiveChecked.get() == 0:
            self.dicesNumbers[4]= random.randint(1, 6)
        print(self.dicesNumbers)
        self.btnValidateDices.config(state="normal")
        if self.numberOfToss < 2:
            if self.numberOfToss == 0:
                for i in range(len(self.dicesNumbers)):
                    self.dicesNumbers[i]= random.randint(1, 6)
            self.numberOfToss += 1
            self.displayDices(self.dicesNumbers)
        else:
            self.displayDices(self.dicesNumbers)
            self.btnShuffleDices.config(state="disable")
            
        print('shuffle')
        #Dice 1 | Affiche le dé correspondant au dernier lancé
        diceOne = (Image.open(self.dicesUI[0])).resize((100,100)); renderDiceOne = ImageTk.PhotoImage(diceOne); imgDiceOne = tk.Label(self, image=renderDiceOne)
        imgDiceOne.image = renderDiceOne; imgDiceOne.grid(row = 9, column = 4, rowspan=4)
        #Dice 2
        diceTwo = (Image.open(self.dicesUI[1])).resize((100,100)); renderDiceTwo = ImageTk.PhotoImage(diceTwo); imgDiceTwo = tk.Label(self, image=renderDiceTwo)
        imgDiceTwo.image = renderDiceTwo; imgDiceTwo.grid(row = 9, column = 5, rowspan=4)
        #Dice 3
        diceThree = (Image.open(self.dicesUI[2])).resize((100,100)); renderDiceThree = ImageTk.PhotoImage(diceThree); imgDiceThree = tk.Label(self, image=renderDiceThree)
        imgDiceThree.image = renderDiceThree; imgDiceThree.grid(row = 9, column = 6, rowspan=4)
        #Dice 4
        diceFour = (Image.open(self.dicesUI[3])).resize((100,100)); renderDiceFour = ImageTk.PhotoImage(diceFour); imgDiceFour = tk.Label(self, image=renderDiceFour)
        imgDiceFour.image = renderDiceFour; imgDiceFour.grid(row = 9, column = 7, rowspan=4)
        #Dice 5
        diceFive = (Image.open(self.dicesUI[4])).resize((100,100)); renderDiceFive = ImageTk.PhotoImage(diceFive); imgDiceFive = tk.Label(self, image=renderDiceFive)
        imgDiceFive.image = renderDiceFive; imgDiceFive.grid(row = 9, column = 8, rowspan=4)


    def displayDices(self, dices):
        #dire à quoi sert la fonction
        for i in range(len(self.dicesNumbers)):
            if str(self.dicesNumbers[i]) in 'de1':
                self.dicesUI[i] = './assets/dices/de1.png'
            elif str(self.dicesNumbers[i]) in 'de2':
                self.dicesUI[i] = './assets/dices/de2.png'
            elif str(self.dicesNumbers[i]) in 'de3':
                self.dicesUI[i] = './assets/dices/de3.png'
            elif str(self.dicesNumbers[i]) in 'de4':
                self.dicesUI[i] = './assets/dices/de4.png'
            elif str(self.dicesNumbers[i]) in 'de5':
                self.dicesUI[i] = './assets/dices/de5.png'
            else:
                self.dicesUI[i] = './assets/dices/de6.png'
        print(self.dicesUI)
            # self.dicesUI = dices
        

    def ReturnScore(self, combine):
        # combine = validateDices()
        # print('Combine = ' + validateDices())
        dices = self.dicesNumbers 
        if combine == "1":
            if self.checkDiceOne == "False":
                if 1 not in dices:
                    confirmBox = tk.messagebox.askquestion("Confirmation", "Vous avez choisi : 1 = 0 points")
                    if confirmBox == 'yes':
                        self.label_player1_one.config(text=self.GameRules.n1(dices))
                        self.label_player1_total.config(text=self.GameRules.n1(dices))
                else:
                    confirmBox = tk.messagebox.askquestion("Confirmation", "Vous avez choisi : 1")
                    if confirmBox == 'yes':
                        self.label_player1_one.config(text=self.GameRules.n1(dices))
                        self.checkDiceOne = True
            else:
                tk.messagebox.showerror("Alerte", "Vous avez déjà joué les 1")


        elif combine == "2":
            score = self.GameRules.n2(dices)
            self.label_player1_two.config(text=self.GameRules.n2(dices))
        elif combine == "3":
            score = self.GameRules.n3(dices)
        elif combine == "4":
            score = self.GameRules.n4(dices)
        elif combine == "5":
            score = self.GameRules.n5(dices)
        elif combine == "6":
            score = self.GameRules.n6(dices)
        elif combine == "Brelan":
            score = self.GameRules.brelan(dices)
        elif combine == "Carré":
            score = self.GameRules.carre(dices)
        elif combine == "Full":
            score = self.GameRules.full(dices)
        elif combine == "Petite Suite":
            score = self.GameRules.petiteSuite(dices)
        elif combine == "Grande Suite":
            score = self.GameRules.grandeSuite(dices)
        elif combine == "Yam":
            score = self.GameRules.yams(dices)
        elif combine == "Chance":
            score = self.GameRules.chance(dices)
        else:
            tk.messagebox.showinfo(title="Alert", message="Please choose a valide option")
            #throw alert
        return score

    # End Game Function

    # Messages function
    def goBack(self):
        self.controller.client.send("QUIT")
        self.controller.show_frame("StartPage")

    def sendMessage(self):
        self.controller.client.send(self.entryMessage.get())
        self.entryMessage.delete(0, tk.END)
    
    # End Messages function

if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()