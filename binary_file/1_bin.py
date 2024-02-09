import pickle


with open('binary_file/info.dat', "wb+") as fp:
    mesg = "Hello I am learning binary files"
    mesg2 = 21
    pickle.dump(mesg, fp)
    pickle.dump(mesg2, fp)
    fp.seek(0)
    info1 = pickle.load(fp)
    info2 = pickle.load(fp)
print(type(info2))
print(info2)
print("Success")


