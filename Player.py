class Player:
    """
    a player should be able to catch a pokemon, fight a pokemon, use an item, pick up an item, and release a pokemon.
    """
    def __init__(self,name):
        self.name=name
        self.coin=0
        self.pokemonTeam=[]
        self.itemBag=[]
        self.pokeBank=[]


    def catch(self, pokemon):
        """

        :param pokemon: the pokemon that was caught to be added
        :return: a message saying the pokemon was caught and has been added to the inventory or you let the pokemon go.
        """
        if len(self.pokemonTeam)>5:
            self.pokeBank.append(self.pokemonTeam[5])
            self.pokemonTeam.pop(5)
        else:
            self.pokemonTeam.append(pokemon)
        return "{} has been added to the party".format(pokemon.getname())
    def pickupItem(self,item):
        self.itemBag.append(item)
    def dropitem(self,index):
        self.itemBag.pop(index-1)
    def getItemBag(self):
        return self.itemBag





