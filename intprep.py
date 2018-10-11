import numpy as np

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
    question_dict = {
    0: ["How would you rate you skill with Python on a scale from 1-10?", "How would you rate you skill with Python on a scale from 1-5?"],
    1: ["Whats your experience with PySpark?", 'How would you rate yourself with Spark on a scale from 1-10?', 'How would you rate yourself with Spark on a scale from 1-5?'],
    2: ["What's your experience with SQL?", 'How would you rate yourself with SQL on a scale from 1-10?', 'How would you rate yourself with SQL on a scale from 1-5?'],
    3: ["What is R2? What are other metrics that could be better than R2?"],
    4: ["What is the curse of dimensionality?"],
    5: ["Is more data always better?"],
    6: ["How can you determine which features are the most im- portant in your model?"],
    7: ["What are the advantages/disadvantages of GBM vs SVM?", "What are the advantages/disadvantages of GBM vs random forest?", "What are the advantages/disadvantages of logistic regression vs GBM?"],
    8: ["What is Spark/PySpark?", "What is distributed computing? When would you use it?"],
    9: ["Now you have a feasible amount of predictors, but you’re fairly sure that you don’t need all of them. How would you perform feature selection on the dataset?"],
    10: ["What is the main idea behind ensemble learning? If I had many different models that predicted the same response variable, what might I want to do to incorporate all of the models? Would you expect this to perform better than an individual model or worse?"],
    11: ["In an A/B test, how can you check if assignment to the various buckets was truly random?"],
    12: ["What might be the benefits of running an A/A test, where you have two buckets who are exposed to the exact same product?"],
    13: ["What would be the hazards of letting users sneak a peek at the other bucket in an A/B test?"],
    14: ["What would be some issues if blogs decide to cover one of your experimental groups?"],
    15: ["How would you run an A/B test for many variants, say 20 or more?"],
    16: ["How would you run an A/B test if the observations are extremely right-skewed?"],
    17: ["What is a p-value? What is the di erence between type-1 and type-2 error?"],
    18: ["What is maximum likelihood estimation? Could there be any case where it doesn’t exist?"],
    19: ["What is a confidence interval and how do you interpret it?"],
    21: ["What is unbiasedness as a property of an estimator? Is this always a desirable property when performing inference? What about in data analysis or predictive modeling?"],
    22: ["When can parallelism make your algorithms run faster? Slower?"],
    23: ["What are the different types of joins? What are the differences between them?"],
    24: ["Why might a join on a subquery be slow? How might you speed it up?"],
    25: ["Describe the difference between primary keys and foreign keys in a SQL database."]
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
