'''game ideas: racing theme, characters are drivers, pit crew members, engineers, and team boss. these characters can receive upgrades. upgraded drivers are faster and more consistent meaning less incidents 
 like spinning out or crashing. upgraded pit crews add more pit crew members per upgrade, meaning faster pit stops. upgraded engineers mean a faster car with upgraded aerodynamics and engine. an upgraded
boss adds more consistency to pit stops and car upgrades. a lower level boss increases the chances of inconsistent pit stop times regardless of the number of members, and it can mean car upgrades may backfire
and make the car slower than before. events could be the race start, pit stops, and battles on sections of track such as straights, high speed, medium speed, and low speed corners. include safety car as cutscene.
safety car is most common pit stop time.'''

from typing import List

from project_code.src.Character import Character
from project_code.src.Event import Event
from project_code.src.Location import Location



class Game:
    def __init__(self):
        self.characters: List[Character] = ["Driver", "Pit crew", "Engineers"]
        self.locations: List[Location] = ["Race Track"]
        self.events: List[Event] = ["Race Start", "Straight battle", "High-speed corner battle", "Medium-speed corner battle", 
        "Low-speed corner battle", "Pit stop", "Safety car", "Crash", "Race finish"]
        self.party: List[Character] = ["Team Owner"]
        self.current_location = None
        self.current_event = None
        self._initialize_game()
        self.continue_playing = True

# Initalizes all upgrades and set race number to 1 before championship starts
class Driver:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

class Player_car:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

class Opponent_car:
    def __init__(self):
        self.level = 1

    def randomize_level(self):
        self.level = random.randint(1, 4)

class Pit_crew:
    def __init__(self, level):
        self.level = level

    def upgrade(self):
        if self.level < 4:
            self.level += 1

    def pit_stop_time(self):
        # Define pit stop time based on pit crew level
        if self.level == 1:
            return round(random.uniform(10, 15), 1)
        elif self.level == 2:
            return round(random.uniform(6, 10), 1)
        elif self.level == 3:
            return round(random.uniform(4, 8), 1)
        elif self.level == 4:
            return round(random.uniform(2, 3.5), 1)

class Race:
# Events that take place during the race
    def __init__(self):
        self.events = ['Straight battle', 'High speed corner battle', 'Medium speed corner battle',
                       'Low speed corner battle', 'Pit stop']

# Names of the races
    def get_race_name(self):
        race_names = ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix", "Belgian Grand Prix"]
        return random.choice(race_names)

# Race start
    def race_start(self):
        if random.random() < 0.9:  
            print("Race start successful!")
            return True
        else:
            print("DNF. You crashed with another driver and are out of this race.")
            return False

# Straight battle
    def straight_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        if random.random() < 0.025:
            print("DNF. You crashed trying a straight line overtake.")
            return "DNF"

        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        if player_driver.level >= 3 and player_car.level == opponent_car.level:
            print("Straight line overtake successful!")
            return "Player's car"
        elif player_car.level > opponent_car.level:
            print("Straight line overtake successful!")
            return "Player's car"
        elif player_car.level == opponent_car.level:
            print("Straight line overtake failed.")
            return "Opponent's car"
        else:
            print("Straight line overtake failed.")
            return "Opponent's car"

# Low speed corner battle
    def low_speed_corner_battle(self, player_driver, opponent_driver):
        if random.random() < 0.05:
            print("DNF. You crashed trying a low speed corner overtake.")
            return "DNF"

        opponent_driver.randomize_level()

        if player_driver.level > opponent_driver.level:
            print("Low speed corner overtake successful!")
            return "Player's car"
        elif player_driver.level == opponent_driver.level:
            print("Low speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("Low speed corner overtake failed.")
            return "Opponent's car"

# Medium speed corner battle
    def medium_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        if random.random() < 0.1:
            print("DNF. You crashed trying a medium speed corner overtake.")
            return "DNF"

        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        player_strength = (player_driver.level + player_car.level) / 2
        opponent_strength = (opponent_driver.level + opponent_car.level) / 2
        if player_strength > opponent_strength:
            print("Medium speed corner overtake successful!")
            return "Player's car"
        elif player_strength == opponent_strength:
            print("Medium speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("Medium speed corner overtake failed.")
            return "Opponent's car"

# High speed corner battle
    def high_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        if random.random() < 0.15: 
            print("DNF. You crashed trying a high speed corner overtake.")
            return "DNF"
        opponent_driver.randomize_level()
        opponent_car.randomize_level()

        player_strength = (player_driver.level * 0.25) + (player_car.level * 0.75)
        opponent_strength = (opponent_driver.level * 0.25) + (opponent_car.level * 0.75)
        if player_strength > opponent_strength:
            print("High speed corner overtake successful!")
            return "Player's car"
        elif player_strength == opponent_strength:
            print("High speed corner overtake failed.")
            return "Opponent's car"
        else:
            print("High speed corner overtake failed.")
            return "Opponent's car"

# Pit stop
    def pit_stop(self, player_pit_crew):
        pit_time = player_pit_crew.pit_stop_time()
        print(f"Player's pit stop time: {pit_time} seconds")

        return pit_time
# Run race
def run_race(self, player_driver, player_car, player_pit_crew):
        # Opponent setup
        opponent_driver = Driver()
        opponent_car = OpponentCar()

        if not self.race_start():
            return

        race_name = self.get_race_name()
        print(f"\nRace: {race_name}")

        print("Race started!")
        print(f"Player's driver level: {player_driver.level}, Player's car level: {player_car.level}")

        events = [self.straight_battle, self.low_speed_corner_battle, self.medium_speed_corner_battle,
                  self.high_speed_corner_battle, self.pit_stop] * 2  # Repeat each event twice

        random.shuffle(events)  # Shuffle event order

        for event in events:
            if event == self.pit_stop:
                pass 
            else:
                event_outcome = event(player_driver, player_car, opponent_driver, opponent_car)

                if event_outcome == "Crash":
                    break

        print("Race finish!")
def upgrade_menu(self, player_driver, player_car, player_pit_crew):
        print("\nUpgrade Menu:")
        print("1. Upgrade Driver")
        print("2. Upgrade Car")
        print("3. Upgrade Pit Crew")
        print("4. Continue to next race")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            player_driver.upgrade()
            print("Driver upgraded!")
        elif choice == "2":
            player_car.upgrade()
            print("Car upgraded!")
        elif choice == "3":
            player_pit_crew.upgrade()
            print("Pit Crew upgraded!")
        elif choice == "4":
            print("Continuing to next race...")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    game = RacingGame()
    num_races = 5  # Championship consists of 5 races
    player_driver = Driver()  # Player's driver starts at level 1
    player_car = Car()  # Player's car starts at level 1
    player_pit_crew = PitCrew(1)  # Player's pit crew starts at level 1

    for race in range(num_races):
        print(f"\nRace {race+1}")
        game.upgrade_menu(player_driver, player_car, player_pit_crew)
      
# Idk what this is
    def _main_game_loop(self):
        """The main game loop."""
        while self.continue_playing:
            pass
            # ask for user input
            # parse user input
            # update game state
            # check if party is all dead
            # if part is dead, award legacy points and end instance of game
            # if party is not dead, continue game
        if self.continue_playing is False:
            return True
        elif self.continue_playing == "Save and quit":
            return "Save and quit"
        else:
            return False
