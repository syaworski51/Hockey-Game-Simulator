from random import *

class Team:
    """ Represents one of the teams. """
    
    def __init__(self, name:str):
        """ Create a new instance of the Team object.

        Parameters:
            - name (string): The name of this team.
        """
        self.name = name
        self.score = 0
    
    def goal(self):
        """ When this team scores a goal, add 1 point to their score. """
        self.score += 1

    def resetScore(self):
        """ Reset this team's score to 0. """
        self.score = 0



class Machine:
    """ Represents the machine that prints the score of the game. """

    def printSeparation(self):
        """ Print a series of hyphens for separation. """
        return "----------------------------------------------------------"

    def printScore(self, period:int, time:float, awayTeam:Team, homeTeam:Team):
        """ Print the current score of the game.

        Parameters:
            - period: The current period.
            - time: The time remaining in the period in seconds.
            - awayTeam: The away team in this game.
            - homeTeam: The home team in this game.
        """

        minute = time // 60
        second = time % 60
        periodString = f"P{period}"

        if period > 3:
            if period == 4:
                periodString = "OT"
            else:
                periodString = f"{period - 3}OT"
        
        if minute == 0:
            if second < 10:
                return f"{periodString}\t {time:.1f}\t{awayTeam.name} {int(awayTeam.score)}, {homeTeam.name} {int(homeTeam.score)}"

            return f"{periodString}\t{time:.1f}\t{awayTeam.name} {int(awayTeam.score)}, {homeTeam.name} {int(homeTeam.score)}"

        if minute < 10:
            if second < 10:
                return f"{periodString}\t {int(minute)}:0{int(second)}\t{awayTeam.name} {int(awayTeam.score)}, {homeTeam.name} {int(homeTeam.score)}"

            return f"{periodString}\t {int(minute)}:{int(second)}\t{awayTeam.name} {int(awayTeam.score)}, {homeTeam.name} {int(homeTeam.score)}"
        
        if second < 10:
            return f"{periodString}\t{int(minute)}:0{int(second)}\t{awayTeam.name} {int(awayTeam.score)}, {homeTeam.name} {int(homeTeam.score)}"

        return f"{periodString}\t{int(minute)}:{int(second)}\t{awayTeam.name} {int(awayTeam.score)}, {homeTeam.name} {int(homeTeam.score)}"

    def wasGoalScored(self, odds:int):
        """ Was there a goal scored?
        Generate a random number between 0 and {odds}.
        If the number is 1, a goal was scored.

        Parameters:
            - odds: The 1-in-{odds} chance of a goal being scored.
        
        Returns:
            True if a goal was scored (random # == 1)
            False otherwise.
        """
        goal = randint(0, odds - 1)
        return goal == 1
    
    def didHomeTeamScore(self):
        """ Did the home team score a goal?
        Generate a random number between 0 and 100.
        If the number is even, the home team scored a goal.
        Otherwise, the away team scored a goal.

        Returns:
            True if the home team scored a goal (random # is even).
            False if the away team scored a goal.
        """
        team = randint(0, 100)
        return team % 2 == 0