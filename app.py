import csv
from logging import raiseExceptions
from game_status import GameStatus

class Game:

    def __init__(self, max_of_attempts, path_to_file = r'C:\Users\admin1\Documents\TRUST_OR_NOT_GAMES\data\Questions.csv'):
        if max_of_attempts < 3:
            raise ValueError('The min count of attempts is 3')
        self.questions = {}
        self.answers = {}
        self.max_of_attempts = max_of_attempts
        self.path_to_file = path_to_file
        self.__game_status = GameStatus.IN_PROGRESS
        with open(path_to_file, 'r', newline='') as file:
            s = csv.reader(file, delimiter=';')
            i=1
            for row in s:
                self.questions[row[0]]= row[1]
                self.answers[i] = row[2] 
                i +=1  


    @property
    def status_of_game(self):
        return self.__game_status


    def next_question(self):
        return print(self.questions)

     
            