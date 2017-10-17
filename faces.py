import random
import sys
import perceptron
import train_perceptron

"""
  Faces
  Program to read pixels from text-files and learn to regognize facial expressions represented by the pixels
  4 feelings exist
      1. Happy
      2. Sad
      3. Mischievous
      4. Angry

"""

"""
Method loadGivingData
Method to read the data into a list where each picture is represented
with a line in a list. The image name is ignored and the index is the key.

Parameters: file_name the name of the file to read
Returns: List with the pixels from each image collected in one row
"""
def loadGivingData(file_name):
    #Reads the file as written ex 4000x20
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
    #Converts the file to desired format 200x400
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


"""
Method loadImagesName
Reades the names of the images into a list, required since the 
given test programs demands a certain format containing imagenames

Parameters: file_name the file to read from
Returns: list with images name  ex "Image201"
"""
def loadImagesName(file_name):
    images_name= []
    with open(file_name) as txt_file:
        for line in txt_file:
            cleanedLine = line.strip()

            if not cleanedLine.startswith('#'):
                if not cleanedLine.startswith('\n'):
                    if cleanedLine.startswith('I'):
                        images_name.append(cleanedLine)
    return images_name


"""
Method split_data
Splits the data into two halfes with given size

Parameters: a_list the list to split, split the size to split into
Returns: Two list splitted at the desired size
"""
def split_data(a_list, split):
    half = int(len(a_list) * split)
    return a_list[:half], a_list[half:]


"""
Method loadAnswerData
Reads the facit file

Parameters: facit_name, the name of the file contating the facit
Returns: List with facit data, one line for each image
"""
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


"""
Method createWeights
Creates the random weight used when initiating perceptrons

Returns: The random weights
"""
def createWeights():
    randomValues = []
    for j in range(0, 400):
        randomValue = random.uniform(0, 0.1)
        randomValues.append(randomValue)
    return randomValues


"""
Method whoWon
Method who decides which perceptron had the highest output

Parameters: allperceptron, vector with the 4 perceptrons
Returns: The emotion of the winning perceptron
"""
def whoWon(allperceptron):
    temp = float()
    winner = 0
    for i in range(len(allperceptron)):
        output = allperceptron[i].getOutput()
        if output > temp:
            temp = output
            winner = allperceptron[i].getEmotion()
    return winner


"""
Method compareResult
Compares the facit with the actual result from the perceptrons

Parameters: facitX the facit, resultX, the result
Returns: A counter with the number rights
"""
def compareResult(facitX, resultX):
    counter = 0
    for i in range(len(facitX)):
        a = int(facitX[i])
        b = resultX[i]
        if a is b:
            counter += 1
    return counter


"""
Method shuffle
Method to shuffle two lists in the same order

Parameters: list_1 the first list, list_2 the second list
Returns: The two lists shuffled in the same order
"""
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

    images = loadGivingData(traning_images)
    facit = loadAnswerData(facit_image)
    final_test_images = loadGivingData(final_test_file)
    images_names=loadImagesName(final_test_file)



    """Creating the lists"""
    test_data = []
    train_data = []

    test_facit = []
    train_facit = []

    final_test_data = []
    garbage = []

    images, facit = shuffle(images, facit)

    """Splitting the data"""
    train_data, test_data = split_data(images,0.75)
    train_facit, test_facit = split_data(facit,0.75)
    final_test_data, garbage = split_data(final_test_images, 1.0)


    """Creating weights"""
    weights_happy = createWeights()
    weights_sad = createWeights()
    weights_mischievous = createWeights()
    weights_angry = createWeights()

    """Creating perceptrons"""
    happy = perceptron.Perceptron(weights_happy, 1)
    sad = perceptron.Perceptron(weights_sad, 2)
    mischievous = perceptron.Perceptron(weights_mischievous, 3)
    angry = perceptron.Perceptron(weights_angry, 4)

    allperceptron = [happy, sad, mischievous, angry]

    """Initalizing variables"""
    result = []
    percentage = 0
    errorSum = 0
    numberOfRounds = 50

    """TRAINING WITH 75% OF DATA"""
    for x in range(numberOfRounds):
        result = []

        for i in range(len(train_data)):
            errorSum = 0

            for j in range(len(allperceptron)):
                output=allperceptron[j].activation_function(train_data[i])
                training_session = train_perceptron.Train_perceptron(allperceptron[j], train_data[i], train_facit[i],output)
                training_session.train()
                errorSum += abs(training_session.getError())

            winner = whoWon(allperceptron)
            result.append(winner)

        numberRights = compareResult(train_facit, result)

        percentage = (float(numberRights) / (len(train_facit)))

        print ("I got %.2f percent correct this training round" % (percentage * 100))



    """TESTING WITH REMAINING 25% OF DATA"""

    test_result = []
    for w in range(len(test_data)):
        for q in range(len(allperceptron)):
            output = allperceptron[q].activation_function(test_data[w])
        winner = whoWon(allperceptron)
        test_result.append(winner)

    numberRights = compareResult(test_facit, test_result)

    percentage = (float(numberRights) / (len(test_facit)))

    print("I got %.2f percent correct this test round" % (percentage * 100))


    """FINAL TEST WITH NEW DATA"""
    final_test_result = []
    for m in range(len(final_test_data)):
        for n in range(len(allperceptron)):
            output = allperceptron[n].activation_function(final_test_data[m])
        winner = whoWon(allperceptron)
        final_test_result.append(winner)



    """Writning answer to file"""
    file = open("result.txt", "w+")
    for p in range(len(final_test_result)):
        file.write("%s %d\n" % (images_names[p], final_test_result[p]))

    file.close()




