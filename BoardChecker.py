#TODO: removeme from pycloak.collections import sub_lst


class BoardChecker:
   def __init__(self, gameBoard):
      #TODO: check that all things exist
      self._neighbor_info = gameBoard['countries']
      self.continents = gameBoard['continents']

      assert(gameBoard['start-army'] >= len(self._neighbor_info))

      self._run_map_tests()

   def get_country_continent(self, name):
      for continent in self.continents:
         if name in continent['members']:
            return continent

   #kk how does this work without being implemented?
   def touching(self, c1, c2):
      self.check_exists(c1, c2)
      if c2 in self._neighbor_info[c1]:
         return True
      return False
      #TODO: wtf i thought this was implemented

   def check_exists(self, *names):
      for country in names:
         if self._neighbor_info.get(country, None) is None:
            raise Exception("Country doesn't exist: %s" % country)
            return False
      return True

   def _run_map_tests(self):
      self._check_self_neighbor(self._neighbor_info)
      self._check_neighbors_exist(self._neighbor_info)
      self._check_duplex(self._neighbor_info)
      self._check_pathways(self._neighbor_info)
      self._check_continents()

   def _check_continents(self):
      #TODO: implement continent checks, maybe move it to same structure as countries
      #make sure all countries in continent touch at least 1 other country in continent
      #make sure every country is part of only 1 continent
      #make sure they're not part of 2 different continents
      #make sure there isn't continents without countries
      pass

   #neighbor does not have entry in countries
   def _check_neighbors_exist(self, countries):
      for country in countries:
         neighbors = countries.get(country, None)
         if neighbors is None or len(neighbors) == 0:
            raise Exception('Country cannot have empty neighbors')
         self.check_exists(*neighbors)

   #own neighbor
   def _check_self_neighbor(self, countries):
      for country in countries:
         neighbors = countries[country]
         for neighbor in neighbors:
            if country == neighbor:
               raise Exception("Country '%s' cannot be it's own neighbor" % country)

   #check that route exists
   def _check_pathways(self, countries):
      for start in countries:
         for end in countries:
            if not self._connects(start, end, []):
               raise Exception('Countries not connected: %s %s' % (start, end))

   def _connects(self, start, end, checked=[]):
      if start == end:
         return True
      #if self.touching(start, end):
      #   return True
      else:
         end_neighbors = self._neighbor_info[end]
         for neighbor in end_neighbors:
            #if self.touching(start, neighbor):
            #   return True
            if not (neighbor in checked):
               checked.append(neighbor)
               if self._connects(start, neighbor, checked):
                  return True
      return False

   #country has other country, but other country doesn't have first country
   def _check_duplex(self, countries):
      for name in countries:
         neighbors = countries[name]
         for neighbor in neighbors:
            if not name in countries[neighbor]:
               msg = 'Non-duplex: %s has %s, but not vice-versa' % (name, neighbor)
               raise Exception(msg)

