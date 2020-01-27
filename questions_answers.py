question_dict_tech = {
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
25: ["Describe the difference between primary keys and foreign keys in a SQL database."],
26: ["What is precision and recall?", "Why might accuracy not be a good metric to use? Give an example.", "How is True Positive Rate and Recall related? Write the equation."],
27: ["Explain how an ROC curve works."],
28: ["What is the difference between Type 1 and Type 2 error?"],
29: ["How would you handle an imbalanced dataset?"],
30: ["When would you use classification over regression?"],
31: ["How do you ensure that you're not overfitting a model?"],
32: [" What evaluation approaches would you work to gauge the effectiveness of a machine learning model?"],
33: ["Describe a hash table"],
34: ["How is KNN different from k-means clustering?"],
35: ["What’s the trade-off between bias and variance?"],
36: ["You are given a data set on cancer detection. You’ve build a classification model and achieved an accuracy of 96%. Why shouldn’t you be happy with your model performance? What can you do about it?"],
37: ["Why is Naive Bayes so naive?", "Explain prior probability, likelihood and marginal likelihood in context of naiveBayes algorithm?"],
38: ["What is multicollinearity?", "After analyzing the model, your manager has informed that your regression model is suffering from multicollinearity. How would you check if he’s true? Without losing any information, can you still build a better model?"],
39: ["While working on a data set, how do you select important variables? Explain your methods."],
40: ["Both being tree based algorithm, how is random forest different from Gradient boosting algorithm (GBM)?"],
41: ['What is Bayes Theorem?', 'Explain Bayes theorem.'],
42: ['What is the difference between a permutation and a combination?'],
43: ['What is variance?', 'What is covariance?', 'What is a correlation?'],
44: ['Describe the Central Limit Theorem.']
45: ['Describe the following statistical distributions and an example of when you would use it: Bernoulli, Binomial, Geometrics, Poisson, Exponential, Uniform, Gaussian.']
}

answer_dict_tech = {
    41: '''Baye's Rule describes the probability of an event occuring based on
        prior known knowledge that is related to the event. For example, if the probability that someone has cancer
        is related to their age, we can use Baye's theorem to more accurately assess the probability of cancer than
        if we did not have this information. Baye's theorem says that the probability of event B occurring given
        event A occurring is equal to the probability that event A occurs given event B * the probability of event B
        divided by the probability of event A.''',
    42: '''Permutations are the unique number of ways to choose k out of n (n!/(n-k)!).
        Combinations are the number of ways to choose k out of n (n![(n-k)!*k!]).

        '''
    43: '''Variance is the spread in a set of numbers. It is calculated as the the sum of (difference between the observation i and sample mean)^2
        Covariance is the measure of how much 2 random variables change together. It can identify relationships with positive, negative, or no trends. You never calculate covariance though, it is more of a stepping stone toward calculating correlation.
        Covariance is calculated as the sum of the product of the difference between the x observation minus the x sample mean * the y observation minus the y sample mean / n. If the covariance is positive, the trend is positive.
        Correlation quantifies the strength of a relationship between 2 variables. Correlation is between -1 (negative) and 1 (positive). A correlation of 0 means that there is no relationship between the data.
        Correlation is calculated as the covariance of x,y / (sqrt of the variance x / sqrt of the variance of y)
        R^2 quantifies the difference that a linear function fits data better or worse than a line of the mean. It is equal to the var(mean) - var(line) / var(mean)
        ''',
    44: ''' ''',
    45: '''Distributions can be thought of as a histogram or mathematical function that describes the relationship between sample observations.
        It is the shape that can calculate the probability of observing a given observation in a sample space.
        Once a distribution function is known, it can be used as a shorthand for describing and calculating related quantities, such as likelihoods of observations, and plotting the relationship between observations in the domain.
        Bernoulli: Single coin flip;
        Binomial: Number of coin flips out of 100 that turn out to be heads;
        Geometric: Number of trials until a coin turns up as heads;
        Poisson: A rare event occurs, number of events occurring in fixed interval of time or space. number of taxis passing a street corner in given hour;
        Exponential: Time between poisson events, Time until taxi passes a street corner;
        Uniform: degrees between hours on a clock;
        Gaussian: Commonly occurring distribution shaped like a bell curve. Related to the central limit theorem. student test scores, IQ scores;
        '''

}
