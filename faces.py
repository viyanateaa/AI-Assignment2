import sys


def loadGivingData(file_name):
    images = []
    pixel_data = []
    with open('training-A.txt') as txt_file:
        for line in txt_file:
            cleanedLine = line.strip()

            if not cleanedLine.startswith('#'):
                if not cleanedLine.startswith(' \n'):
                    if not cleanedLine.startswith('I'):
                        if line.rstrip():
                            splitLine = cleanedLine.split()
                            pixel_data.append(splitLine)
                            # start = 0
                            # end = 20
                            # for i in range(start, end):
                            #   images.append(pixel_data[i])
                            #  start += 20
                            # end += 0
                            # if end > len(pixel_data):
                            #   break

    list = []
    for i in range(len(pixel_data)):
        line = pixel_data[i]
        if i % 20 != 0 or i == 0:
            list.extend(line)


        else:
            # print (len(list), "i= ", i)
            images.append(list)
            while len(list) > 0:
                list.pop()
            line = pixel_data[i]
            list.extend(line)

    return images


def split_data(a_list):
    half = int(len(a_list) * 0.75)
    return a_list[:half], a_list[half:]


def loadAnswerData(facit_name):
    facit_data = []
    with open(facit_name) as txt_file:
        for line in txt_file:
            cleanedline = line.strip()

            if not cleanedline.startswith('#'):
                if not cleanedline.startswith(' \n'):
                    if cleanedline.startswith('I'):
                        if line.rstrip():
                            splitlines = cleanedline.split()
                            facit_data.append(splitlines[1])

       # print (facit_data[:10])
    return facit_data

if __name__ == '__main__':

    traning_images = sys.argv[1]
    images = loadGivingData(traning_images)
    test_data = []
    train_data = []
    test_data, train_data = split_data(images)
    print (len(test_data))
    print (len(train_data))
    facit_data = loadAnswerData('facit-B.txt')
    test_facit = []
    train_facit = []
    test_facit, train_facit = split_data(facit_data)
    print (len(test_facit))
    print (len(train_facit))
    # traning_images = sys.argv[1]
