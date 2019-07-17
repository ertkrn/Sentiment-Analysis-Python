# Sentiment-Analysis-Python
This Python Project is integrated into the bilvideo web application. It provides the categorization of comments to videos as positive or negative.

## Sentiment Analysis

During the design of the system, emotion analysis of the comments made on the videos in the system was made and it was decided to determine whether the attitude towards the issue was positive, negative or neutral. The process of commenting is as follows:
 * When a user comments on a video via the client, it is first registered in the database and then the request is sent to "../api/getcomments".
 * The final comment made upon this request is drawn and the relevant comment is subjected to emotion analysis.

Emotion classification techniques that can be used to analyze emotions are given in Figure 1 below.

![techniques](https://user-images.githubusercontent.com/37222672/61375848-920fec80-a8a8-11e9-9500-dde6d2a285a0.png)

It is determined that one of the techniques "Generalized Linear Models" which you have seen above, "Logistic Regression" will be used for emotion analysis. Logistic Regression Analysis is preferred to other methods used to explain the relationship between variables when the dependent variable is categorical. The most important reason for this is that the independent variables are suitable for the multivariate normal distribution and can be used without the need for important assumptions such that the variance covariances of the known groups are homogeneous.
Since the subject of application is happiness, it is appropriate to use Logistic Regression Method in this study. Logistic Regression Analysis can be examined in 3 different groups as Binary Logistic Regression, Multinomial Logistic Regression and Ordinal Logistic Regression according to the nature of the dependent variable. However, the existence of a rank among the categories of happiness, which is a dependent variable due to the nature of the data, requires the use of Ordinal Logistics Regression Method.

Let's get to know some terms related to logistic regression:

**Odds, odds ratio and lojit** 

These terms are important basic terms in logistic regression.
 * **Odds:** The "p" of success or probability is "1-p" to the probability of failure or invisibility.
 * **Odds Ratio(OR):** The ratio of two odds to each other. It is a summary measure of the relationship between two variables.
 * **Lojit:** It is the natural logarithm of the odds ratio. Odds ratio is asymmetric. It is converted into a symmetric state by taking its natural logarithm.
 
 General representation of Logistic Regression model can be done as follows;
 
 ![logistic-regression](https://user-images.githubusercontent.com/37222672/61376498-fed7b680-a8a9-11e9-80a5-e655a2aa22a3.png)

The logistic model, which is also referred to as a cumulative logitical model, is generally used cumulatively because the intercategorical comparison can be performed well. Because as can be seen from the formula odds ratio; The probability of falling into the lower category is obtained by proportioning the probability of falling into the higher category.

In line with this information, let's talk about "pandas", "numpy" and "sklearn" which are necessary libraries for emotion analysis in Python. "pandas" is used to open the Csv and text files and read the data contained in it to reach the desired result easily. So we can open an excel file and select a column or row. The shaping of the data made in the Numpy library can be used in more detail. "numpy" is a python library written to facilitate scientific computing. Computational operations are often performed when studying machine learning, image processing and artificial intelligence. The code structure, which is commonly used in computational and conversion processes, is designed with the numpy library at a simple level and with little code. "scikit-learn", linear regression, logistic regression, decision trees, this library contains many basic methods such as random forest. It is a frequently used library because it performs mathematical operations very fast. The analysis phase is as follows:

 * There are 21000 data sets (comments). This data set in ".csv" format is read with pandas.
 * The Turkish fill words in the data set are removed. These fill words "wonder, but, also" and so on. such as words that do not add any emotion.
 * The first 15000 comments in our dataset are added to the data to be trained positively.
 * The first training data is obtained using the "CountVectorizer", which converts the data into a frequency matrix of passing characteristics.
 * The obtained data is trained with LogisticRegression classifier.
 * Trained data is tested with the "predict" API included in scikit-learn.
 * The tf-idf vectorizer was launched and applied to the training data. tf-idf is based on subtracting the terms in a text and performing various calculations based on the amount of such terms.
 * The training set, which specifies a minimum frequency of 5 documents and extracts 1 gram and 2 grams, was relocated. bigrams count pairs of adjacent words. It can give features like bad and not bad.
 
The screen outputs at the time of the training are as follows.
 
![D_egitim1](https://user-images.githubusercontent.com/37222672/61376858-b40a6e80-a8aa-11e9-8d9b-5e6418427327.png)
 
Title of training data and number of columns
 
![D_egitim2](https://user-images.githubusercontent.com/37222672/61376859-b40a6e80-a8aa-11e9-907c-cd8b022d4d30.png)
 
Evaluation and interpretation of results
 
![D_egitim3](https://user-images.githubusercontent.com/37222672/61376861-b40a6e80-a8aa-11e9-98c3-d62067f9c2e2.png)
 
Results of tf-idf calculations
 
![D_egitim4](https://user-images.githubusercontent.com/37222672/61376862-b4a30500-a8aa-11e9-8cc1-a1c45e3f1f21.png)

Negative and positive words related to coefficient
