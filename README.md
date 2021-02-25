# Capstone 1: [eSports Winnings](https://www.kaggle.com/jackdaoud/esports-earnings-for-players-teams-by-game)

## Dataset

This data was pulled from [eSportsEarning.com](https://www.esportsearnings.com/) and has info for players and teams in different tournaments.

### Struggles with Dataset:

* No way to link the Teams df with the other df's

* Teams df doesn't include a count of players splitting the earnings

* 

## Visualizations

* Prize share between games:

![Prize Share](images/pie_prize_share.png)

* Average team prize per game:

![Prize per team](images/average_team_prize_per_game.png)

* Average player prize per game:

![Prize per player](images/barh_players_prize_per_game.png)

* Showing price per tournament grouped by genre:

![Genre Players](images/barh_players_prize_per_genre.png)

* Split out prize per player for games by genre:

![Prize per player](images/avg_prize_per_team_by_genre.png)

* Prize totals per country:

![Prize per country](images/barh_conrties_prize_total.png)

* Prize averages per country:

![Prize total per country](images/barh_conrties_prize_total.png)

## Possible Hypothesis

* First-Person Shooters pay more per player
* It makes more sense for someone to compete in games that do not have teams, or have small teams
    * Possible issue since I can't get consistent answer on players per game or size of the team without more data
* 

## To-do's:

* Scrape site for more data
    * What games certain teams focus on
    * Does allocating time and energy to a specific game or genre have a significant impact on prize earnings

## References:

* Site that holds all this information typically --> https://www.esportsearnings.com/

