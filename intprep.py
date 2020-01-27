import numpy as np

from questions_answers import question_dict_tech, answer_dict_tech

def pick_nontech(num_questions=1):
  question_dict = {
    0: ["Tell me about yourself. How did you get here?"],
    1: ["Why are you interested in this position?", "What are you looking for in your next position?"],
    2: ["Why this company?", "What do you know about this company?"],
    3: ["Have you done any exploratory data analysis?"],
    4: ["Tell me about a project that you've done.", "Tell me about a time that you used data to make an actionable decision", "What were your aha moments when you built your model?", "What was your process for testing your model?"],
    5: ["How large was the datasets you've worked with?"],
    6: ["What are your salary expectations?"],
    7: ["What's something that you're proud of?"],
    8: ["What are your greatest strengths? greatest weaknesses?"],
    9: ["What are your long-term goals?"],
    10: ["How would you increase company revenue?"],
    11: ["What would you do if you had an unlimited data? What kinds of questions would you try to answer?"],
    12: ["Describe a time when you used data to evaluate and change a campaign."],
    13: ["Do you have any questions for me?"]
  }

  used = []
  i = 1
  while i <= num_questions:
      choice = np.random.choice(len(question_dict))
      if choice not in used:
          used.append(choice)
          i += 1
          related_questions = question_dict[choice]
          question = related_questions[np.random.choice(len(related_questions))]
          print(question)
          input('')

def pick_tech(num_questions=1):

    used = []
    i = 1
    while i <= num_questions:
      choice = np.random.choice(len(question_dict))
      if choice not in used:
          used.append(choice)
          i += 1
          related_questions = question_dict[choice]
          question = related_questions[np.random.choice(len(related_questions))]
          print(question)
          input('')

if __name__ == '__main__':
    question_type = input('Tech or nontech questions?:').lower()
    print(question_type)
    while question_type not in ['tech', 'nontech']:
        print('Please choose tech or nontech')
        question_type = input('Tech or nontech questions?:').lower()

    num_questions = int(input('Number of questions:'))
    while num_questions >= 15:
        print('Please choose a number below 15')
        num_questions = int(input('Number of questions:'))

    if question_type == 'tech':
        pick_tech(num_questions=num_questions)
    elif question_type == 'nontech':
        pick_nontech(num_questions=num_questions)
