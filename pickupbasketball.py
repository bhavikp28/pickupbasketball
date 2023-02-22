import math
import random
# function to calculate the total rating of a team
def team_rating(team):
    return sum(player[2] for player in team)

# function to balance the teams by swapping players
def balance_teams(num_teams, players):
    # calculate number of players per team
    num_players = len(players)
    players_per_team = math.ceil(num_players / num_teams)

    # calculate number of centers per team
    num_centers = sum(player[1] == 'C' for player in players)
    centers_per_team = math.ceil(num_centers / num_teams)

    # sort players by rating in descending order
    players.sort(key=lambda x: x[2], reverse=True)

    # initialize empty teams
    teams = [[] for i in range(num_teams)]

    # assign centers to teams
    for i in range(num_teams):
        centers_assigned = 0
        j = 0
        while centers_assigned < centers_per_team and j < len(players):
            if players[j][1] == 'C':
                teams[i].append(players[j])
                players.pop(j)
                centers_assigned += 1
            else:
                j += 1

    # assign remaining players to teams
    for i in range(num_teams):
        players_assigned = len(teams[i])
        while players_assigned < players_per_team and players:
            teams[i].append(players.pop())
            players_assigned += 1

    # balance teams by swapping players
    while True:
        # calculate total rating of each team
        team_ratings = [team_rating(team) for team in teams]
        avg_rating = sum(team_ratings) / num_teams

        # find team with highest rating
        max_rating_team = max(range(num_teams), key=lambda i: team_ratings[i])

        # find player in max rating team with highest rating
        max_rating_player = max(teams[max_rating_team], key=lambda x: x[2])

        # find team with lowest rating
        min_rating_team = min(range(num_teams), key=lambda i: team_ratings[i])

        # find player in min rating team with lowest rating
        min_rating_player = min(teams[min_rating_team], key=lambda x: x[2])

        # check if swapping the players would make the teams more balanced
        if abs((team_ratings[max_rating_team] - max_rating_player[2] + min_rating_player[2]) - avg_rating) < abs(team_ratings[max_rating_team] - avg_rating):
            # swap players
            teams[max_rating_team].remove(max_rating_player)
            teams[min_rating_team].remove(min_rating_player)
            teams[max_rating_team].append(min_rating_player)
            teams[min_rating_team].append(max_rating_player)
        else:
            break

    return teams, team_ratings

# get number of teams from user
num_teams = int(input("Enter number of teams: "))

# players list
# players = [['P1','C',5],['P2','PG',4]]
players = [['P1','C',5],
           ['P2','PG',5],
           ['P3','C',5],
           ['P4','PG',5]]

# balance the teams
teams, trating = balance_teams(num_teams, players)

# print the teams
for i, team in enumerate(teams):
    print(f"Team {i+1}:")
    for player in team:
        print(f"{player[0]} ({player[1]}, {player[2]})")
    print()
print(trating)
