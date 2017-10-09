import faces
import random
import math
import numpy
"""
  Perceptron Classifier

  Parameters
  num_weights: input of node
  learning_rate: is used to control how fast our perceptron will learn.


"""


class Perceptron:
    def __init__(self, weights, learning_rate, emotion):
        self.emotion = emotion
        self.speed = learning_rate
        self.weights = weights
        self.output = float()

    def activation_function(self, inputs):
        sum = float()
        list = []
        for j in range(len(self.weights)):
            a = float(self.weights[j])

            b = float(inputs[j])/float(32)

            sum+=a*b

            e = math.e

            result = 1 / (1 + e ** - sum)

            self.output = result

            return result

    def updateWeights(self, newWeights):
        self.weights = newWeights

    def getWeights(self):
        return self.weights

    def getOutput(self):
        return self.output

    def getEmotion(self):
        return self.emotion

