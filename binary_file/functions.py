import pickle

def readBinaryData():
    # opening with read only binary mode
    f = open("bindata.dat", "rb")

    # reading binary data with the help of pickle module
    bindata = pickle.load(f.read())
    print(bindata)

    # closing file
    f.close()


def writeBinaryData():
    # opening with write only binary mode
    f = open("bindata.dat", "wb")

    data = {
        "id": 0,
        "name": "unknown"
    }

    # writing binary data with pickle.dump(data: list | dict, fileObject) function
    pickle.dump(data, f)

    # closing file
    f.close()