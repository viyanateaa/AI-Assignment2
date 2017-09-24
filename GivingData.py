
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
            data = []
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

