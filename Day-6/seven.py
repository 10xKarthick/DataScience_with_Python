from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import pandas
import csv

data = pandas.read_csv('spam', sep='\t', names=['v1','v2'])
train_data = data[:4400] # 4400 items
test_data = data[4400:] # 1172 items

classifier = OneVsRestClassifier(SVC(kernel='linear'))
vectorizer = TfidfVectorizer()

# train
vectorize_text = vectorizer.fit_transform(train_data.v2)
classifier.fit(vectorize_text, train_data.v1)

# score
vectorize_text = vectorizer.transform(test_data.v2)
score = classifier.score(vectorize_text, test_data.v1)
print(score) # 98,8


csv_arr = []
for index, row in test_data.iterrows():
    answer = row[0]
    text = row[1]
    vectorize_text = vectorizer.transform([text])
    predict = classifier.predict(vectorize_text)[0]
    if predict == answer:
        result = '-right'
    else:
        result = '-wrong'
    csv_arr.append([len(csv_arr), text, answer, predict, result])


# write csv
with open('test_score.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['#', 'text', 'answer', 'predict', result])

    for row in csv_arr:
        spamwriter.writerow(row)