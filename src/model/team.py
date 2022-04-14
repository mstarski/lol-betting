class Team:
    def __init__(self, name, rating):
        self.name = self._handleNameExceptions(name)
        self.rating = float(rating)

    
    # There's a difference between names returned from Lolpedia and LeagueOfElo library
    # i.e Rogue

    # Private
    def _handleNameExceptions(self, name):
        if name == "Rogue (European Team)":
            return "Rogue"
        else:
            return name


