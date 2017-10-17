import math

"""
  Perceptron

  Class which represents a single perceptron
  
  Parameters: weights the init weights, emotion the emotion for this perceptron


"""

class Perceptron:

    """
    Constructor Perceptron
    Creates an instance of the perceptron class

    Parameter: weights, the weights for each pixel
    emotion, the emotion for this perceptron

    """
    def __init__(self, weights, emotion):
        self.emotion = emotion
        self.weights = weights

        self.output = float()

    """
    Method activiation_function
    Method to represent the activation function which gives an output between 0 and 1
    of how active a perceptron has been
    
    Parameters: inputs: The pixels
    Returns: The activation level of the perceptron
    """
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

    """
    Method updateWeights
    Method to adjust the size of the weights
    
    Parameters: delta_W_arr the array with the adjustments to be made
    """
    def updateWeights(self, delta_W_arr):
        for i in range(len(self.weights)):
            self.weights[i] += delta_W_arr[i]


    """Getters"""
    def getWeights(self):
        return self.weights

    def getOutput(self):
        return self.output

    def getEmotion(self):
        return self.emotion





