class RaceHorse:
    def __init__(self, speed, age, name):
        self.speed = speed
        self.age = age
        self.name = name
        self.placeInRace = None

    def __str__(self):
        return f"Name: {self.name}, Speed: {self.speed}, Age: {self.age}, Place in Race: {self.placeInRace}"
    

class Race:
    def __init__(self):
        self.participants = []

    def add_horse(self, horse):
        if 3 <= horse.age <= 7:
            self.participants.append(horse)
        else:
            print(f"Horse {horse.name} does not meet the age requirement (3-7 years)")

    def remove_horse(self, name):
        self.participants = [horse for horse in self.participants if horse.name != name]
    
    def determine_winner(self):
        if not self.participants:
            print("No participants in the race.")
            return None

        avg_age = sum(horse.age for horse in self.participants) / len(self.participants)
        winner = max(self.participants, key=lambda horse: (horse.speed, -abs(horse.age - avg_age)))
        return winner

    def sort_by_speed(self):
        self.participants.sort(key=lambda horse: horse.speed, reverse=True)
        for i, horse in enumerate(self.participants[:3], start=1):
            horse.placeInRace = i

    def display_participants(self):
        for horse in self.participants:
            print(horse)

class Horse:
    def __init__(self, age, base_xp, speed):
        self.age = age
        self.base_xp = base_xp
        self.speed = speed
        self.current_xp = self.calculate_xp()
    
    def calculate_xp(self):
        # Розрахунок XP на основі віку коня
        if self.age < 5:
            return self.base_xp * 1.2
        elif 5 <= self.age < 10:
            return self.base_xp
        else:
            return self.base_xp * 0.8

class Steroid:
    def __init__(self, cost, speed_boost, xp_loss):
        self.cost = cost
        self.speed_boost = speed_boost
        self.xp_loss = xp_loss

class RaceWithEntryFee:
    def __init__(self, entry_fee):
        self.entry_fee = entry_fee
        self.prize = 0  

    def set_prize(self, prize):
        self.prize = prize

    def apply_steroids(self, horse, steroid):
        if steroid.cost >= 0.5 * self.entry_fee:
            print("Стероїди занадто дорогі для цього забігу.")
            return False

        horse.speed += steroid.speed_boost
        horse.current_xp -= steroid.xp_loss
        if horse.current_xp < 0:
            print("Кінь загинув через втрату XP.")
            return False

        print(f"Швидкість після застосування стероїдів: {horse.speed}")
        print(f"XP після втрати: {horse.current_xp}")
        return True


# Використання класів
horse = Horse(age=7, base_xp=100, speed=50)
steroid = Steroid(cost=20, speed_boost=15, xp_loss=10)
race_with_entry_fee = RaceWithEntryFee(entry_fee=100)
race_with_entry_fee.set_prize(200) 
race_with_entry_fee.apply_steroids(horse, steroid)

def main():
    race = Race()

    horse1 = RaceHorse(50, 5, "McQueen")
    horse2 = RaceHorse(48, 4, "Hudson Hornet")
    horse3 = RaceHorse(52, 6, "Storm")
    horse4 = RaceHorse(45, 8, "Guido")  

    race.add_horse(horse1)
    race.add_horse(horse2)
    race.add_horse(horse3)
    race.add_horse(horse4)

    print("Participants before sorting:")
    race.display_participants()

    winner = race.determine_winner()
    if winner:
        print(f"\nWinner: {winner}")
    race.sort_by_speed()

    print("\nParticipants after sorting by speed:")
    race.display_participants()

main()