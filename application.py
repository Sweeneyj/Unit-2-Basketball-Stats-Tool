import constants
import copy
import random
import sys

if __name__ == '__main__':
  
#6 players a team with 3 experience on each, Need to show team name as string, total palyers on that team, and the player names as strings separated by commas. 

  my_player_list = copy.deepcopy(constants.PLAYERS)
  teams = copy.deepcopy(constants.TEAMS)

  experienced_players = []
  inexperienced_players = []
  
  panthers = []
  bandits = []
  warriors = [] 


  def clean_data():
    for player in my_player_list:
      player["height"] = int(player["height"][0:2])
    
      if player["experience"] == "YES":
        experience = True
        player["experience"] = experience
        experienced_players.append(player["name"])
      else:
        experience = False 
        player["experience"] = experience
        inexperienced_players.append(player["name"])
            
            
  def balance_teams(team):
    while len(experienced_players) != 0 and len(team) < 3:
      team.append(experienced_players.pop(random.randrange(0, len(experienced_players))))
    while len(inexperienced_players) != 0 and len(team) < 6:
      team.append(inexperienced_players.pop(random.randrange(0, len(inexperienced_players))))
     

  clean_data()
  balance_teams(panthers)
  balance_teams(bandits)
  balance_teams(warriors)

  def main_function():
    print("BASKETBALL TEAM STATS TOOL") 
    print("---- MENU ----") 
    while True:
      try:
        main_menu = int(input("Please select from the following options:\n 1) Display Team Stats\n 2) Quit\n"))
        if main_menu == 2:
          print("Thanks for playing!")
          break
        if main_menu == 1:
          team_menu = True
          while team_menu:
            team_select = int(input("Please select the team via 1, 2, or 3. Alternatively, you can quit selecting the number 4. \n 1) Panthers\n 2) Bandits \n 3) Warriors\n 4) Quit\n"))
            if team_select == 1:
              print("Team Name: Panthers")
              print("Team Size: {}".format(len(panthers)))
              panther_roster = "Players: " + panthers[0] + ", " + panthers[1] + ", " + panthers[2] + ", " + panthers[3] + ", " + panthers[4] + ", " + panthers[5]
              print(panther_roster)
              teamn_menu = False
            elif team_select == 2:
              print("Team Name: Bandits")
              print("Team Size: {}".format(len(bandits)))
              bandit_roster = bandits[0] + ", " + bandits[1] + ", " + bandits[2] + ", " + bandits[3] + ", " + bandits[4] + ", " + bandits[5]
              print(bandit_roster)
              continue
            elif team_select == 3:
              print("Team Name: Warriors")
              print("Team Size: {}".format(len(warriors)))
              warrior_roster = warriors[0] + ", " + warriors[1] + ", " + warriors[2] + ", " + warriors[3] + ", " + warriors[4] + ", " + warriors[5]
              print(warrior_roster)
              continue
            elif team_select == 4: 
              print("Thanks for hanging out")
              sys.exit()
            else:
              print("That is not a valid input, please try again")
              continue
      except ValueError:
        print("Sorry, not a valid input! Please select 1 or 2")

  main_function()
                     
                      



