class Moves:
    """
    description of stuff
    """
    def __init__(self,damage,type,bonuseffects="none"):
        self.damage=damage
        self.type=type
        self.bonuseffects=bonuseffects

    def getdamage(self):
        return(self.damage)

    def gettype(self):
        return(self.type)

    def getbonuseffects(self):
        return(self.bonuseffects)