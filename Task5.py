class SearchTrainer(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Gym:
    def __init__(self, list_of_sports, team_of_trainers, schedule, cost_of_training):
        self.info = {"Перелік видів спорту": list_of_sports,
                     "Команда тренерів": team_of_trainers,
                     "Розклад тренувань": schedule,
                     "Вартість тренування": cost_of_training,
                     }

    def search_info(self):
        while True:
            command = input(
                "1 - перелік видів спорту, 2 - команда тренерів, 3 - розклад тренувань, 4 - вартість тренування, 5 - пошук тренера, 0 - вихід:")
            if command == "1":
                print(self.info["Перелік видів спорту"])
            elif command == "2":
                print(self.info["Команда тренерів"])
            elif command == "3":
                print(self.info["Розклад тренувань"])
            elif command == "4":
                print(self.info["Вартість тренування"])
            elif command == "5":
                try:
                    trainer = input("Введіть ім'я тренера: ")
                    if trainer not in self.info["Команда тренерів"]:
                        raise SearchTrainer("Такого тренера немає в команді")
                    print(f"{trainer} буде в понеділок")
                except SearchTrainer as e:
                    print(e.message)

            elif command == "0":
                break
            else:
                print("Команда не знайден")

    def __str__(self):
        return f"{self.info}"


list_of_sports = ["football", "basketball", "tennis", "gym"]
team_of_trainers = ["Ivanov", "Petrov", "Sidorov"]
schedule = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
cost_of_training = 100

gym = Gym(list_of_sports, team_of_trainers, schedule, cost_of_training)
gym.search_info()
