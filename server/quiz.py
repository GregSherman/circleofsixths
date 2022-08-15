from question import *


class Quiz:

    def __init__(self, questions, answers) -> None:
        
        self.questions = questions
        self.answers = answers
        self.num_questions = len(self.questions)

    def export_json(self):
        pass
