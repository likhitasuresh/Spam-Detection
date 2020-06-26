# Spam-Detection

## Aim
This project aims at utilizing the Naive Bayes classifier to perform a binary text classification task -  spam detection.

## Experiment
The training set of over 1000 CSV files with tokenized and labeled email bodies was provided to the NB classifier. 

## Learning the model
NB classfier largely relies on calculating probabilities of occurences as well as conditional probabilities of tokens. In this project, our aim was to keep track of P(spam), P(ham), P(token|spam) and P(token|ham).

A second model was developed with an additional feature, feature being smoothing. In this project, add one smoothing was used.

## Enhancement to the model
This project also intented to experiment with additional enhancements to observe the effects they had on the overall precision of the model. Some of these enhancements were:
* Tokens always must being with a letter or a digit.
* Igonring common words such as derterminers and prepositions.
* Ignoring tokens of length 2 and lesser.

## Precision, Recall and F1 scores of the model

"*In pattern recognition, information retrieval and classification (machine learning), precision (also called positive predictive value) is the fraction of relevant instances among the retrieved instances, while recall (also known as sensitivity) is the fraction of the total amount of relevant instances that were actually retrieved. The two measures are sometimes used together in the F1 Score (or f-measure) to provide a single measurement for a system.*"
-Wikipedia (Precision and Recall)

* Performance on the development data with 100% of the training data.
  * spam precision: 0.99
  * spam recall: 0.98
  * spam F1 score: 0.99
  * ham precision: 0.95
  * ham recall: 0.98
  * ham F1 score: 0.96

* Performance on the development data with 10% of the training data
  * spam precision: 0.98
  * spam recall: 0.94
  * spam F1 score: 0.95
  * ham precision: 0.86
  * ham recall: 0.95
  * ham F1 score: 0.90

* Best performance results based on enhancements - *Tokens always must being with a letter or a digit.*
  * spam precision: 0.99
  * spam recall: 0.98
  * spam F1 score: 0.99
  * ham precision: 0.96
  * ham recall: 0.99
  * ham F1 score: 0.98

