# Hockey Game Simulator
This small program randomly simulates the scoring of a hockey game, played with Stanley Cup Playoff overtime rules. Ideal for helping you predict the winner of a game, be it for sports betting, a bracket challenge, or anything else!

### How it works
1. At the start of the program, the user supplies the names of the teams.
2. At each 0.1 second, a random number between 0 and N-1 is drawn (N = the denominator of the odds of a goal being scored (1 / 6750 for regulation, 1 / 13,500 for overtime)). If the number drawn is 1, a goal was scored.
3. If a goal was scored, another random number between 0 and 99 is drawn; even #'s = home team scored, odd #'s = away team scored.

Currently, the simulator is unbiased, meaning that both teams are equally likely to score a goal at any second.
In the future, I may add a bias feature where the user can make the simulation biased towards one team, especially if that team is significantly better than the other.
