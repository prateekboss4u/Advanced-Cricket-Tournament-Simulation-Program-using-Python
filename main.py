class Player:
    """
        This class should contain information on player stats, such as:

        name (e.g., "MS Dhoni")
        bowling: 0.2
        batting: 0.8
        fielding: 0.99
        running: 0.8
        experience: 0.9
        <etc>
        
        These player stats should be used when running the simulation and should affect the probabilities of various events occurring like a boundary, getting out, etc.
    """
        
    def __init__(self, name, bowling, batting, fielding, running, experience):
        
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience
        
    
class Teams:
    """
    A team will consist of players. It should have methods like selecting the captain, sending the next player to the field, choosing a bowler for an over, deciding batting order, etc.
    
    """
    
    def __init__(self, name):
        self.name = name
        self.team = []
        self.captain = None
         
    def add_player(self, player):
        self.team.append(player)
        
    def select_captain(self, player):
        self.captain = player
    
    def send_next_player(self):
        pass

    def choose_bowler(self):
        pass
    
    def decide_batting_order(self):
        pass
    

class Field:
    """
    This class will contain factors like field size, fan ratio, pitch conditions, home advantage, etc., which can impact the probabilities of the simulation.

    """
    
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage
        
        
class Umpire:
    """
    This class will be responsible for chunking probabilities of all the players on the field and predicting the outcome of a ball. The Umpire class will also keep track of scores, wickets, and overs. It can also make decisions on LBWs, catches, no-balls, wide-balls, etc.
    
    """
    
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.score = 0
        self.wickets = 0
        self.overs = 0
    
    def simulate_ball(self):
        pass
    
    def update_score(self, runs):
        self.score += runs
    
    def update_wickets(self):
        self.wickets += 1
    
    def update_overs(self):
        self.overs += 1

class Commentator:
    """
    This class will provide commentary for each ball and over. It can use the match stats to give a description of the ongoing game events.

    """
    def __init__(self, umpire):
        self.umpire = umpire
    
    def provide_commentary(self):
        pass
    

class Match:
    """
     This class will simulate an individual cricket match. It will use objects of the Teams, Field, and Umpire classes and should have methods to start the match, change innings, and end the match.

    """
    
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(team1, team2, field)
        self.commentator = Commentator(self.umpire)
    
    def start_match(self):
        pass
    
    def change_innings(self):
        pass
    
    def end_match(self):
        pass
    

        
    
    
        
 

         

        
        
        