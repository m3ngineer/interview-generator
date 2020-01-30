question_dict_tech = {
0: ["How would you rate you skill with Python on a scale from 1-10?", "How would you rate you skill with Python on a scale from 1-5?"],
1: ["Whats your experience with PySpark?", 'How would you rate yourself with Spark on a scale from 1-10?', 'How would you rate yourself with Spark on a scale from 1-5?'],
2: ["What's your experience with SQL?", 'How would you rate yourself with SQL on a scale from 1-10?', 'How would you rate yourself with SQL on a scale from 1-5?'],
3: ["What is R2? What are other metrics that could be better than R2?"],
4: ["What is the curse of dimensionality?"],
5: ["Is more data always better?"],
6: ["How can you determine which features are the most important in your model?"],
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
17: ["What is a p-value? What is the difference between type-1 and type-2 error?"],
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
40: ["Both being tree based algorithm, how is random forest different from Gradient boosting algorithm (GBM)?", "Describe random forest algorithm. What are its strengths and limitations?"],
41: ['What is Bayes Theorem?', 'Explain Bayes theorem.'],
42: ['What is the difference between a permutation and a combination?'],
43: ['What is variance?', 'What is covariance?', 'What is a correlation?'],
44: ['Describe the Central Limit Theorem.']
45: ['Describe the following statistical distributions and an example of when you would use it: Bernoulli, Binomial, Geometrics, Poisson, Exponential, Uniform, Gaussian.'],
46: ['Calculate the variance of the following population: 10, 12, 34, 24'],
47: ['How would you prove that a coin is unfair'],

}

answer_dict_tech = {
    3: '''R^2 quantifies the difference that a linear function fits data better or worse than a line of the mean. It is equal to the var(mean) - var(line) / var(mean) or 1 - RSS/TSS, where RSS=sum(yi-yhat)^2 and TSS=sum(yi-ybar)^2. An R2 value of 0.9 means that 90% of the variation in the data is explained by the line.
    Adjusted R^2 takes into account the number of predictors in the model, since R2 will always increase when more predictors are added. adjusted R-squared increases only if the new term improves the model more than would be expected by chance.
    ''',
    26: '''Precision = TP/(TP + FP) - Out of everything that called positive, how many are actually positive?
    Recall = TP/(TP + FN) - Out of everything that is actually positive, how many did you catch?;
    F1 = 2TP/(2TP + FP + FN) - harmonic mean of recall and precision. Combination of everything that is actually positive, how many did you catch and how many are actually positive?
    Sensitivity = TPR = TP/P (hit rate, recall)
    Specificity = TNR = TN/N
    Sensitivity and Specificity are inversely proportional to one another.
    FPR = 1 - specificity
    ROC = Plot of FPR vs TPR. As FPR and TPR are inversely proportional and come at the expense of one another
    AUC = . If AUC = 0.7, there is a 70% chance the model will be able to distinguish between positive and negative classes.
    ROC Curves summarize the trade-off between the true positive rate and false positive rate for a predictive model using different probability thresholds.
Precision-Recall curves summarize the trade-off between the true positive rate and the positive predictive value for a predictive model using different probability thresholds.
    ROC curves are appropriate when the observations are balanced between each class, whereas precision-recall curves are appropriate for imbalanced datasets.

    ''',
    28: '''Type 1 error: false positive (FP), false alarm;
        Type 2 error: false negative (FN), miss;''',
    29: '''Undersampling: Remove data labeled 0. The disadvantage is that we reduce the size of our dataset. One way to get around this is by ensembling models that each uses a different sample of common class label and all of the rare class label. You can take the majority vote of all of these models.
        Oversampling: Add more positive data points by picking existing samples with replacement via  1) SMOTE (synthetic minority oversampling technique): generate similar points around the original data 2) ADASYN (adaptive synthetic sampling approach for imbalanced learning). You can also create a generative model to create new samples. Oversampling can be computationally expensive and algorithmically more involved.
        Combined: keep 1/3 of the of negative-labeled data, use SMOTE to increase positive-labeled data
        Set hyperparameters: You can use hyperparamters to set the weights. This will give more weight to the underrepresented class. For example in XGBoost you can set the scale_pos_weight to be 10 if you have a 10:1 imbalance in the dataset. For Random Forest you can set the class_weight formula.
        ''',
    35: '''
        A model's prediction error is composed of bias + variance + irreducible error. The bias-variance tradeoff states that a simple model will have high bias and low variance, and as it becomes more complex will have high variance and low bias. High bias models tend to be more generalizable (bias) and underfit because they are unable to capture the underlying pattern in the data. A high variance model may overfit because it captures the noise in the data as a pattern. The more flexible the model, the greater the variance.
        High bias (underfitting) models can miss relevant relationships between features and target outputs. High variance (overfitting) models can be sensitive to noise in the training data, rather than the intended target.
        Some strategies for dealing with reducing variance for linear regression are to subset the selection of predictors stepwise, use regularization, project the predictors into a lower dimensional space.
        Simpler models tend to underfit (logistic and linear regression), while more complex models tend to overfit (GBM, decision trees, RF).
        ''',
    40: '''Decision trees can be grown as a forest by bootstrapping our dataset (pick with replacement). While growing each of our trees we can randomly select only an m subset of the variables features at each split. This creates variability in the trees and decorrelates them.
        With bootstrapping ~1/3 of the data is left out of every tree. This out of bag data can be used to estimate the out of bag error.
        Boosting: Combine weak learners to create strong learners. Sequentially apply weak classification algorithms to modified versions of the data
        ''',
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
        R^2 quantifies the difference that a linear function fits data better or worse than a line of the mean. It is equal to the var(mean) - var(line) / var(mean) or 1 - RSS/TSS, where RSS=sum(yi-yhat)^2 and TSS=sum(yi-ybar)^2. An R2 value of 0.9 means that 90% of the variation in the data is explained by the line.
        ''',
    44: '''The central limit theorem says that the mean of samples collected from any distribution are normally distributed. Therefore, it doesn't matter what distribution type the samples came from.
        Because the sample means will always be normally distributed we can make inferences about the CI, and perform t-tests or ANOVA between the sample means''',
    45: '''Distributions can be thought of as a histogram or mathematical function that describes the relationship between sample observations.
        It is the shape that can calculate the probability of observing a given observation in a sample space.
        Once a distribution function is known, it can be used as a shorthand for describing and calculating related quantities, such as likelihoods of observations, and plotting the relationship between observations in the domain.
        Bernoulli: Single coin flip;
        Binomial: Number of coin flips out of 100 that turn out to be heads;
        Geometric: Number of trials until a coin turns up as heads;
        Poisson: A rare event occurs, number of events occurring in fixed interval of time or space. number of taxis passing a street corner in given hour;
        Exponential: Time between poisson events, Time until taxi passes a street corner;
        Uniform: equal probabilities of selecting values from 0-1. degrees between hours on a clock;
        Gaussian: Commonly occurring distribution shaped like a bell curve. Related to the central limit theorem. student test scores, IQ scores;
        '''

}
