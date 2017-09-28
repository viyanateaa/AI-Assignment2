import csv


class GivingData:
    path = 'training-A.txt'
    data_file = open(path, 'r')
    data = data_file.read()

    def loadGivingData(self, file_name):

        #try:
         #   txt_file = open(file_name)
        #except IOError:
           # print "Problem with giving file" ,file_name



        with open(file_name) as txt_file:
            lines = csv.reader(file_name)
            dataset = list(lines)
            for x in range(len(dataset)-1):
                for y in range(4):
                    dataset[x][y]= float(dataset[x][y])

            #data = [][]
            data = [[0 for i in range(19)] for j in range(19)]

            # Creates a list containing 5 lists, each of 8 items, all set to 0
           # w, h = 8, 5;
            #Matrix = [[0 for x in range(w)] for y in range(h)]
           # lines = txt_file.read().split('\n')

            for line in txt_file:
                #if line != "#":
                    line = line.split()
                    
                    data.append(line)
                    print (line)

        
        







        # txt_file = open("training-A.txt","r")
                    # while

                    # txt_file.close()


       # with open("training-A.txt") as file:
        #    lines

         #   for lin

