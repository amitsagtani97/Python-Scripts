from numpy import *
import operator


def classify(x,dataset,labels,k):
    datasetsize=dataset.shape[0]
    diffmat=tile(x,(datasetsize,1))-dataset
    sqdiffmat=diffmat**2
    sqdistances=sqdiffmat.sum(axis=1)
    distances=sqdistances**0.5
    sorteddistindices=distances.argsort()
    classcount={}
    for i in range(k):

        voteIlabel=labels[sorteddistindices[i]]
        classcount[voteIlabel]=classcount.get(voteIlabel,0) +1

    sortedclasscount=sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedclasscount[0][0]

def autonorm(dataset):
    minval=dataset.min(0)
    maxval=dataset.max(0)
    ranges=maxval-minval
    normdataset=zeros(shape(dataset))
    m=dataset.shape[0]
    normdataset=dataset-tile(minval,(m,1))
    normdataset=normdataset/tile(ranges,(m,1))
    return normdataset,ranges,minval


def file2matrix(filename):
    fr=open(filename)
    numberoflines=len(fr.readlines())
    returnmat=zeros((numberoflines,7))
    classLabelvec=[]
    fr=open(filename)
    index=0
    for line in fr.readlines():
        line=line.strip()
        listfromline=line.split(",")
        returnmat[index,:]=listfromline[1:8]
        classLabelvec.append((listfromline[0]))
        index+=1
    return returnmat,classLabelvec

def classperson():
    print("Abalone is a common name for any of a group of small to very large sea snails, marine gastropod molluscs in the family Haliotidae.")
    print("\n")
    print("From certain input about Abalone this algorithm will predict whether Abalone is \nM-> Male,\nF->Female or\nI->Infant ")
    print("\n")
    print("Accuracy of this algorithm is 65 to 70%")
    input1 =float(input("enter length of Abalone"))
    input2 = float(input("enter diameter"))
    input3 = float(input("enter height"))
    input4 = float(input("enter whole weight"))
    input5 = float(input("enter shucked weight"))
    input6 = float(input("enter viscera weight"))
    input7 = float(input("enter shell weight"))


    datamat, lab = file2matrix("KNN_support/abalone.data")
    normmat, ran, minval = autonorm(datamat)

    inarr=array([input1,input2,input3,input4,input5,input6,input7])
    classresult=classify((inarr-minval)/ran,normmat,lab,3)
    print("\n")
    print(classresult)


classperson()