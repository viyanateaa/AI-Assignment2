import csv


class GivingData:
    ##read file
    # path = 'training-A.txt'
    # data_file = open(path, 'r')
    # data = data_file.read()

    # def loadGivingData(self, file_name):

    try:
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

        print (pixel_data[:10])

        def split_data(a_list):
            half = int(len(a_list) / (3.0 / 2.0))
            return a_list[:half], a_list[half:]

        test_data = []
        train_data = []
        test_data, train_data = split_data(pixel_data)

        #print (len(test_data))
        #print test_data
        #print (len(train_data))
        #print (train_data[:10])

    except IOError:
        print "Problem with giving file", file_name
