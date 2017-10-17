"""
  train_perceptron

  Class which represents a traning session with a perceptron

"""



class Train_perceptron:

    """
    Constructor train_perceptron
    Creates an instance of the train_perceptron class

    Parameters: perceptron the perceptron to train, image the image to train on, rightanswer the correct answer
    , output the output from the activation function
    """
    def __init__(self, perceptron, image,rightanswer,output):
        self.perceptron = perceptron
        self.image = image
        self.speed = 0.005
        self.rightanswer = int(rightanswer)
        self.error = 0
        self.output=output

        """Converting wanted answer to either 1(active) or 0(non-active)"""
        if self.rightanswer == self.perceptron.getEmotion():
            self.wantedanswer = 1
        else:
            self.wantedanswer = 0

    """
    Method calculateError
    Method to calculate the error betweent the acutal and wanted ansers
    
    Returns: The differential
    """
    def calculateError(self):
        error = float(self.wantedanswer) - self.output
        self.error = error
        return error

    """
    Method calculateNewWeights
    Calculates the new weights based on the error and learning rate
    Returns: The delta werights vector
    """
    def calculateNewWeights(self):
        error = self.calculateError()
        weights = self.perceptron.getWeights()


        delta_W_arr = []
        for i in range(len(weights)):
            delta_W = self.speed * error * ((float(self.image[i]))/32)
            delta_W_arr.append(delta_W)

        return delta_W_arr

    """
    Method train
    Trains the perceptron and updates the weights
    """
    def train(self):
        delta_W_arr = self.calculateNewWeights()
        self.perceptron.updateWeights(delta_W_arr)

    """Getters"""
    def getError(self):
        return self.error
