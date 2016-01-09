
#don't be confused by infinities
def get_nth_dict(d, n):
   i = 0
   for x,y in d:
      if i == n:
         return x, y
   return None, None

class Player:
   def __init__(self, i):
      self.num = i
      self.gameBoard = None
      #{name: troops}
      self.countries = {} #owned countries

   def _setGameBoard(self, gameBoard):
      self.gameBoard = gameBoard

   ##pre-game things
   #TODO: AI needs more info to analyze things
   def chooseCountry(self, freeCountries):
      n = shellutils.get_random() % (len(freeCountries) - 1)
      chosen = freeCountries[n]
      self.countries[chosen] = 0
      return n, chosen

   #TODO: don't need to return if we keep track of it
   #returns list of where it added people e.g. {'China': 1, 'US': 2}
   def reinforce(self, numTroops):
      placesToReinforce = {}
      while numTroops > 0:
         n = shellutils.get_random(len(self.countries) - 1)
         chosenCtr = get_nth_dict(self.countries, n)
         ctrName, ctrTroops = chosenCtr

         self.countries[ctrName] += 1
         if placesToReinforce.get(chosenCtr, None) is None:
            placesToReinforce[chosenCtr] = 1
         placesToReinforce[chosenCtr] += 1
      return placesToReinforce

   ##end pre-game things

   #{'start':'China', 'end':'Russia', 'count':10}
   def move(self):
     pass

