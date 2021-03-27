   if combine == "1":
        score = self.GameRules.n1(dices)
        if self.label_player1_one.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi 1 pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_two.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_top_sub_total.config(
                    text=score+int(self.label_player1_top_sub_total.cget("text")))
                try:
                    # faire la somme des score en haut pour calculer le bonus
                    if self.label_player1_bonus.cget("text") != "35":
                        if int(self.label_player1_one.cget("text")) + int(self.label_player1_two.cget("text")) + int(self.label_player1_three.cget("text")) + int(self.label_player1_four.cget("text")) + int(self.label_player1_five.cget("text")) >= 63:
                            self.label_player1_bonus.config(text=35)
                            self.label_player1_top_sub_total.config(
                                text=35+int(self.label_player1_top_sub_total.cget("text")))
                            self.label_player1_total.config(
                                text=35+int(self.label_player1_total.cget("text")))
                        print('Bonus obtenu!')
                    else:
                        print('Bonus déjà obtenu!')
                except:
                    print('Score inférieur à 63 points')
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les 1.\nVeuillez choisir une autre combinaison")
    elif combine == "2":
        score = self.GameRules.n2(dices)
        if self.label_player1_two.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi 2 pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_two.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_top_sub_total.config(
                    text=score+int(self.label_player1_top_sub_total.cget("text")))
                try:
                    # faire la somme des score en haut pour calculer le bonus
                    if self.label_player1_bonus.cget("text") != "35":
                        if int(self.label_player1_one.cget("text")) + int(self.label_player1_two.cget("text")) + int(self.label_player1_three.cget("text")) + int(self.label_player1_four.cget("text")) + int(self.label_player1_five.cget("text")) >= 63:
                            self.label_player1_bonus.config(text=35)
                            self.label_player1_top_sub_total.config(
                                text=35+int(self.label_player1_top_sub_total.cget("text")))
                            self.label_player1_total.config(
                                text=35+int(self.label_player1_total.cget("text")))
                        print('Bonus obtenu!')
                    else:
                        print('Bonus déjà obtenu!')
                except:
                    print('Score inférieur à 63 points')
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les 2.\nVeuillez choisir une autre combinaison")
    elif combine == "3":
        score = self.GameRules.n3(dices)
        if self.label_player1_three.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi 3 pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_three.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_top_sub_total.config(
                    text=score+int(self.label_player1_top_sub_total.cget("text")))
                try:
                    # faire la somme des score en haut pour calculer le bonus
                    if self.label_player1_bonus.cget("text") != "35":
                        if int(self.label_player1_one.cget("text")) + int(self.label_player1_two.cget("text")) + int(self.label_player1_three.cget("text")) + int(self.label_player1_four.cget("text")) + int(self.label_player1_five.cget("text")) >= 63:
                            self.label_player1_bonus.config(text=35)
                            self.label_player1_top_sub_total.config(
                                text=35+int(self.label_player1_top_sub_total.cget("text")))
                            self.label_player1_total.config(
                                text=35+int(self.label_player1_total.cget("text")))
                        print('Bonus obtenu!')
                    else:
                        print('Bonus déjà obtenu!')
                except:
                    print('Score inférieur à 63 points')
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les 3.\nVeuillez choisir une autre combinaison")
    elif combine == "4":
        score = self.GameRules.n4(dices)
        if self.label_player1_four.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi 4 pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_four.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_top_sub_total.config(
                    text=score+int(self.label_player1_top_sub_total.cget("text")))
                try:
                    # faire la somme des score en haut pour calculer le bonus
                    if self.label_player1_bonus.cget("text") != "35":
                        if int(self.label_player1_one.cget("text")) + int(self.label_player1_two.cget("text")) + int(self.label_player1_three.cget("text")) + int(self.label_player1_four.cget("text")) + int(self.label_player1_five.cget("text")) >= 63:
                            self.label_player1_bonus.config(text=35)
                            self.label_player1_top_sub_total.config(
                                text=35+int(self.label_player1_top_sub_total.cget("text")))
                            self.label_player1_total.config(
                                text=35+int(self.label_player1_total.cget("text")))
                        print('Bonus obtenu!')
                    else:
                        print('Bonus déjà obtenu!')
                except:
                    print('Score inférieur à 63 points')
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les 4.\nVeuillez choisir une autre combinaison")
    elif combine == "5":
        score = self.GameRules.n5(dices)
        if self.label_player1_five.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi 5 pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_two.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_top_sub_total.config(
                    text=score+int(self.label_player1_top_sub_total.cget("text")))
                try:
                    # faire la somme des score en haut pour calculer le bonus
                    if self.label_player1_bonus.cget("text") != "35":
                        if int(self.label_player1_one.cget("text")) + int(self.label_player1_two.cget("text")) + int(self.label_player1_three.cget("text")) + int(self.label_player1_four.cget("text")) + int(self.label_player1_five.cget("text")) >= 63:
                            self.label_player1_bonus.config(text=35)
                            self.label_player1_top_sub_total.config(
                                text=35+int(self.label_player1_top_sub_total.cget("text")))
                            self.label_player1_total.config(
                                text=35+int(self.label_player1_total.cget("text")))
                        print('Bonus obtenu!')
                    else:
                        print('Bonus déjà obtenu!')
                except:
                    print('Score inférieur à 63 points')
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les 5.\nVeuillez choisir une autre combinaison")
    elif combine == "6":
        score = self.GameRules.n6(dices)
        if self.label_player1_six.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi 6 pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_six.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_top_sub_total.config(
                    text=score+int(self.label_player1_top_sub_total.cget("text")))
                try:
                    # faire la somme des score en haut pour calculer le bonus
                    if self.label_player1_bonus.cget("text") != "35":
                        if int(self.label_player1_one.cget("text")) + int(self.label_player1_two.cget("text")) + int(self.label_player1_three.cget("text")) + int(self.label_player1_four.cget("text")) + int(self.label_player1_five.cget("text")) >= 63:
                            self.label_player1_bonus.config(text=35)
                            self.label_player1_top_sub_total.config(
                                text=35+int(self.label_player1_top_sub_total.cget("text")))
                            self.label_player1_total.config(
                                text=35+int(self.label_player1_total.cget("text")))
                        print('Bonus obtenu!')
                    else:
                        print('Bonus déjà obtenu!')
                except:
                    print('Score inférieur à 63 points')
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les 6.\nVeuillez choisir une autre combinaison")
    elif combine == "Brelan":
        score = self.GameRules.brelan(dices)
        if self.label_player1_brelan.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Brelan pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_brelan.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété le Brelan.\nVeuillez choisir une autre combinaison")
    elif combine == "Carré":
        score = self.GameRules.carre(dices)
        if self.label_player1_carre.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Carré pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_carre.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété le Carré.\nVeuillez choisir une autre combinaison")
    elif combine == "Full":
        score = self.GameRules.full(dices)
        if self.label_player1_full.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Full pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_full.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété le Full.\nVeuillez choisir une autre combinaison")
    elif combine == "Petite Suite":
        score = self.GameRules.petiteSuite(dices)
        if self.label_player1_small_suite.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Petie Suite pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_small_suite.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété la Petite Suite.\nVeuillez choisir une autre combinaison")
    elif combine == "Grande Suite":
        score = self.GameRules.grandeSuite(dices)
        if self.label_player1_great_suite.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Grande Suite pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_great_suite.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété la Grande Suite.\nVeuillez choisir une autre combinaison")
    elif combine == "Yam":
        score = self.GameRules.brelan(dices)
        if self.label_player1_brelan.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Brelan pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_brelan.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les Brelan.\nVeuillez choisir une autre combinaison")
    elif combine == "Chance":
        score = self.GameRules.brelan(dices)
        if self.label_player1_brelan.cget("text") == ".":
            confirmBox = tk.messagebox.askquestion(
                "Confirmation", "Vous avez choisi Brelan pour " + str(score) + " points")
            if confirmBox == 'yes':
                self.label_player1_brelan.config(text=score)
                self.btnShuffleDices.config(state="normal")
                self.btnValidateDices.config(state="disable")
                self.label_player1_total.config(
                    text=score+int(self.label_player1_total.cget("text")))
                self.label_player1_sub_total.config(
                    text=score+int(self.label_player1_sub_total.cget("text")))
        else:
            confirmBox = tk.messagebox.showwarning(
                "Alerte", "Vous avez déjà complété les Brelan.\nVeuillez choisir une autre combinaison")
    else:
        tk.messagebox.showinfo(
            title="Alert", message="Please choose a valide option")
        # throw alert
    return score
