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
    
    def __init__(self, name, players):
        """
        Initialize a Team object with the provided attributes.
        
        Args:
            name (str): The name of the team.
            players (list): The list of Player objects representing the team's players.
        """
        self.name = name 
        self.players = players 
        self.captain = None 
        self.batting_order = players.copy()
        self.bowlers = []

    def select_captain(self, captain):
        """
        Select the captain for the team.
        
        Args:
            captain (Player): The Player object representing the captain of the team.
        """
        self.captain = captain

    def sending_next_player(self):
        """
        Send the next player from the batting order.
        
        Returns:
            Player or None: The next Player object from the batting order, or None if the batting order is empty.
        """
        if len(self.batting_order)>:
            return self.batting_order.pop(0)
        return None 
    
    def choose_bowler(self):
        """
        Choose a bowler randomly from the team's bowlers.
        
        Returns:
            Player: The Player object representing the chosen bowler.
        """
        return random.choice(self.bowlers)
    

class Field:
    """
    This class will contain factors like field size, fan ratio, pitch conditions, home advantage, etc., which can impact the probabilities of the simulation.

    """
    
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage
        
        
class Umpire:
    """
    This class will be responsible for chunking probabilities of all the players on the field and predicting the outcome of a ball. The Umpire class will also keep track of scores, wickets, and overs. It can also make decisions on LBWs, catches, no-balls, wide-balls, etc.
    
    """
    
    def __init__(self, team1, team2, field):
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0
    
    def update_score(self, runs):
        """
        Update the score based on the runs scored.
        
        Args:
            runs (int): The runs scored in the ball.
        """
        self.scores += runs

    def update_wickets(self):
        """
        Update the wickets count.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the overs count.
        """
        self.overs += 1
    
    def predict_outcome(self, batsman, bowler):
        """
        Predict the outcome of a ball based on batsman and bowler stats.
        
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
        
        Returns:
            str: The outcome of the ball (either "OUT" or "NOT OUT").
        """
        batting_prob = batsman.batting * self.field.pitch_conditions * random.random()
        bowling_prob = bowler.bowling * self.field.pitch_conditions * random.random()
        if batting_prob > bowling_prob:
            return "OUT"
        return "NOT OUT"

class Commentator:
    """
    This class will provide commentary for each ball and over. It can use the match stats to give a description of the ongoing game events.

    """
    def __init__(self, umpire):
        self.umpire = umpire
    
    def describe_ball(self, batsman, bowler):
        """
        Generate a description of the ball played by the batsman.
        
        Args:
            batsman (Player): The Player object representing the batsman.
            bowler (Player): The Player object representing the bowler.
        
        Returns:
            str: The description of the ball played by the batsman.
        """
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print("Outcome: ", outcome)
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!"
        else:
            description = f"{batsman.name} plays the shot."

        return description

    def describe_game(self, captain1, captain2, country1, country2, over):
        """
        Provide a description of the cricket match.
        
        Args:
            captain1 (str): The name of the captain of the first team.
            captain2 (str): The name of the captain of the second team.
            country1 (str): The name of the first team.
            country2 (str): The name of the second team.
            over (int): The total number of overs in the match.
        """
        print("\n--------- Game Information ---------\n")
        print(f"{country1} Vs {country2}")
        print(f"Captain 1 : {captain1}, Captain 2 : {captain2}")
        print(f"Over : {over}")
        print("\n---------------------------------------------\n")

    def describe_start(self, team):
        """
        Provide a description of the start of an innings.
        
        Args:
            team (str): The name of the team currently batting.
        """
        print("\n------------- GAME STARTED ------------------\n")
        print(f"Team {team} playing: ")
    
    def describe_end(self):
        """
        Provide a description of the end of an innings.
        """
        print(f"\n\nFinal Run: {self.umpire.scores} Wicket: {self.umpire.wickets} Overs: {self.umpire.overs}")
        print("\n---------------------------------------------\n")

    
    def current_info(self, ball_count):
        """
        Provide the current match information.
        
        Args:
            ball_count (int): The count of balls played in the current over.
        """
        print(f"Balls: {ball_count} Over: {self.umpire.overs} Run: {self.umpire.scores}  Wicket: {self.umpire.wickets}")

    def describe_final_result(self, name, scores):
        """
        Provide a description of the final result of the match.
        
        Args:
            name (str): The name of the winning team.
            scores (int): The```
            score achieved by the winning team.
        """
        print("--------------- Winner -----------------------")
        print(f"TEAM : {name} WON BY SCORE: {scores}")
        print("\n---------------------------------------------\n")
    

class Match:
    """
     This class will simulate an individual cricket match. It will use objects of the Teams, Field, and Umpire classes and should have methods to start the match, change innings, and end the match.

    """
    
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(field)
        self.commentator = Commentator(self.umpire)
        self.total_overs = total_overs

    
    def start_match(self):
        """
        Starts the cricket match.
        """
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.describe_game(self.team1.captain.name, self.team2.captain.name, self.team1.name, self.team2.name, over=self.total_overs)

        # Team 1 playing    
        self.commentator.describe_start(self.team1.name)
        self.play_innings(self.team1, self.team2)
        self.commentator.describe_end()
        lastScores = self.commentator.umpire.scores


        # Team 2 playing    
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_start(self.team2.name)
        self.play_innings(self.team2, self.team1)
        self.commentator.describe_end()
        newScores = self.commentator.umpire.scores
        # Final outcome
        if lastScores > newScores:
            self.commentator.describe_final_result(team1.name, lastScores)
        else:
            self.commentator.describe_final_result(team2.name, newScores)


    def play_innings(self, batting_team, bowling_team):
        """
        Simulates the innings of a team.
        
        Args:
            batting_team (Team): The Team object representing the batting team.
            bowling_team (Team): The Team object representing the bowling team.
        """
        ball_count = 1
        over = 0
        bowler = bowling_team.choose_bowler() 
        batsman = batting_team.sending_next_player()
        while over < self.total_overs:
            print("\n")
            self.commentator.current_info(ball_count)
            ball_description = self.commentator.describe_ball(batsman, bowler)
            
            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.sending_next_player()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"Wickets: {self.umpire.wickets} , Overs: {self.umpire.overs}")
                print(f"New player {batsman.name} is playing...")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"Over {over} Starting...")
                self.umpire.update_overs()
                bowler = bowling_team.choose_bowler()
                ball_count = 0

            self.commentator.current_info(ball_count)
            ball_count += 1



# Creating dummy data
# Adding players

player1 = []
for i in range(10):
    player1.append(Player("Player1_"+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)))

player2 = []
for i in range(10):
    player2.append(Player("Player2_"+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)))

# Adding players to the team
team1 = Team("Country1", player1)
team2 = Team("Country2", player2)

# showing the field
field = Field("Large", 0.7, 0.8, 0.9)

# starting match simulation
total_overs = 2
match = Match(team1, team2, field, total_overs)
match.start_match()
    

        
    
    
        
 

         

        
        
        
