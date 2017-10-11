# import perceptron

class Train_perceptron:
    def __init__(self, perceptron, image,rightanswer):
        self.perceptron = perceptron
        self.image = image
        self.speed = 0.005
        self.rightanswer = int(rightanswer)
        self.error = 0

        if self.rightanswer == self.perceptron.getEmotion():
            self.wantedanswer = 1
        else:
            self.wantedanswer = 0


    def calculateError(self):
        error = float(self.wantedanswer) - self.perceptron.getOutput()
        self.error = error
        #print("Error!!!", error)
        return error

    def calculateNewWeights(self):
        error = self.calculateError()
        weights = self.perceptron.getWeights()


        newWeights = []

        for i in range(len(weights)):
            delta_W = self.speed * error * ((float(self.image[i]))/32)
            #print(delta_W)
            newWeight = weights[i] + delta_W
            newWeights.append(newWeight)

        return newWeights



    def train(self):
        newWeights = self.calculateNewWeights()
        self.perceptron.updateWeights(newWeights)

    def getError(self):
        return self.error
