#!/usr/bin/python

from audio.audio_mood import AudioMood
from numpy import delete

from sklearn import tree
import pydot
import os
import csv

from sklearn.externals.six import StringIO


"""
Uses a decision tree classifier to build a feature-matching model, 
then trains the fit of the training data with our class labels.

Contains test cases which generate probability-based classification predictions 
"""
def run_analysis(audio_files = None, file_name = ""):

    if not audio_files and not file_name:
        print "run_analysis requires at least one parameter. None given."
        return

    if audio_files:
        training_data, class_labels = import_training_data(audio_files)
    else:
        training_data, class_labels = read_training_data(file_name)

    training_data, class_labels, test_cases = generate_test_cases(training_data, class_labels)

    if audio_files:
        save_training_data(training_data, class_labels)

    clf = tree.DecisionTreeClassifier()
    clf.fit(training_data, class_labels)

    print "Finished training learning tree"

    for mood, data in test_cases.iteritems():
        prediction = clf.predict_proba(data)
        prediction2 = clf.predict(data)
        print "Mood: {0}, prediction 1: {1}, prediction 2: {2}".format(mood, prediction, prediction2)

    # dot_data = StringIO()
    # tree.export_graphviz(clf, out_file=dot_data)
    # graph = pydot.graph_from_dot_data(dot_data.getvalue())
    # graph.write_pdf(os.getcwd() + "/tree.pdf")


"""
Build a set of test cases to be evaluated by the run analysis step.

Returns training data, class labels, and test cases.
"""
def generate_test_cases(training_data, class_labels):
    test_cases = {}

    test_case_indexes = {}

    for count, category in enumerate(class_labels):
        if category not in test_case_indexes.keys():
            test_cases[category] = training_data[count]
            test_case_indexes[category] = count

    training_data = delete(training_data, test_case_indexes.values(), axis = 0)
    class_labels = delete(class_labels, test_case_indexes.values(), axis=0)

    print "Test cases: {0}".format(test_cases)
    return training_data, class_labels, test_cases


"""
Extract training data from the audio_files passed to this function.
Categorizes extracted data by a corresponding mood.

Returns training data and class_labels
"""
def import_training_data(audio_files):
    training_data = []
    class_labels = []

    for mood_category, data in audio_files.iteritems():
        class_labels.extend([ mood_category ] * (len(data)))

        mood = AudioMood(mood_category, data)
        mood_dataset = mood.generate_dataset()
        training_data.extend(mood_dataset)

    return training_data, class_labels


"""
Reads training data from csv file by class label

Returns training data and class_labels
"""
def read_training_data(file_name):
    training_data = []

    with open(os.getcwd() + file_name) as csvfile:
        reader = csv.reader(csvfile)
        csv_list = list(reader)

    class_labels = csv_list[0]
    for i in range(1, len(csv_list)):
        training_data.append(csv_list[i])

    return training_data, class_labels


"""
Writes training data to a csv as class labels and audio track data.
"""
def save_training_data(training_data, class_labels):
    with open(os.getcwd() + "/training_data.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(class_labels)
        for index, song_data in enumerate(training_data):
            writer.writerow(song_data)
