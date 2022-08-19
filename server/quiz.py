from question_types import *
import random
import json

class Quiz:

    questions: set[Question]

    def __init__(self, num_questions, question_types) -> None:
        self.num_questions = num_questions
        self.question_types = question_types
        self.questions = set()

    def generate_questions(self) -> None:
        for _ in range(self.num_questions):
            question = random.choice([IdentifiyProgressionModes(), IdentifyModeGivenNotes(), IdentifyNotesMode(), IdentifyNoteWithTones()])
            question.generate_random()
            self.questions.add(question)

    def print_questions(self) -> None:
        for question in self.questions:
            question.make_verbose()

    def get_total_marks(self) -> int:
        count = 0
        for question in self.questions:
            count += question.worth
        return count

    def export_json(self):
        questions_list = [question.get_dict_representation() for question in self.questions]
        quiz_data = {"Number of Questions": self.num_questions, "Total Marks": self.get_total_marks(), "Questions": questions_list}
        return json.dumps(quiz_data)



g = Quiz(4, "")
g.generate_questions()
g.print_questions()
print(g.export_json())