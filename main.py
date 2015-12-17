from pycloak import shellutils
import importlib
#TODO, varify biderection country

def get_random():
    return shellutils.read_file('/dev/urandom', 15, binary=True)

#subtract a list from a list
def sub_lst(lst, to_subtract):
    ret = []
    for item in lst:
        if not item in to_subtract:
            ret.append(item)
    return ret


class Country:
    def __init__(self, name, continent):
        self.name = name
        self.team = -1 #-1 = none, then 0-infinity
        self.continent = continent
        self.num_troops = 0

    def add_troops(self, n): #TODO: check
        self.num_troops += n
    def change_team(self, team): #TODO check
        self.team = team


class GameBoard:
    def __init__(self, countries, continents):
        self.neighbor_info = countries
        self.continents = continents
        self._run_map_tests()

        self.countries = {}
        for country in self.neighbor_info:
            self.contries[country] = Country(country, contitents[country])
            #self.troops[country] = 0

    def touching(self, c1, c2):
        self.check_exists(c1, c2)

    def check_exists(self, *countries):
        for country in countries:
            if self.neighbor_info.get(country, None) is None:
                raise Exception("Country doesn't exist: %s" % country)
                return False
        return True

    def _run_map_tests(self):
        self._check_self_neighbor(self.neighbor_info)
        self._check_neighbors_exist(self.neighbor_info)
        self._check_duplex(self.neighbor_info)
        self._check_pathways(self.neighbor_info)
        self._check_continents()

    def _check_continents(self):
        #TODO: implement continent checks, maybe move it to same structure as countries
        #make sure all countries in continent touch at least 1 other country in continent
        #make sure every country is part of continent
        #make sure they're not part of 2 different continents
        #make sure there isn't continents without countries
        pass

    def _check_neighbors_exist(self, countries):
        for country in countries:
            neighbors = countries.get(country, None)
            if neighbors is None or len(neighbors) == 0:
                raise Exception('Country cannot have empty neighbors')
            self.check_exists(*neighbors)

    def _check_self_neighbor(self, countries):
        for country in countries:
            neighbors = countries[country]
            for neighbor in neighbors:
                if country == neighbor:
                    raise Exception("Country '%s' cannot be it's own neighbor" % country)

    def _check_pathways(self, countries):
        for start in countries:
            for end in countries:
                if not self._connects(start, end, []):
                    raise Exception('Countries not connected: %s %s' % (start, end))

    def _connects(self, start, end, checked=[]):
        if start == end:
            return True
        if self.touching(start, end):
            return True
        else:
            end_neighbors = self.neighbor_info[end]
            for neighbor in end_neighbors:
                if self.touching(start, neighbor):
                    return True
                if not (neighbor in checked):
                    checked.append(neighbor)
                    if self._connects(start, neighbor, checked):
                        return True
        return False

    def _check_duplex(self, countries):
        for name in countries:
            neighbors = countries[name]
            for neighbor in neighbors:
                if not name in countries[neighbor]:
                    msg = 'Non-duplex: %s has %s, but not vice-versa' % (name, neighbor)
                    raise Exception(msg)

#TODO: Player needs access to GameBoard info,
#but GameBoard and Player are both part of Game
#Should we use inheritance or pass callbacks, etc?
class Player:
    def __init__(self):
        pass
    def chooseCountry(self, allCountries, freeCountries):
        pass
    def reinforce(self, ownCountries):
        self.chooseCountry = chooseCountryCallback
        #returns list of where it added people e.g. {'China': 1, 'US': 2}
#choice or automatic selection
class Game:
    def __init__(self, nPlayers, nCpus, chooseAuto=False):
        self.nPlayers = nPlayers
        self.nCpus = nCpus


    def
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
    m = GameBoard(countries, continents)
    return m

#importlib.reload(main)
a = main()

