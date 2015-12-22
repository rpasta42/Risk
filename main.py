from pycloak import shellutils
import importlib
from GameBoard import GameBoard #, Country

#TODO: Player needs access to GameBoard info,
#but GameBoard and Player are both part of Game
#Should we use inheritance or pass callbacks, etc?
class Player:
    def __init__(self):
        pass

    #pre-game things
    def chooseCountry(self, allCountries, freeCountries):
        pass
    def reinforce(self, ownCountries):
        self.chooseCountry = chooseCountryCallback
        #returns list of where it added people e.g. {'China': 1, 'US': 2}

#choice or automatic selection
class Game:
    def __init__(self, players, gameBoard, chooseAuto=False):
        self.gameBoard = gameBoard
        self.players = players
        self.chooseAuto = chooseAuto

    def begin(self):
        pass

def main():
    countries = {
        'Ukraine'   : ['Russia', 'France'],
        'Russia'    : ['China', 'Ukraine', 'Canada', 'Sweden'],
        'US'        : ['Canada'],
        'Canada'    : ['US', 'Russia'],
        'China'     : ['Russia'],
        'Britain'   : ['France', 'Sweden'],
        'Sweden'    : ['Russia', 'Britain'],
        'France'    : ['Ukraine', 'Britain', 'Italy'],
        'Italy'     : ['France']
    }

    continents = {
        'Europe' : ['Ukraine', 'Britain', 'Sweden', 'France', 'Italy'],
        'Asia'   : ['Russia', 'China'],
        'Merica' : ['US', 'Canada']
    }

    gameBoard = GameBoard(countries, continents)
    players = [Player(), Player()]

    game = Game(players, gameBoard)

    return m

#importlib.reload(main)
a = main()

