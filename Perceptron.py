 import GivingData
"""
  Perceptron Classifier

  Parameters
  num_weights: input of node
  learning_rate: is used to control how fast our perceptron will learn.


"""


class Perceptron:

    def __init__(self, learning_rate, num_weights):

        # self.speed = learning_rate
        # learning_rate = 0.1
        # learning_rate = 0.5


        self.weights = []
        for x in range(0, num_weights):
            self.weights.append()

        """
        output_error method for estimator error
        
        Parameters
        Y = the desired output
        a = activation of current node
        """
        def output_error(,):

            return ()

        """
        activate_function 

        Parameters
        w = the desired output
        x = activation of current node
        """
        #The activation is then transformed into an output value or
        #prediction using a transfer function, such as the step transfer function.
        def activation_function (self, inputs):
            sum = 0
            # multiply inputs by weights and sum them
            for x in range(0, len(self.weights)):
                sum += self.weights[x] * inputs[x]
            # return the 'activated' sum
            return sum

        """
        different between node j and i  method 

        Parameters
        w1 = the desired output
        w2 = activation of current node
        """



