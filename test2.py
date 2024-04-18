import tkinter as tk
from tkinter import scrolledtext  # Import scrolledtext for displaying text
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
        master.title("")  # Clear the default title

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

        # Create scrolled text widget to display race events and pit stop times
        self.text_area = scrolledtext.ScrolledText(master, width=50, height=20, wrap=tk.WORD)
        self.text_area.pack()

        # Center the title label
        self.title_label = tk.Label(master, text="Formula Python", font=("Arial", 16))
        self.title_label.place(relx=0.5, rely=0.05, anchor="center")  # Position in the middle of the top header

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
        # Clear previous race details from the screen
        self.text_area.delete('1.0', tk.END)

        # Opponent setup
        opponent_driver = Driver()
        opponent_car = Car()

        # Race start
        if not self.race_start():
            return

        race_name = self.get_race_name()
        self.text_area.insert(tk.END, f"\nRace: {race_name}\n")

        self.text_area.insert(tk.END, "Race started!\n")
        self.text_area.insert(tk.END, f"Player's driver level: {self.player_driver.level}, Player's car level: {self.player_car.level}\n")

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

        self.text_area.insert(tk.END, "Race finish!\n")
        self.num_races -= 1
        self.races_left_label.config(text="Races Left: {}".format(self.num_races))

        # Check if the game is over
        if self.num_races == 0:
            self.text_area.insert(tk.END, "Game Over!\n")
            self.master.destroy()
        else:
            self.upgrade_menu()

    def pit_stop(self, player_driver, player_car, player_pit_crew):
        self.text_area.insert(tk.END, "\nTime for a pit stop!\n")

        # Calculate pit stop time based on pit crew level
        pit_stop_time = player_pit_crew.pit_stop_time()
        self.text_area.insert(tk.END, f"Pit stop time: {pit_stop_time} seconds\n")

        # Simulate pit stop time
        self.text_area.insert(tk.END, "Executing pit stop...\n")
        for i in range(int(pit_stop_time)):
            self.text_area.insert(tk.END, f"{i+1} seconds...\n")
            self.master.after(1000)  # Delay for 1 second

        self.text_area.insert(tk.END, "Pit stop complete!\n")

    def upgrade_menu(self):
        self.upgrade_window = tk.Toplevel(self.master)
        self.upgrade_window.title("Upgrade Menu")

        button_width = 8  # Define the width of the buttons

        # Define a smaller font for the buttons and labels
        font_small = ('Arial', 8)

        self.upgrade_driver_button = tk.Button(self.upgrade_window, text="Upgrade Driver", command=self.upgrade_driver, width=button_width, font=font_small)
        self.upgrade_driver_button.pack(pady=2)

        self.upgrade_car_button = tk.Button(self.upgrade_window, text="Upgrade Car", command=self.upgrade_car, width=button_width, font=font_small)
        self.upgrade_car_button.pack(pady=2)

        self.upgrade_pit_crew_button = tk.Button(self.upgrade_window, text="Upgrade Pit Crew", command=self.upgrade_pit_crew, width=button_width, font=font_small)
        self.upgrade_pit_crew_button.pack(pady=2)

        self.continue_button = tk.Button(self.upgrade_window, text="Continue", command=self.upgrade_window.destroy, width=button_width, font=font_small)
        self.continue_button.pack(pady=2)

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
