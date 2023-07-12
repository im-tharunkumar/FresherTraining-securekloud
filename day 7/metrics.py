from sklearn import metrics
from nltk.translate.bleu_score import sentence_bleu
from sklearn.metrics import roc_auc_score, precision_recall_curve, auc
from jiwer import wer



y_true=[1,0,1,1,1,0,0,1,1,0]
y_pred=[1,1,1,0,1,0,1,0,1,1]
print("confusion matrix:\n",metrics.confusion_matrix(y_true,y_pred,labels=[1,0]))
print("precision:\n",metrics.precision_score(y_true,y_pred))
print("recall:\n",metrics.recall_score(y_true,y_pred))
print("f1 score:\m",metrics.f1_score(y_true,y_pred))


reference = [['this', 'is', 'a', 'score'], ['this', 'is' ,'bleu','score']]
candidate = ['this', 'is', 'a', 'bleu','score']
print("bleu score:\n",sentence_bleu(reference, candidate))

reference = ['The cat is on the mat']
candidate = 'The cat is on the mat'
print(sentence_bleu([reference], candidate))

ground_truth = [1, 0, 1, 1, 0, 1]
predicted_probabilities = [0.8, 0.6, 0.2, 0.9, 0.4, 0.7]

# Calculate AUC/ROC
auc_roc = roc_auc_score(ground_truth, predicted_probabilities)

# Calculate Precision-Recall Curve
precision, recall, _ = precision_recall_curve(ground_truth, predicted_probabilities)
auc_prc = auc(recall, precision)

print("AUC/ROC:", auc_roc)
print("AUC PRC:", auc_prc)

reference = "hello world good night moon"
hypothesis = "hello world good day sun"
print("word error rate:\n",wer(reference, hypothesis))