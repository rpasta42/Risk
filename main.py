from pycloak import shellutils
import importlib
from GameBoard import GameBoard #, Country

#TODO: Player needs access to GameBoard info,
#but GameBoard and Player are both part of Game
#Should we use inheritance or pass callbacks, etc?
class Player:
   def __init__(self):
      self.gameBoard = None
      self.countries = [] #owned countries

   def setGameBoard(self, gameBoard):
      self.gameBoard = gameBoard

   ##pre-game things
   #TODO: AI needs more info to analyze things
   def chooseCountry(self, freeCountries):
      n = shellutils.get_random() % (len(freeCountries) - 1)
      chosen = freeCountries[n]
      self.countries.append(chosen)
     return chosen

   #returns list of where it added people e.g. {'China': 1, 'US': 2}
   def reinforce(self, numTroops):
      placesToReinforce = {}
      while numTroops > 0:
         n = shellutils.get_random() % (len(self.countries) - 1)
         chosenCtr = self.countries[n]
         if placesToReinforce.get(chosenCtr, None) is None:
            placesToReinforce[chosenCtr] = 0
         placesToReinforce[chosenCtr] += 1
      return placesToReinforce

   ##end pre-game things
 
   #{'start':'China', 'end':'Russia', 'count':10}
   def move(self):
     pass

#choice or automatic selection
class Game:
   def __init__(self, players, gameBoard, chooseAuto=False):
      self.gameBoard = gameBoard
      self.players = players

      for player in players:
         player.setGameBoard(gameBoard)
      #self.chooseAuto = chooseAuto

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

   return game

#importlib.reload(main)
a = main()

