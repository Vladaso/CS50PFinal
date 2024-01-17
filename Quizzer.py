from Question import Question
questions = [
    ["I like adventure.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["I enjoy crowds.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["I am active.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["How much free time do you have?", "Little to none", "Not enough", "Just about enough", "Plenty"],
    ["I am an extrovert.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["How many children do you have?", "0", "1", "2-3", "4+"],
    ["I love affection from my pets.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["I prefer loud environments with people.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["I have lots of energy.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
    ["I am curious.", "Strongly Disagree", "Disagree", "Agree", "Strongly Agree"],
]
class Quizzer:
    def __init__(self):
        self.questions = []
        for q in questions:
            self.questions.append(Question(q[0], q[1:]))
        