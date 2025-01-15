# Hockey Game Simulator
This small program randomly simulates the scoring of a hockey game, played with Stanley Cup Playoff overtime rules. Ideal for helping you predict the winner of a game, be it for sports betting, a bracket challenge, or anything else!

### Installation
1. From the green Code dropdown, select Download ZIP.
2. Extract the full ZIP folder, then open the main.py file.

### How it works
1. At the start of the program, the user supplies the names of the teams, then sets the bias meridian (see below for more info).
2. At each 0.1 second, a random number between 0 and N-1 is drawn (N = the denominator of the odds of a goal being scored (1 / 6750 for regulation, 1 / 13,500 for overtime)). If the number drawn is 1, a goal was scored.
3. If a goal was scored, another random number between 0 and 99 is drawn.

| Value | Description |
| ----- | ----------- |
| < bias meridian | Home team scored |
| >= bias meridian | Away team scored |

#### Bias Meridian
- The % chance of the home team winning the game.
- Arbitrary number between 20 and 80

| Value | Description |
| ----- | ----------- |
| < 50 | Favours away team |
| 50 | Unbiased |
| > 50 | Favours home team |

> Less than 50: Favours away team.
> 50: Unbiased.
> Greater than 50: Favours home team.
