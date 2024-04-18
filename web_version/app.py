from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)


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
        if self.level == 1:
            return round(random.uniform(10, 15), 1)
        elif self.level == 2:
            return round(random.uniform(6, 10), 1)
        elif self.level == 3:
            return round(random.uniform(4, 8), 1)
        elif self.level == 4:
            return round(random.uniform(2, 3.5), 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_race', methods=['POST'])
def run_race():
    player_driver = Driver()
    player_car = Car()
    player_pit_crew = PitCrew(1)

    race_events = []

    # Race start
    if random.random() < 0.9:
        race_events.append("Race start successful!")
    else:
        race_events.append("DNF. You crashed with another driver and are out of this race.")
        return jsonify({'events': race_events})

    race_name = random.choice(
        ["British Grand Prix", "Italian Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix", "Belgian Grand Prix"])

    race_events.append(f"Player's driver level: {player_driver.level}, Player's car level: {player_car.level}")

    # Events
    events = [straight_battle, low_speed_corner_battle, medium_speed_corner_battle,
              high_speed_corner_battle, pit_stop] * 2
    random.shuffle(events)

    for event in events:
        if event == pit_stop:
            pit_stop_time = player_pit_crew.pit_stop_time()
            race_events.append(f"Pit stop time: {pit_stop_time} seconds")
            race_events.append("Executing pit stop...")
            for i in range(int(pit_stop_time)):
                race_events.append(f"{i + 1} seconds...")
            race_events.append("Pit stop complete!")
        else:
            event_outcome = event(player_driver, player_car, Driver(), Car())
            if event_outcome == "Crash":
                break

    return jsonify({'race_name': race_name, 'player_driver_level': player_driver.level,
                    'player_car_level': player_car.level, 'events': race_events})


def straight_battle(player_driver, player_car, opponent_driver, opponent_car):
    pass


def low_speed_corner_battle(player_driver, player_car, opponent_driver, opponent_car):
    pass


def medium_speed_corner_battle(player_driver, player_car, opponent_driver, opponent_car):
    pass


def high_speed_corner_battle(player_driver, player_car, opponent_driver, opponent_car):
    pass


def pit_stop(player_driver, player_car, player_pit_crew):
    pass


if __name__ == '__main__':
    app.run()
