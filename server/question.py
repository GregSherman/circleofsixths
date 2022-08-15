class Question:

    def __init__(self, prompt, answer, answer_inputs) -> None:
        self.prompt = prompt
        self.answer = answer
        self.answer_inputs = answer_inputs

    def make_verbose(self):
        print(self.prompt)
        print(self.answer_inputs)
        print("Answer: " + str(self.answer))