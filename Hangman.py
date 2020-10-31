######################################################################
# Author(s): Ahmed Abdulahi
# Username(s): abdulahia
#
# Assignment: P01 final project
#
# Purpose: The game of hangman: will invite the user to guess words from possible word bank and by guessing letter by
# letter the turtle will be drawing the hangman.
######################################################################
# Acknowledgements: Kite at Youtube and William Romano
# link of Youtube video : https://www.youtube.com/watch?v=m4nEnsavl6w&t=449s
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
##################################################################################
import turtle
from wordss import words
import random


class Hangman:
    """
    The player will given the chance to guess to guess the word in less then 6 tries before the hangman is
    fully drawn. In the game of hangman, the person is drawn in 6 parts which is why we have 6 pre drawn parts
    plus the tree.
    """

    def __init__(self):
        """

        :param mooley: our turtle that we would be using through out
        """

        super().__init__()
        self.mooley = turtle.Turtle()
        self.mooley.hideturtle()
        self.mooley.color("red")
        self.mooley.speed("fastest")

    def tree(self):
        """
        The tree where the hangman hangs from
        :return: None
        """

        self.mooley.penup()
        self.mooley.goto(-250, -100)
        self.mooley.pendown()
        self.mooley.goto(0, -100)
        self.mooley.goto(-150, -100)
        self.mooley.goto(-150, 150)
        self.mooley.goto(-0, 150)
        self.mooley.goto(0, 100)

    def draw_head(self):
        """
        the head of the hangman / first guess
        :return: None
        """

        self.mooley.penup()
        self.mooley.goto(0, 70)
        self.mooley.pendown()
        self.mooley.circle(15)

    def draw_body(self, ):
        """
        the body of the hangman / second guess
        :return:
        """
        self.mooley.goto(0, -20)

    def draw_left_leg(self):
        """
        the left leg of the hangman / third guess
        :return:
        """
        self.mooley.goto(-33, -50)

    def draw_right_leg(self,):
        """
        the right leg of the hangman / fourth guess
        :return:
        """
        self.mooley.penup()
        self.mooley.goto(0, -20)
        self.mooley.pendown()
        self.mooley.goto(33, -50)

    def draw_left_arm(self,):
        """
        the left arm of the hangman / fifth guess
        :return:
        """

        self.mooley.penup()
        self.mooley.goto(0, 40)
        self.mooley.pendown()
        self.mooley.goto(-33, 20)

    def draw_right_arm(self):
        """
        the right arm of the hangman / sixth guess
        :return:
        """
        self.mooley.penup()
        self.mooley.goto(0, 40)
        self.mooley.pendown()
        self.mooley.goto(33, 20)


class Game:
    """
    This is the game of hangman, where it all comes alive
    """

    def __init__(self):

        self.wn = turtle.Screen()
        self.wn.bgcolor("light blue")
        self.mooley = turtle.Turtle()
        self.mooley.color("red")

    def word(self):
        """
        Our random word that we will get everytime it runs
        :return:
        """
        random_word = random.choice(words)
        return random_word

    def fill_dash_lines(self,random_word):
        """
        dashes that represent the length of the word and fills out when they are right
        :return:
        """

        dash = "_" * len(random_word) # creates the dashlines based on length of the word
        print(dash)

# allow us to write on the turtle screen
    def write(self, txt):
        """
        Will write text on the turtle screen several times i.e when the player loses or wins
        :param txt: The text that writes on the screen
        :return: None
        """
        self.txt = txt
        self.mooley.hideturtle()
        self.mooley.penup()
        self.mooley.setpos(-120, -175)
        self.mooley.write(self.txt, move=False, align='center', font=("Arial", 30, "bold"))


def main():

    d = Hangman()
    d.tree()

    h1 = Game()

    word_chosen = h1.word()
    h1.write("_ " * len(word_chosen))

    h1.fill_dash_lines(word_chosen)
    guessed = False

    guesses = 6 # number of guesses allowed
    already_guessed = []
    while not guessed and guesses > 0:
        user = h1.wn.textinput("hangman", "guess a letter? ")

        if len(str(user)) == len(str(word_chosen)):
            if user == word_chosen:
                print(" you have won")

        if len(user) == 1:
            if user in word_chosen:
                print(" you guessed", user, "right")
                new_list = ""
                already_guessed.append(user)
                for letter in word_chosen:
                   if letter in user:
                       new_list += letter
                   else:
                       new_list += (" _ ")
                h1.write(new_list)
                if user == word_chosen:
                    print(" you have won")
            if user not in word_chosen:
                guesses -= 1
                if guesses == 5:
                    d.draw_head()
                if guesses == 4:
                    d.draw_body()
                if guesses == 3:
                    d.draw_left_leg()
                if guesses == 2:
                    d.draw_right_leg()
                if guesses == 1:
                    d.draw_left_arm()
                if guesses == 0:
                    d.draw_right_arm()
                    h1.write(20)
                    h1.write("YOU LOST, GAME OVER!!!")

        if guesses != 0 and "".join(already_guessed).strip() == word_chosen.strip():
            print(" you have won!")
            h1.write(" you have won")


if __name__ == '__main__':
    main()

