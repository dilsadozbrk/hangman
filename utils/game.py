import random
from typing import List


class Hangman(object):
    """The Hangman Game"""


    def __init__(self, lives: int = 5):
        """
        This function contains all the attributes which the game needs, it takes 1 argument
        :pram lives: The number of lives that the player still has left
        """
        self.lives = lives
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions', 'book', 'spring', 'travel',
                                          'cheese', 'computer']
        self.word_to_find: List[str] = [c for c in random.choice(self.possible_words)]
        self.correctly_guessed_letters: List[str] = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0


    def play(self):
        """
        This function checks if the user_input meets the given criteria, it uses the attributes of __init__ function.
        It checks if user input matches with the letter in word_to_find list and it adds this letter to
        correctly_guessed_letters.
        It also counts the number of error_count and lives
        """

        while True:
            user_input = input('Please enter a letter: ').lower()
            if user_input.isalpha() and len(user_input) == 1:
                if user_input in self.word_to_find:
                    print("it's correct!")
                    for i, c in enumerate(self.word_to_find):
                        if c == user_input:
                            self.correctly_guessed_letters[i] = user_input
                else:
                    print("Wrong guess!")
                    self.wrongly_guessed_letters.append(user_input)
                    self.error_count += 1
                    self.lives -= 1
                break


    def start_game(self):
        """
        This function is calling the play function to initialize the game.
        It checks if the player still has lives or the word is found.
        It increases turn_count when play function is called and
        also displays the info about the current situation of the game.
        """
        while True:
            self.play()
            self.turn_count += 1
            print(self.correctly_guessed_letters)
            print(self.wrongly_guessed_letters)
            print(self.lives)
            print(self.error_count)
            print(self.turn_count)
            if self.correctly_guessed_letters == self.word_to_find:
                self.well_played()
                break
            elif self.lives == 0:
                self.game_over()
                break


    def well_played(self):
        """
        This function displays the word which was correctly guessed and it also shows the attempt and error number
        """
        print('You found the word: {} in {} turns with {} errors!'.format(self.word_to_find, self.turn_count,
                                                                          self.error_count))

    def game_over(self):
        """
        It only displays if game ends
        """
        print("game over...")
