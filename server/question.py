class Question:

    def __init__(self) -> None:
        self.prompt = ""
        self.answer = ""
        self.answer_inputs = []
        self.worth = 0
    
    def get_dict_representation(self) -> list:
        return {"Prompt": self.prompt, "Answer": self.answer, "Worth": self.worth, "Answer Inputs": self.answer_inputs}

    def make_verbose(self):
        print(self.prompt)
        print(self.answer_inputs)
        print("Answer (worth " + str(self.worth) + "): " + str(self.answer) + "\n\n")