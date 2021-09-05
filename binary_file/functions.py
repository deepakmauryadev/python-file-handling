import pickle

def readBinaryData():
    # opening with read only binary mode
    f = open("bindata.dat", "rb")

    # reading binary data with the help of pickle module
    try:
        bindata = pickle.load(f)
        print(bindata)
        
    except EOFError:
        pass

    # closing file
    f.close()


def writeBinaryData():
    # opening with write only binary mode
    f = open("bindata.dat", "wb")

    data = {
        "id": "0",
        "name": "writeBinaryData function"
    }

    # writing binary data with pickle.dump(data: list | dict, fileObject) function
    pickle.dump(data, f)

    # closing file
    f.close()


def writeAndReadBinaryData():
    # opening binary file with write and read mode
    f = open("bindata.dat", "wb+")

    data = {
        "id": "1",
        "name": "writeAndReadBinaryData function"
    }

    # write
    pickle.dump(data, f)

    f.seek(0)
    # read
    try:
        bindata = pickle.load(f)
        print(bindata)
        
    except EOFError:
        pass

    # closing file
    f.close()


def appendBinaryData():
    # opening file in read and write mode
    f = open("bindata.dat", "rb+")

    # function to read file
    def fetchBinaryData():
        try:
            f.seek(0)
            return pickle.load(f)
            
        except EOFError:
            pass

    bindata = dict(fetchBinaryData())

    data = {
        "nickname": "appendBinaryData"
    }

    bindata.update(data)

    f.seek(0)
    # writing file
    pickle.dump(bindata, f)

    print(fetchBinaryData())

    # closing file 
    f.close()