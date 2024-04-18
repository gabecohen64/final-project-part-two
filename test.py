import tkinter as tk
import random

class Driver:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

class Car:
    def __init__(self):
        self.level = 1

    def upgrade(self):
        if self.level < 4:
            self.level += 1

class PitCrew:
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

class RacingGame:
    def __init__(self, master):
        self.master = master
        master.title("Formula Python")  # Change window title to "Formula Python"

        self.player_driver = Driver()
        self.player_car = Car()
        self.player_pit_crew = PitCrew(1)
        self.num_races = 5

        self.driver_label = tk.Label(master, text=f"Player's Driver Level: {self.player_driver.level}")
        self.driver_label.pack()

        self.car_label = tk.Label(master, text=f"Player's Car Level: {self.player_car.level}")
        self.car_label.pack()

        self.pit_crew_label = tk.Label(master, text=f"Player's Pit Crew Level: {self.player_pit_crew.level}")
        self.pit_crew_label.pack()

        self.races_left_label = tk.Label(master, text="Races Left: {}".format(self.num_races))
        self.races_left_label.pack()

        self.race_button = tk.Button(master, text="Race", command=self.run_race)
        self.race_button.pack()

    def race_start(self):
        if random.random() < 0.9:  
            print("Race start successful!")
            return True
        else:
            print("DNF. You crashed with another driver and are out of this race.")
            return False

    def get_race_name(self):
        race_names = ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix", "Belgian Grand Prix"]
        return random.choice(race_names)

    def run_race(self):
        # Opponent setup
        opponent_driver = Driver()
        opponent_car = Car()

        # Race start
        if not self.race_start():
            return

        race_name = self.get_race_name()
        print(f"\nRace: {race_name}")

        print("Race started!")
        print(f"Player's driver level: {self.player_driver.level}, Player's car level: {self.player_car.level}")

        # Events
        events = [self.straight_battle, self.low_speed_corner_battle, self.medium_speed_corner_battle,
                  self.high_speed_corner_battle, self.pit_stop] * 2  # Repeat each event twice
        random.shuffle(events)  # Shuffle event order

        for event in events:
            if event == self.pit_stop:
                event(self.player_driver, self.player_car, self.player_pit_crew)
            else:
                event_outcome = event(self.player_driver, self.player_car, opponent_driver, opponent_car)

                if event_outcome == "Crash":
                    break

        print("Race finish!")
        self.num_races -= 1
        self.races_left_label.config(text="Races Left: {}".format(self.num_races))

        # Check if the game is over
        if self.num_races == 0:
            print("Game Over!")
            self.master.destroy()
        else:
            self.upgrade_menu()

    def pit_stop(self, player_driver, player_car, player_pit_crew):
        print("\nTime for a pit stop!")

        # Calculate pit stop time based on pit crew level
        pit_stop_time = player_pit_crew.pit_stop_time()
        print(f"Pit stop time: {pit_stop_time} seconds")

        # Simulate pit stop time
        print("Executing pit stop...")
        for i in range(int(pit_stop_time)):
            print(f"{i+1} seconds...")
            self.master.after(1000)  # Delay for 1 second

        print("Pit stop complete!")

    def upgrade_menu(self):
        self.upgrade_window = tk.Toplevel(self.master)
        self.upgrade_window.title("Upgrade Menu")

        self.upgrade_driver_button = tk.Button(self.upgrade_window, text="Upgrade Driver", command=self.upgrade_driver)
        self.upgrade_driver_button.pack()

        self.upgrade_car_button = tk.Button(self.upgrade_window, text="Upgrade Car", command=self.upgrade_car)
        self.upgrade_car_button.pack()

        self.upgrade_pit_crew_button = tk.Button(self.upgrade_window, text="Upgrade Pit Crew", command=self.upgrade_pit_crew)
        self.upgrade_pit_crew_button.pack()

        self.continue_button = tk.Button(self.upgrade_window, text="Continue to Next Race", command=self.upgrade_window.destroy)
        self.continue_button.pack()

    def upgrade_driver(self):
        self.player_driver.upgrade()
        self.driver_label.config(text=f"Player's Driver Level: {self.player_driver.level}")
        self.upgrade_window.destroy()

    def upgrade_car(self):
        self.player_car.upgrade()
        self.car_label.config(text=f"Player's Car Level: {self.player_car.level}")
        self.upgrade_window.destroy()

    def upgrade_pit_crew(self):
        if self.player_pit_crew.level < 4:
            self.player_pit_crew.upgrade()
            self.pit_crew_label.config(text=f"Player's Pit Crew Level: {self.player_pit_crew.level}")
        else:
            print("Pit crew is already at maximum level.")
        self.upgrade_window.destroy()

    def straight_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        pass

    def low_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        pass

    def medium_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        pass

    def high_speed_corner_battle(self, player_driver, player_car, opponent_driver, opponent_car):
        pass

root = tk.Tk()
game = RacingGame(root)
root.mainloop()
