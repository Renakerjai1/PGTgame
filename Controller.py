import random
class Controller:
    def __init__(self,view,player):
        """
        make an area and based on the area different pokemon will spawn and attack
        """
        self.view= view
        self.player=player
        self.area= random.random(3)

    def explore(self):
        adventurestatus=True
        while(adventurestatus==True and self.checkPokemonTeamstatus()):




    def checkPokemonTeamstatus(self):
        """
        :return: True if all pokemon are alive
        """
        return True
