#!/usr/bin/env python

from pycloak import shellutils
from pycloak.collections import sub_lst
import importlib
from BoardChecker import BoardChecker #, Country
from Player import Player

#message to user
def user_notify(msg):
   print(msg)

#used by Game for varification I guess
#  check number of troops, continent, country, etc.
#not used by player
#don't store name because Country is entry for name key
class Country:
   def __init__(name, continent):
      self.troops = 0
      self.continent = continent
      self.team = -1

#choice or automatic selection
class Game:
   def __init__(self, players, gameBoard): #, chooseAuto=False):
      self.gameBoard = gameBoard
      self.players = players

      for player in players:
         player._setGameBoard(gameBoard)

      countriesDict = gameBoard['countries']
      self._freeCountries = []
      for country, neighbors in countriesDict:
         self._freeCountries.append(country)

      #TODO: make sure we can spread starter army evenly
      if len(countriesDict) % len(players) is not 0:
         user_notify('Cannot distribute countries evenly')

   #TODO: checks if any specific player won or
   #return a dict of {country:continent} ?
   def controlsContinent(self):
      #for
      player = self.players[playerNum]
      for name, troops in player.countries:
         pass
   def hasAllCountries(self, playerNum):
      pass

   #begins whole process
   def begin(self):
      self.choose_countries()
      self.initial_reinforce()
      while !hasAllCountries():
         self.start_move()

   def start_move(self):
      for player in self.players:
         self.reinforce()
         self.attack()
         self.move()
      self.

   def initial_reinforce(self):
      startTroops = self.gameBoard['start-army']

      while starTroops > 0:
         for player in self.players:
            if !(startTroops > 0):
               user_notify('Cannot spread reinforcements equally')
               break
            player.reinforce(1) #annoying af, fixme
            startTroops -= 1

   def choose_countries(self):
      c = self._freeCountries
      while len(c) != 0:
         for player in self.players:
            if len(c) == 0: #in case we can't distribute equally
               break;
            n = country = player.chooseCountry(c)
            self._freeCountries = sub_lst(c, c[n])



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
      'Italy'     : ['France'] #,
      #'Georgia'   : ['Niger'],
      #'Niger'     : ['Georgia']
   }

   continents = [
      {  'name'      : 'Europe',
         'bonus'     : 5,
         'members'   : ['Ukraine', 'Britain', 'Sweden', 'France', 'Italy']
      },
      {  'name'      : 'Asia',
         'bonus'     : 2,
         'members'   : ['Russia', 'China']
      },
      {
         'name'      : 'Merica',
         'bonus'     : 4,
         'members'   : ['US', 'Canada']
      }
   ]

   gameBoard = {
      'countries'    : countries,
      'continents'   : continents,
      'start-army'   : 20
   }

   boardChecker = BoardChecker(gameBoard)
   players = [Player(0), Player(1)]

   game = Game(players, gameBoard)

   return game

#importlib.reload(main)
a = main()

