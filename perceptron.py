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
        # learning_rate = 0.1
        # learning_rate = 0.5

    def activation_function(self, inputs):
        sum = float()
        list = []
        for j in range(len(self.weights)):
            a = float(self.weights[j])
            #print(type(inputs[j]))
            b = float(inputs[j])/float(32)
            #print(type(b))
            #print(type(a))
            #print('Hej')
            #print (a)
            #print (b)
            sum+=a*b
            #list = map (lambda y: y* self.weights[x], inputs[x])
            #sum += numpy.multiply(self.weights[x] * inputs[x])
            #sum += list
            e = math.e
            result = 1 / (1 + e ** - sum)

            self.output=result

            return result

    def updateWeights(self, newWeights):
        self.weights = newWeights

    def getWeights(self):
        return self.weights

    def getOutput(self):
        return self.output

    def getEmotion(self):
        return self.emotion


