from classifier import Classifier
import time
class Validator:
    def __init__(self, dataset):
        self.classifier = Classifier()
        self.classifier.get_df(dataset)
    def evaluate(self, features):
        if(len(features) == 0):
            count1 = 0
            count2 = 0
            for point in self.classifier.df:
                if(point[0] == 1):
                    count1 += 1
                if(point[0] == 2):
                    count2 += 1
            if(count1 > count2):
                return count1 / (count1 + count2)
            else:
                return count2/ (count1 + count2)
        start_time = time.time()
        test_labels = []
        #will find accuracy of classifier given feature subset
        for i in range(len(self.classifier.df)):
            res = self.classifier.KNearest(i, features, 1)
            test_labels.append(res)
        acc = self.classifier.accuracy(test_labels)
        #print(f"Accuracy of the classifier with features {features} is {acc * 100}%. \n\t The program finished running in {time.time() - start_time} seconds.")
        return acc

# validator = Validator("small-test-dataset.txt")
# validator.evaluate([3, 5, 7])