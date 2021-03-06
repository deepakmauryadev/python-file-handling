def readDataWithReadFun():
    # opening file with open(file_name, mode) function
    # where mode is "r", which means we can write only
    f = open("data.txt", "r")

    # reading data inside file
    data = f.read()

    # printing data
    print(data)

    # closing file
    f.close()


def readDataWithReadlineFun():
    # opening file with read only mode
    f = open("data.txt", "r")

    # writing with writeline(size: int) function
    data = f.readline(10)
    print(data)

    # closing file
    f.close()


def readDataWithReadlinesFun():
    # opening file with read only mode
    f = open("data.txt", "r")

    # writing with function writelines() --> list
    data = f.readlines()
    print(data)
    
    # closing file
    f.close()


def writeDataWithWriteFun():
    # opening file with write only mode
    f = open("data.txt", "w")

    # writing data with write(str) function
    f.write("This is second data")

    # closing file
    f.close()


def writeDataWithWritelinesFun():
    # opening file with write only mode
    f = open("data.txt", "w")
    
    # writing with writelines(list[str]) function
    f.writelines(["1st elem", "2nd elem"])

    # closing file
    f.close()

def writeAndReadData():
    # opening file with write and read mode
    f = open("data.txt", "w+")
    
    # writing with write(str) function
    f.write("This will be written")

    # seek(offset: int) used here to bring back cursor to start
    f.seek(0)

    # reading file
    data = f.read()
    print(data)

    # closing file
    f.close()

    
def readAndWriteData():
    # opening file with rrad and write mode
    f = open("data.txt", "r+")
    
    # writing with write(str) function
    f.write("This will be written")

    # seek(offset: int) used here to bring back cursor to start
    f.seek(0)

    # reading file
    data = f.read()
    print(data)

    # closing file
    f.close()

def appendDataFile():
    # opening file with append only mode
    f = open("data.txt", "a")

    f.write("This will be appended")