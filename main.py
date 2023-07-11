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
        
 

         

        
        
        