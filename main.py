import Controller,Player

def heart(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    """
    here is where the heart of the game will go. create the controller and view. pass the view to the controller and make the items 
    inside of the controller. 
    
    objects needed: items, moves, pokemon
    make trainers later
    """
    Ash=Player("player")
    #gameview=view
    gameController=Controller(1,Ash)
    gameController.explore()


if __name__ == '__main__':
    heart('PyCharm')

