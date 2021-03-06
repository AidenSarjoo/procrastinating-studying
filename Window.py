# Import modules
import sys
import random
from tkinter import *
from PIL import Image, ImageTk


class BaseWindow:
    def __init__(self, tk):
        # Import classes
        self.questions = Questions()

        # Initialize the tkinter window
        self.tk = tk

        # Quit button (runs quit function)
        self.quit_button = Button(self.tk, text="Quit", command=self.quit)
        self.quit_button.grid(row=0, column=0)

        # Initialize question frame
        self.question_frame = Frame(self.tk, width=1000, height=1000)
        self.question_frame.grid(row=1, column=0)

        # Initialize choice frame
        self.choice_frame = Frame(self.tk)
        self.choice_frame.grid(row=2, column=0)

        #Options
        self.choice = StringVar()
        self.choice_a = Radiobutton(self.choice_frame, text="A", variable=self.choice, value="a")
        self.choice_a.pack()
        self.choice_b = Radiobutton(self.choice_frame, text="B", variable=self.choice, value="b")
        self.choice_b.pack()
        self.choice_c = Radiobutton(self.choice_frame, text="C", variable=self.choice, value="c")
        self.choice_c.pack()
        self.choice_d = Radiobutton(self.choice_frame, text="D", variable=self.choice, value="d")
        self.choice_d.pack()
        self.choice_e = Radiobutton(self.choice_frame, text="E", variable=self.choice, value="e")
        self.choice_e.pack()
        self.choices_list = [self.choice_a, self.choice_b, self.choice_c, self.choice_d, self.choice_e]
        #self.clear_choices()
        # Puts the image on the screen
        self.display_question()

        self.submit_button = Button(self.choice_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        print(self.questions.q_list)
        print(self.questions.q_map)

    def quit(self):
        """
        Closes the tkinter window and then exits the script
        """
        # Closes tkinter window
        self.tk.destroy()
        # Closes the script
        sys.exit()

    def clear_choices(self):
        for x in self.choices_list:
            x.deselect()

    def display_question(self):
        self.curr_question = self.questions.pick_question()
        image_filepath = 'Questions/' +self.curr_question+'.PNG'

        img = Image.open(image_filepath)
        question_pic = ImageTk.PhotoImage(img)

        label1 = Label(self.question_frame, image=question_pic)
        label1.image = question_pic
        label1.pack()

    def check_answer(self):
        if self.questions.q_map[self.curr_question] == self.choice:
            print('good job',self.questions.q_map[self.curr_question],self.choice)
        else:
            print('idiot',self.questions.q_map[self.curr_question],self.choice)

    def display_answer(self):
        img = Image.open("Questions\Q1key.PNG")
        question_pic = ImageTk.PhotoImage(img)

        label1 = Label(self.question_frame, image=question_pic)
        label1.image = question_pic
        label1.pack()

class Questions:
    def __init__(self):
        # Set file name for key
        self.key_file_name = "QuestionMap.txt"
        # Set answer key dictionary
        self.q_map = self.read_key()
        # Set list of questions
        self.q_list = self.list_questions()

    def read_key(self):
        """
        Iterates through the question list file, splitting each line into a dictionary key:value pair, the key being
        the question name and the value being the answer
        """
        # Open the file
        question_list = open(self.key_file_name, "r")
        lst = []
        dic = {}

        # Reads every line of the file and splits each line into a list of the Q# ([0]) and answer ([1]), appending
        # the lists into a list
        for question in question_list:
            question = question.strip()
            question = question.split(':')
            lst.append(question)

        # Maps the list to a dictionary, the first item being the key and the second being the value
        for question in range(len(lst)):
            dic[lst[question][0]] = lst[question][1]

        # Close your file
        question_list.close()

        # lol
        return dic

    def list_questions(self):
        """
        Iterates through the question list file and saves each question to a list
        """

        # Opens the file
        question_list = open(self.key_file_name, "r")
        lst = []

        # Appends each Q# from the file into a list
        for question in question_list:
            question = question[0:question.find(":")]
            lst.append(question)

        # Close your file
        question_list.close()

        # lol
        return lst

    def pick_question(self):
        """
        Randomly picks a question from the list of questions, then pops it
        """

        # Randomly picks a question from the question list
        question = random.choice(self.q_list)
        # Removes the chosen question so it can't be chosen again
        self.q_list.pop()
        # lol
        return question


def main():
    # Creating the tkinter window
    window = Tk()
    # Naming the tkinter window
    window.title("Question!")
    # Running the class
    App = BaseWindow(window)
    # Initializing tkinter
    window.mainloop()


if __name__ == "__main__":
    main()
