from npc import NPC
from const import *
from s4vsprite import s4vSprite
class PlayerNPC(NPC):
    def __init__(self):
        super().__init__()
        self.custom = s4vSprite(NPC_X, NPC_Y, TRAU_IMG)

    