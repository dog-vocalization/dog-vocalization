#!/usr/bin/python

import glob
import os

from spectrum_analysis import SpectrumAnalyzer
from sklearn import tree
from numpy import delete


def build_decision_tree():
    training_data, class_labels = build_dataset()
    clf = tree.DecisionTreeClassifier()

    clf.fit(training_data, class_labels)

    # training_data, class_labels, test_cases = get_test_cases(training_data, class_labels)
    # print test_cases
    # for mood, data in test_cases.iteritems():
    #     prediction = clf.predict_proba(data)
    #     prediction2 = clf.predict(data)
    #     print "Mood: {0}, prediction 1: {1}, prediction 2: {2}".format(mood, prediction, prediction2)

    with open(os.getcwd() + "/image_files/tree.dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)

    return clf

def build_dataset():
    dataset = []
    class_labels = []

    audacity_files = glob.glob(os.getcwd() + '/audio/audacity_files/*.txt')

    for file_name in audacity_files:
        with open(file_name, 'r') as file:
            data = file.readlines()[0].replace("\r", " ").replace("\t", " ").split()

            category = file_name.split("/")
            category = category[len(category) - 1].split("_")[0]

            spectrum = SpectrumAnalyzer(data, category)
            dataset.append(spectrum.training_data())
            class_labels.append(category)

    return dataset, class_labels

def get_test_cases(training_data, class_labels):
    test_cases = {}

    test_case_indexes = {}

    for count, category in enumerate(class_labels):
        if category not in test_case_indexes.keys():
            test_cases[category] = training_data[count]
            test_case_indexes[category] = count

    training_data = delete(training_data, test_case_indexes.values(), axis = 0)
    class_labels = delete(class_labels, test_case_indexes.values(), axis=0)

    return training_data, class_labels, test_cases

