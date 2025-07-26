import random
import time
class cricketfun():
     def __init__(self,team_a,team_b):
       self.score = 0
       self.team_a = team_a
       self.team_b = team_b
      


     def first_innings(self):
          
           while True:
                   
                  try:
                        
                       player_choice=int(input("Make Your Run 1 to 6 : "))
                       if player_choice <1 or player_choice> 6:
                          print("enter the valid number 1 To 6 ")
                          continue


                       computer_choice=random.randint(1,6)
                       if (computer_choice==player_choice):
                         print(f"\t\t\tOOps your out\n FINAL SCORE IS  : {self.score}")
                         break
                       else:
                         self.score+=player_choice
                         print(f"\t\t\t\t\t{self.team_a} your Score is : {self.score}")


                  except ValueError as e:
                       
                       print(f"Type valid number :{player_choice}")


                  finally:
                     print("\n\t\t\tAwsome play!!")

           target = self.score + 1
           print(f"\n\t\t{b} Need  {target} Run to Win")
           self.score = 0

           while True:
                  try:
                       player_choice=int(input("\nMake your ball 1 to 6 :"))
                       if player_choice<1 or player_choice>6:
                            print("Enter The Valid Number 1 TO 6")
                            continue

                       computer_choice=random.randint(1,6)
                       if (computer_choice==player_choice):
                           print(f"\t\t\tOops you Get Wicket\n FINAL SCORE IS : {self.score}")
                           break
                       else:
                           self.score+=player_choice
                           print(f"\t\t\t\t\t{self.team_b} Your score is : {self.score}")
                           if self.score >= target:
                                print(f"\n\t\t{b} won the match")
                                return


                  except ValueError as e :
                      print(f"Type valid number :{playe_choice}")

                  finally:
                       
                     print("\n\t\t\tWoderfulll playy")
          

                      
           if self.score < target:
               print(f"\n\t\t\t{a} Won the Match")

           elif self.score==target:
                print("Match Is Draw")


     def second_innings(self):
     
             while True:
                  try:
                       player_choice=int(input("Make your ball 1 to 6 :"))
                       if player_choice<1 or player_choice>6:
                            print("Enter The Valid Number 1 TO 6")
                            continue

                       computer_choice=random.randint(1,6)
                       if (computer_choice==player_choice):
                           print(f"\t\t\tOops you Get Wicket\n FINAL SCORE IS : {self.score}")
                           break
                       else:
                           self.score+=player_choice
                           print(f"\t\t\t\t\t{self.team_b} Your score is : {self.score}")
                           target=self.score+1


                  except ValueError as e :
                      print(f"Type valid number :{playe_choice}")

                  finally:
                         print("\n\t\t\tWoderfulll playyy")

                      
             target = self.score + 1
             print(f"\n\t\t{a} Need  {target} Run to Win")
             self.score = 0
             while True:

                    try:
                       player_choice=int(input("\nMake Your Run 1 To 6 :"))
                       if player_choice<1 or player_choice>6:
                          print("enter the valid number 1 To 6 ")
                          continue


                       computer_choice=random.randint(1,6)
                       if (computer_choice==player_choice):
                          print(f"\t\t\tOOps your out\n FINAL SCORE IS : {self.score}")
                          if self.score ==target:
                              print("Match Draw")
                          break
                       else:
                           self.score+=player_choice
                           print(f"\t\t\t\t\t{self.team_a} your Score is : {self.score}")
                           if self.score>target:
                                 print(f"\n\t\t{a} Won the Match ")
                                 return 


                    except ValueError as e:
                       
                         print(f"Type valid number :{player_choice}")


                    finally:
                     
                        print("\n\t\t\tAwsome play!!")
                        

             if self.score < target:
              
       
                   print(f"\n\t\t\t{b}Won The Match")


             elif self.score==target:
                   print("match is draw")
 

dream="ilaya"
B=""
print( "\t\tWelcome To Great Karikalan\n                     Cricket Game!!🏏🏏🏏")
time.sleep(1)
d=int(input("\n\tIf You Want Head Press 1 Or Tail Press 0 : "))
time.sleep(1)
c=random.randint(0,1)
if (d==c):
   print(f"\t\tYou Win The Toss ")
   B=int(input("\n\tIf you want Bat first press 1 Or Bowl first press 0: "))
   if B==1:
      print(f"\t\tGreat If choose Bat First")
   else:
      print(f"\t\tGreat If choose Bowl First")

else:
   print("\t\tYou Loss The Toss!!")
   batball=["Bat","Bowll"]
   dream=random.choice(batball)
   print(f"\n\t\tYour Oponent Choose {dream} First ")
        
a=str(input("\n\t\tEnter Your Team Name : "))
time.sleep(1)
Team =[ " Atharavator Group "," Bayama Enaka ","Acham Ile Odu" ,"Anbodu Vanga Vambodu Ponga","pokiri pongal","Va Vantha 11 ", "Raanuva Padai ","The Boys" ]
b=random.choice(Team)
score=0
print(f" \n\t\t{a}  VS  {b} \n")
time.sleep(1)


s1=cricketfun(a,b)


if (B == 1 or dream=="Bowll"):
     s1.first_innings()

elif (B == 0 or dream == "Bat"):
     s1.second_innings()
          
                     
          

                
            
