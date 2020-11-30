from const import *
from playernpc import PlayerNPC
from ainpc import AiNPC
class Challenge:
    def __init__(self):
        self.score = 0
        self.count_down = 20
        self.state = CONVERSATION_STATE
        self.player_npc = PlayerNPC()
        self.ai = AiNPC()
        self.turn = 0
    
    def reset(self):
        pass

    def getScore(self):
        return self.score

    def doChallenge(self, window):
        if self.state == CONVERSATION_STATE:
            self.showCommunication(window)
                
        elif self.state == RUN_CHALLENGE_STATE:
            self.drawOutput(window)
        else:
            self.drawOutput(window)
            if self.checkResult():
                self.ai.congrat(window)
                return PASSED_CHALLENGE
            else:
                self.ai.reportError(window) 
                return FAILED_CHALLENGE
        return self.state

    def showCommunication(self,window):
        if self.player_npc.isFinishedTalking() and self.ai.isFinishedTalking():
            self.state = RUN_CHALLENGE_STATE
        elif self.turn == 0:
            if self.ai.talk(window):
                self.turn = 1
        else:
            if self.player_npc.talk(window):
                self.turn = 0
    
    def countDown(self):
        if self.count_down != 0:
            self.count_down -= 1

    def drawOutput(self, window):
        pass

    def checkResult(self):
        pass