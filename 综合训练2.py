#_*_coding:utf-8-*-
import random

class Bingle:
    """
        Generate a random answer,and record guess times,and judge it
    """
    A,B=(0,0)   #Match falg
    AttemptTimes=8  #Geuss times
    Answer=[0,0,0,0]   #The Answer
    def BuildAnswer(self):       
        random.seed()
        while 1:
            digit = random.randint(0, 9999)
            self.Answer[0]=digit/1000
            self.Answer[1]=digit%1000/100
            self.Answer[2]=digit%100/10
            self.Answer[3]=digit%10
            if self.Answer[0]!=self.Answer[1] and self.Answer[0]!=self.Answer[2] and self.Answer[0]!=self.Answer[3] and self.Answer[1]!=self.Answer[2] and self.Answer[1]!=self.Answer[3] and self.Answer[2]!=self.Answer[3]:
                return
    def __init__(self):
        Answer=[0,0,0,0]
        AttemptTimes=0
        self.BuildAnswer()
    def IsTryStringOK(self,TryString):
        if TryString.isdigit() and len(TryString)==4:
            if TryString[0]!=TryString[1] and TryString[0]!=TryString[2] and TryString[0]!=TryString[3] and TryString[1]!=TryString[2] and TryString[1]!=TryString[3] and TryString[2]!=TryString[3]:
                return 1
        return 0       

    def Judge(self,TryString):
        for i in range(4):
            if(TryString[i]==str(self.Answer[i])):
                self.A=self.A+1
            else:
                for j in range(4):
                    if(TryString[i]==str(self.Answer[j])):
                       self.B=self.B+1
        ReturnStr = "%dA%dB"%(self.A,self.B)
        self.A=0
        self.B=0
        return ReturnStr
class MainGame:
    """
        Play the game
    """
    B=None
    def __init__(self):
        self.B=Bingle()
        #print "Answer:%s"%(self.B.Answer)
        print "I've ready,please guess me."

    def Play(self):     
        while self.B.AttemptTimes:
            TryString=raw_input("%d:\t"%self.B.AttemptTimes) 
            if self.B.IsTryStringOK(TryString):                         
                TryResult=self.B.Judge(TryString)
                if TryResult=="4A0B":
                    print "You are winer!"
                    break
                else:
                    print TryResult
                    self.B.AttemptTimes=self.B.AttemptTimes-1
            else:
                print "Input error! Type again,",
                continue
        else:
            print "Attempt times is Eight.\nThe finily answer is: %s\nGame Over!"%self.B.Answer
if __name__=="__main__":      
    Try=1
    while Try:
        BingleGame = MainGame()
        BingleGame.Play()   
        Data=raw_input( "Do you want to try again? \nType [0] for 'No' and others for [Yes]\n")
        if Data.isdigit():
            Try=int(Data)
        else:
            Try=1 
    else:
        print "Game exited!"

 