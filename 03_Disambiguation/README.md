Holly Zhang (zhanghol)

LING-L545

Practical 03: Improve perceptron tagger


### 1. Initial Features:

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
----------:|:---------:|----------:|----------:|-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.23 |     96.23 |     96.23 |     96.23
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.23 |     96.23 |     96.23 |     96.23
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00


### 2. Changed Prefix to 3 Letters instead of 2

Changing the prefix to include three letters instead of two increased the prefomance a little.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.49 |     96.49 |     96.49 |     96.49
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.49 |     96.49 |     96.49 |     96.49
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00


### 3. Added Next Word's Prefix

The changed prefix length was kept as a feature when training the new model. Adding the next word's prefix as a feature did not further improve the model's performance. However, the current features are still better than the original ones.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
----------:|:---------:|----------:|----------:|-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.47 |     96.47 |     96.47 |     96.47
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.47 |     96.47 |     96.47 |     96.47
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00


### 4. Added Word+2 Suffix

For this model, the changed prefix length was included as a feature and the next word's prefix was left out since it didn not improve the model in 2. Adding the second next word's suffix did not improve the preformance when compared to model 2 as well. Though it did improve slightly compared to the original model.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
----------:|:---------:|----------:|----------:|-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.35 |     96.35 |     96.35 |     96.35
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.35 |     96.35 |     96.35 |     96.35
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00


### 5. Added i-2 Tag and Word

This model included the changed prefix length and the i-2 tag with the current word. There was a small improvment compared to the origninal features, but it has worse results than the models in 2 and 3.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
----------:|:---------:|----------:|----------:|-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.41 |     96.41 |     96.41 |     96.41
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.41 |     96.41 |     96.41 |     96.41
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00 


### 6. Includes All Explored Features

Combining all the features only improved the performance by a little. When compared to the other models, this is the second worst at tagging.

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
----------:|:---------:|----------:|----------:|-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.36 |     96.36 |     96.36 |     96.36
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.36 |     96.36 |     96.36 |     96.36
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
