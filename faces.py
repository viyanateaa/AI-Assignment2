import random
import sys
import perceptron
import train_perceptron


def loadGivingData(file_name):
    images_temp = []
    pixel_data = []
    with open(file_name) as txt_file:
        for line in txt_file:
            cleanedLine = line.strip()

            if not cleanedLine.startswith('#'):
                if not cleanedLine.startswith('\n'):
                    if not cleanedLine.startswith('I'):
                        if line.rstrip():
                            splitLine = cleanedLine.split()
                            pixel_data.append(splitLine)

    list = []

    for i in range(len(pixel_data)):
        line = pixel_data[i]
        if i % 20 != 0 or i == 0:
            list.extend(line)
        else:
            images_temp.append(list)
            list = []
            line = pixel_data[i]
            list.extend(line)
    images_temp.append(list)
    return images_temp


def split_data(a_list, split):
    half = int(len(a_list) * split)
    return a_list[:half], a_list[half:]


def loadAnswerData(facit_name):
    facit_data = []
    with open(facit_name) as txt_file:
        for line in txt_file:
            cleanedline = line.strip()

            if not cleanedline.startswith('#'):
                if not cleanedline.startswith(' \n'):
                    if cleanedline.startswith('Image'):
                        if line.rstrip():
                            splitlines = cleanedline.split()
                            facit_data.append(splitlines[1])

    return facit_data


def createWeights():
    randomValues = []
    for j in range(0, 400):
        randomValue = random.uniform(0, 0.1)
        randomValues.append(randomValue)
    return randomValues


def whoWon(allperceptron):
    temp = float()
    winner = 0
    for i in range(len(allperceptron)):
        output = allperceptron[i].getOutput()
        if output > temp:
            temp = output
            winner = allperceptron[i].getEmotion()
    return winner


def compareResult(facitX, resultX):
    counter = 0
    for i in range(len(facitX)):
        a = int(facitX[i])
        b = resultX[i]
        if a is b:
            counter += 1
    return counter


def shuffle(list_1, list_2):
    c = list(zip(list_1, list_2))
    random.shuffle(c)
    a, b = zip(*c)
    return a, b




if __name__ == '__main__':
    """Reading the files"""
    traning_images = sys.argv[1]
    facit_image = sys.argv[2]
    final_test_file = sys.argv[3]
    final_test_facit= sys.argv[4]

    images = loadGivingData(traning_images)
    facit = loadAnswerData(facit_image)
    final_test_images = loadGivingData(final_test_file)
    final_test_facit=loadAnswerData(final_test_facit)

    test_data = []
    train_data = []

    test_facit = []
    train_facit = []

    final_test_data = []
    garbage = []

    images, facit = shuffle(images, facit)
    train_data, test_data = split_data(images,0.75)
    train_facit, test_facit = split_data(facit,0.75)

    final_test_data, garbage = split_data(final_test_images, 1.0)

    """Creating perceptrons"""
    weights_happy = createWeights()
    weights_sad = createWeights()
    weights_mischievous = createWeights()
    weights_angry = createWeights()

    happy = perceptron.Perceptron(weights_happy, 1)
    sad = perceptron.Perceptron(weights_sad, 2)
    mischievous = perceptron.Perceptron(weights_mischievous, 3)
    angry = perceptron.Perceptron(weights_angry, 4)

    allperceptron = [happy, sad, mischievous, angry]

    result = []

    percentage = 0
    errorSum = 0
    # 65%
   # while percentage < 0.8:
    numberOfRounds = 50
    for x in range(numberOfRounds):
        result = []

        #images, facit = shuffle(images, facit)
        #train_data, test_data = split_data(images)
        #train_facit, test_facit = split_data(facit)

        #print(len(train_data))
        #print(len(train_facit))


        for i in range(len(train_data)):
            errorSum = 0

            for j in range(len(allperceptron)):
                output=allperceptron[j].activation_function(train_data[i])
                #print(output)
                training_session = train_perceptron.Train_perceptron(allperceptron[j], train_data[i], train_facit[i],output)
                training_session.train()
                errorSum += abs(training_session.getError())

            winner = whoWon(allperceptron)
            result.append(winner)

        numberRights = compareResult(train_facit, result)


        percentage = (float(numberRights) / (len(train_facit)))

        print ("I got %.2f percent correct this training round" % (percentage * 100))



    """TEST"""

    test_result = []
    for w in range(len(test_data)):
        for q in range(len(allperceptron)):
            output = allperceptron[q].activation_function(test_data[w])
        winner = whoWon(allperceptron)
        test_result.append(winner)

    numberRights = compareResult(test_facit, test_result)

    percentage = (float(numberRights) / (len(test_facit)))

    print("I got %.2f percent correct this test round" % (percentage * 100))


    """FINAL TEST"""
    file = open("result.txt", "w+")
    final_test_result = []
    for m in range(len(final_test_data)):
        for n in range(len(allperceptron)):
            output = allperceptron[n].activation_function(final_test_data[m])
        winner = whoWon(allperceptron)
        final_test_result.append(winner)

    numberRights = compareResult(final_test_facit, final_test_result)

    percentage = (float(numberRights) / (len(final_test_facit)))

    print("I got %.2f percent correct this final test round" % (percentage * 100))



    #Write ansewer to file
    for p in range (len(test_result)):
        file.write("%d\r\n" % (test_result[p]))

    file.close()




