from quizmanager import QuizManager

class QuizApp:
    # Please enter Quiz folder path
    QUIZ_FOLDER = "Enter quiz folder path containing XML file"

    def __init__(self):
        self.username = ""
        self.result = None
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        self.greeting()
        self.username = input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()
    
    def greeting(self):
        print("\n\n Welcome to PyQuiz! \n\n")
    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")
        print("After finishing the test please make selection for exit as 'E")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-------------")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-------------")

    def menu(self):
        self.menu_header()
        selection = ""
        while (True):
            selection = input("Selection?(please select from menu options only!) ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()
            if selection[0] == 'E':
                self.goodbye()
                break
            elif selection[0] == 'M':
                self.menu_header()
                continue
            elif selection[0] == 'L':
                print("\nAvailable Quizzes Are:")
                self.qm.list_quizzes()
                print("----------------------------------\n")
                continue
            elif selection[0] == 'T':
                try:
                    quiznum = int(input("Quiz number: "))
                    print(f"You've selected quiz {quiznum}")
                    self.result = self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                    dosave = input("Save the results? (y/n): ")
                    dosave = dosave.capitalize()
                    if (len(dosave) > 0 and dosave[0] == 'Y'):
                        self.qm.save_results()
                except:
                    self.menu_error()
            else:
                self.menu_error()

    def run(self):
        self.startup()
        self.menu()

if __name__ == "__main__":
    app = QuizApp()
    app.run()
