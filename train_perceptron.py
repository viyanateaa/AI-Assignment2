class Train_perceptron:
    def __init__(self, perceptron, image,rightanswer,output):
        self.perceptron = perceptron
        self.image = image
        self.speed = 0.005
        self.rightanswer = int(rightanswer)
        self.error = 0
        self.output=output

        if self.rightanswer == self.perceptron.getEmotion():
            self.wantedanswer = 1
        else:
            self.wantedanswer = 0


    def calculateError(self):
        error = float(self.wantedanswer) - self.output
        self.error = error
        return error

    def calculateNewWeights(self):
        error = self.calculateError()
        weights = self.perceptron.getWeights()


        delta_W_arr = []
        for i in range(len(weights)):
            delta_W = self.speed * error * ((float(self.image[i]))/32)
            delta_W_arr.append(delta_W)

        return delta_W_arr



    def train(self):
        delta_W_arr = self.calculateNewWeights()
        self.perceptron.updateWeights(delta_W_arr)

    def getError(self):
        return self.error
