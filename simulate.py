#!/usr/bin/env python

from __future__ import division
import os

num_students = raw_input('Number of students [100]: ')
if num_students == '':
    num_students = 100
else:
    num_students = int(num_students)


num_cheaters = raw_input('Number of cheaters [5]: ')
if num_cheaters == '':
    num_cheaters = 5
else:
    num_cheaters = int(num_cheaters)


def simulate(num_students, num_cheaters):
    answersY = 0
    answersN = 0

    for i in range(0, num_students):
        rand = ord(os.urandom(1))
        if rand < 128: # Heads on first throw
            if i < num_cheaters:
                answersY += 1
            else:
                answersN += 1
        else: # Tails on first throw
            if rand < 192: # Heads on second throw
                answersY += 1
            else: # Tails on second throw
                answersN += 1

    return (answersY, answersN)

totalAnswersY = 0
totalAnswersN = 0

num_simulations = 1000

for i in range(0, num_simulations):
    (answersY, answersN) = simulate(num_students, num_cheaters)
    totalAnswersY += answersY
    totalAnswersN += answersN

avgAdmittances = str(totalAnswersY / num_simulations)
avgPercAdmittances = str(round(totalAnswersY / (num_students * num_simulations) * 100))
avgDenials = str(totalAnswersN / num_simulations)
avgPercDenials = str(round(totalAnswersN / (num_students * num_simulations) * 100))

print "Average admittances: " + avgAdmittances + " (" + avgPercAdmittances + "%)"
print "Average denials: " + avgDenials + " (" + avgPercDenials + "%)"

