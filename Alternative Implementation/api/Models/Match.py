class Match:
    def __init__(self, matchID, team1, team2, round, date, tournamentID):
        self.matchID = matchID
        self.team1 = team1
        self.team2 = team2
        self.round = round
        self.date = date
        self.tournamentID = tournamentID

        self.started = False
        self.team1Score = 0
        self.team2Score = 0
