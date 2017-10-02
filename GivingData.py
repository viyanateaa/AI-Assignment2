import csv


class GivingData:
    ##read file
    # path = 'training-A.txt'
    # data_file = open(path, 'r')
    # data = data_file.read()

    # def loadGivingData(self, file_name):


    #def f(x):
     #   return x != '#'

    try:
        pixel_data = []
        # not sure which file to start with ?!
        with open('training-A.txt') as txt_file:
            for line in txt_file:
                # strip() ignore lines with only whitespace
                # if line == '#':
                # pass
                # no = line.replace('\n', '')
                cleanedLine = line.strip()

                if not cleanedLine.startswith('#'):
                    if not cleanedLine.startswith(' \n'):
                        if not cleanedLine.startswith('I'):
                            line.rstrip()
                            splitLine = cleanedLine.split()
                    #
                    # newLine = filter(f, splitLine)
                    # if cleanedLine:  # is not empty
                    # print(cleanedLine)

                    # line = line.split()
                    # if line != '#':
                    # line = line.strip()
                    # else:
                    # line.strip():
                    # splitlines()  eliminate only the NL \n and RF \r symbols
                    # line = line.splitlines()
                    # clean data from #,Imgaes,empty line
                            pixel_data.append(splitLine)

        print (pixel_data[:20])
    except IOError:
        print "Problem with giving file", file_name



        # with open(file_name) as txt_file:
        # lines = csv.reader(file_name)
        # dataset = list(lines)
        # for x in range(len(dataset)-1):
        #   for y in range(4):
        #        dataset[x][y]= float(dataset[x][y])



        # Creates a list containing 5 lists, each of 8 items, all set to 0
        # w, h = 8, 5;
        # Matrix = [[0 for x in range(w)] for y in range(h)]
        # lines = txt_file.read().split('\n')

        # for line in txt_file:
        # if line != "#":
        #        line = line.split()

        #       data.append(line)
        #        print (line)










        # txt_file = open("training-A.txt","r")
        # while

        # txt_file.close()


        # with open("training-A.txt") as file:
        #    lines

        #   for lin
