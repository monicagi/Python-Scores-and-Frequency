"""Name: Monica Guevara
   Class: CSC 4800
   Assignment: Lab #1
   Date: 1/11/17
   This program reads the scores and frequencies from a file and then displays the information in charts """

def get_file():
    """The get_file function asks the user to enter a file name for reading and checks if it exists
       Then it calls the read_file function passing the file as an argument"""
    print("Welcome to the Quiz Score Frequency Analyzer, written by Monica Guevara")
    file_name = input("Enter input data filename: ")

    #Checks to see if the file exists
    try:
        file = open(file_name, 'r')
    except IOError:
        print("Unable to open file")
    else:
        print("Reading file '%s' input:" %(file_name))

        read_file(file)

def read_file(x):
    """The read_file function accepts the file as a parameter then reads the scores and frequencies from the file and
        stores them in the a1 and a2 list. Then it calls the display1 function passing the lists as arguments"""
    a1 = []
    a2 = []

    #Reads from the file and stores the scores in a1 and the frequencies in a2
    for line in x:
        data = line.split()
        a1.append(int(data[0]))
        a2.append(int(data[1]))

    #Closes the file
    x. close()

    display1(a1, a2)

def display1(x, y):
    """The display1 function accepts two lists as parameters it displays the scores and frequencies and then calls
        the nwlist function passing the list for the score and frequencies as arguments"""
    i = 0
    #Displays both lists
    while i < len(x):
        print(x[i], y[i])
        i = i + 1

    nwlist(x, y)

def nwlist(x, y):
    """The nwlist function accepts two lists as parameters then it removes any duplicates in the score list
        making sure to update these changes in the frequency list. Then it calls the display2 function passing the
        new lists as arguments"""
    i = 0
    j = 1
    #Removes any duplicates in the score list while adding the frequencies
    while i < len(x):
        while j < len(x):
            if(x[i] == x[j]):
                x.remove(x[i])
                y[j] = y[i] + y[j]
                y.remove(y[i])
            j = j+1
        i = i+1
        j = i +1

    display2(x, y)

def display2(x, y):
    """ The display2 function accepts two lists as parameters and displays the largest and smallest score as
        well as the largest frequency then it calls the display3 function passing the lists as arguments"""
    print("\nThe smallest score value is %i" % (min(x)))
    print("The largest score value is %i" % (max(x)))
    print("The largest frequency count is %i\n" % (max(y)))

    display3(x, y)

def display3(x, y):
    """The display3 function accepts two lists as parameters and then displays the information in a bar chart
        then it calls the display4 function passing the lists as arguments"""
    print("---Input Data---")
    print("Score: Frequency Bar Chart\n")

    i = min(x)
    #Displays the Bar Chart
    while i <= max(x):
        if (i in x):
            j = x.index(i)
            str = '*' * y[j]
            print("\t%i:\t\t%i\t%s" % (i, y[j], str))
            j = j + 1

        else:
            print("\t%i:\t\t%i" % (i, 0))
        i = i + 1

    display4(x, y)

def display4(x, y):
    """The display4 function accepts the lists as parameters and then displays the information from the lists in a
        vertical bar chart"""
    print("\nFrequency: Score Bar Chart")

    i = max(y)
    j = min(x)

    #Displays the frequencies and the *
    while i >= 1:
        print("\n\t^\t%2i:\t" %(i), end='  ')
        while j <= max(x):
            if(j in x):
                k = x.index(j)
                m = y[k]
                if(m >= i):
                    print("*", end='  ')
                else:
                    print(" ", end='  ')
            else:
                print(" ", end='  ')
            j = j+1
        j = min(x)
        i = i-1
    #Displays the pattern '--^'
    print("\n---------:\t", end='')
    j = min(x)
    while j <= max(x):
        print("--^", end='')
        j = j+1
    #Displays the scores
    print("\n\tScore:\t", end=' ')
    j = min(x)
    while j <= max(x):
        print("%i " %(j), end='')
        j = j + 1

if __name__ == '__main__':
    #Calls the get_file function
    get_file()







