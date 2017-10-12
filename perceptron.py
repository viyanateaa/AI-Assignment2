import math

"""
  Perceptron

  Parameters
  weights: The current weights of the 


"""

class Perceptron:

    def __init__(self, weights, emotion):
        self.emotion = emotion
        self.weights = weights

        self.output = float()

    def activation_function(self, inputs):
        sum = float()
        for j in range(len(self.weights)):
            a = float(self.weights[j])
            b = float(inputs[j])/float(32)
            sum+=a*b
        e = math.e
        result = 1 / (1 + e ** (- sum))
        self.output = result
        return result

    def updateWeights(self, delta_W_arr):
        for i in range(len(self.weights)):
            self.weights[i] += delta_W_arr[i]

    def getWeights(self):
        return self.weights

    def getOutput(self):
        return self.output

    def getEmotion(self):
        return self.emotion





