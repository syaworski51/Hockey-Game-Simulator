""" Hockey Game Simulator

Simulates a hockey game played with the overtime rules used in the Stanley Cup Playoffs.
"""

from classes import *

print('\n')

# Start by giving names to the teams
awayTeam = Team(input("Away team: "))
homeTeam = Team(input("Home team: "))

# The machine is responsible for determining whether a goal was scored at any given moment
# and printing out the score of the game
machine = Machine()

# Print a blank line
print()

# Odds of a goal being scored (1-in-6750)
odds = 6750

# While the period is less than 3, or if the score is tied...
period = 0
while period < 3 or awayTeam.score == homeTeam.score:
    # Increment the period at the start
    period += 1
    
    # If overtime has started, double the odds of a goal being scored
    if period == 4:
        odds *= 2

    # Time remaining in seconds (1200 seconds = 20 minutes)
    time = 1200.0

    # Print the score at the start of the period
    print(machine.printScore(period, time, awayTeam, homeTeam))
    print(machine.printSeparation())

    # While time is still running...
    while time > 0:
        # Determine whether a goal was scored
        goalScored = machine.wasGoalScored(odds)

        # If a goal was scored...
        if goalScored:
            # Determine which team scored the goal and increment the appropriate score
            homeTeamScored = machine.didHomeTeamScore()
            homeTeam.goal() if homeTeamScored else awayTeam.goal()

            # Print the new score
            print(machine.printScore(period, time, awayTeam, homeTeam))

        # If in overtime and the tie is now broken, the game is now over
        if period > 3 and awayTeam.score != homeTeam.score:
            print('\n')
            break

        # Decrement the time by 0.1s
        time -= 0.1
    
    # If in the 3rd period or eariler, OR if the score is tied
    if period <= 3 or awayTeam.score == homeTeam.score:
        # Print the score at the end of the period
        print(machine.printSeparation())
        print(machine.printScore(period, 0, awayTeam, homeTeam))
        print('\n')

# Now that the game is over, store the final score in this string
scoreString = f"{awayTeam.name} {awayTeam.score}, {homeTeam.name} {homeTeam.score}"

# If the game ended in overtime...
if period > 3:
    # Append a hyphen
    scoreString += " - "
    
    # If the game ended in the 1st overtime, add "OT"
    if period == 4:
        scoreString += "OT"
    # If the game ended after the 1st overtime, add "{2, 3, 4...}OT"
    else:
        scoreString += f"{period - 3}OT"

# Print the final score
print("FINAL SCORE")
print(scoreString + '\n\n')