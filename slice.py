from functools import wraps
from threading import Timer
import time
import random
from pyswip import Prolog
from pyswip import *
from pyswip import Functor,Variable,Query
from pip._vendor.distlib.compat import raw_input

file = "dataDepFact.pl"
criterion = "(fD__workspace_antlr_C_SCircle_c___mprintSCircle_r22c7,{type_int(iv)})"

period1StartTime = time.time()#get input time
sliceLab = criterion.split(",",1)[0][1:]
sliceVar = criterion.split(",",1)[1][1:-2]
sliceVar = str(sliceVar).replace("(", "_").replace(")","")
# print(sliceVar)
prolog = Prolog()
prolog.consult(file)

defF = Functor("defF",2)
refF = Functor("refF",2)
flow = Functor("flow",2)
control = Functor("control",2)
dataDepF = Functor("dataDepF",3)
find_instr = Functor("find_instr",3)#add new fact,rule to the .pl file
prolog.assertz("find_instr(X,Y,Z):-instr(X,Y,Z)")#the definition of fact or gule

depth = {}  
depth[sliceLab] = 0
timeStack = {"period1StartTime":period1StartTime}

X = Variable()
Y = Variable()
V = Variable()

weightQ = [sliceLab]
weightQVar = {sliceLab:sliceVar}
M = {sliceLab:2**depth[sliceLab]}
depPre = []
dDepPre = []
wFlag = False
R = []
instrM = {}
instrR = []
#count = 0
sliceflow = Functor("sliceflow",2)

while weightQ:
    n = weightQ.pop()
    nVar = weightQVar.pop(n)
    wFlag = False
    if n in R:
        continue
    else:
        R.append(n)
    depPreQuery = Query(control(X,n))
    while depPreQuery.nextSolution():
        depPre.append(X.value.__str__())
    depPreQuery.closeQuery()
    while nVar:
        print(nVar)
        curVar = nVar.split(",",1)[0]
        depPreQuery = Query(dataDepF(X,n,curVar))
        while depPreQuery.nextSolution():
            depPre.append(X.value.__str__())
            dDepPre.append(X.value.__str__())
#             if X.value.__str__() not in dDepPre.keys():
#                 dDepPre[X.value.__str__()] = curVar
#             else:
#                 dDepPre[X.value.__str__()] = dDepPre[X.value.__str__()]+","+curVar
        depPreQuery.closeQuery()
        if nVar.find(",") == -1:
            nVar = ""
        else:
            nVar = nVar.split(",",1)[1]
            
    while depPre:
        m = depPre.pop()
        depth[m] = depth[n]-1
        if m in M.keys():
            wFlag = True
            continue
        weight = M[n]- (2**depth[m]/3)
        refVarQ = Query(refF(m,V))
        refVar = str()
        while refVarQ.nextSolution():
            refVar = refVar+","+V.value.__str__()
        refVarQ.closeQuery()
        if m in dDepPre:
            weight = weight- (2**depth[m]/3)
#             weightQVar[m] = dDepPre[m]+refVar
        else:
            weight = weight- (2**depth[m]/3*2)
#             weightQVar[m] = ""
        weightQVar[m] = refVar[1:]
        weightQ.append(m)
        M[m] = weight
    if wFlag:
        continue     

print(M)
print(R)

def instrTrans(instr):
    if instr.startswith("ite("):
        instr = instr[:instr.find("), f")+1]+")"
#         print(instr)
        return instr
    elif instr.startswith("switch("):
        instr = instr[:instr.find(", ,(")]+")"
#         print(instr)
        return instr
    elif instr.startswith("for("):
        instr = instr[:instr.find(")), f")+2]+")"
#         print(instr)
        return instr
    elif instr.startswith("while("):
        instr = instr[:instr.find(")), f")+2]+")"
#         print(instr)
        return instr
    else:
#         print(instr)
        return instr
    
def lab2Instr(myLab):
    if type(myLab).__name__ == 'dict':
        ks = myLab.keys()
        for key in ks:
            q = Query(find_instr(key,X,Y))
            if q.nextSolution():                
                instrM[instrTrans(X.value.__str__())] = M[key]
            q.closeQuery()
#         print("instrM:"+str(instrM))
#         return instrM
    elif type(myLab).__name__ == 'list':
        i = 0
        while i < len(myLab):
            
            tempLab = myLab[i]
            q = Query(find_instr(tempLab,X,Y))
            if q.nextSolution():                
                instrR.append(instrTrans(X.value.__str__()))
            q.closeQuery()
            i = i+1
#         print("instrR:"+str(instrR))  
#         return instrR  

lab2Instr(M)    
lab2Instr(R)

period2EndTime = time.time()
# timeStack.append(period2EndTime)
timeStack["period2EndTime"] = period2EndTime
# print("!"+str(timeStack))
# print("slice time:"+str((timeStack["period1EndTime"]-timeStack["period1StartTime"])+(timeStack["period2EndTime"]-timeStack["period2StartTime"])))
      
def rouletteWheelSelection(LabWeightStack):
    rwWeight = list(LabWeightStack.values())
    rwLabel = list(LabWeightStack.keys())
    rwWeight = list(LabWeightStack.values())
    finalLabel = [rwLabel[0]]
    tempWeight = []
    del rwLabel[0]
    del rwWeight[0]
    # print(sum(rwWeight))
    testCount = 1
    while rwLabel:
        sumW = sum(rwWeight)
        tempWeight.append(rwWeight[0])
        i = 1
        while i< len(rwWeight):
            tempWeight.append(tempWeight[-1]+rwWeight[i])
            i = i+1
        rndNum = random.uniform(0,sumW)
        i = 0
        while i<= len(tempWeight):
            if rndNum<tempWeight[i]:
                break
            i = i+1
        finalLabel.append(rwLabel[i-1])
        del rwWeight[i-1]
        del rwLabel[i-1]
    #     print(rwLabel)
        tempWeight.clear()
        testCount = testCount+1
  
#     print(finalLabel)
    return finalLabel

eaChoose = raw_input("start roulette Wheel Selection(Y or N):")

while eaChoose == "Y":
    cc = rouletteWheelSelection(M)  
    print(cc)
    cc = rouletteWheelSelection(instrM)  
    print("rouletteWheelSelection"+str(cc))
    eaChoose = raw_input("start roulette Wheel Selection again (Y or N):")



def computeSliceFlow(sliceStack,preLab,curLabel):
    sliceflowFact = str()
    if preLab in sliceStack:
#         print(sliceStack)
#         q = Query(find_instr(preLab,X,Y))
#         if q.nextSolution():                
#             instr = X.value.__str__()
#         q.closeQuery()
        sliceflowFact = "sliceflow("+preLab+","+curLabel+");"
#         print("1:"+curLabel+" "+sliceflowFact)
        return sliceflowFact
    else:
        preLabelQ = Query(flow(X,preLab))
        ppreLabelS = []
        while preLabelQ.nextSolution():
            ppreLabelS.append(X.value.__str__())
        preLabelQ.closeQuery()
        while ppreLabelS:
            ppreLabel = ppreLabelS.pop()
            sliceflowFact = sliceflowFact + computeSliceFlow(sliceStack, ppreLabel,curLabel)
#             print("2:"+curLabel+" "+sliceflowFact)
        return sliceflowFact


i = 0
while i<len(R):
    sliceLab = R[i]  
    i = i+1
#     print("^"+sliceLab)     
    preSliceLabQ = Query(flow(X,sliceLab))
    preSliceLabS = []
    while preSliceLabQ.nextSolution():
        preSliceLabS.append(X.value.__str__())   
    preSliceLabQ.closeQuery() 
    sfFact = str()
    while preSliceLabS:
        preSliceLab = preSliceLabS.pop()
#         print("^^"+preSliceLab)
        sfFact = sfFact+computeSliceFlow(R, preSliceLab,sliceLab)

    while sfFact.find(";") != -1:
        prolog.assertz(sfFact.split(";",1)[0])
        if sfFact.find(";s") != -1:
            sfFact = sfFact.split(";",1)[1]
        else:
            sfFact = ""
            
print("%sliceflowFact")
sliceflow = Query(sliceflow(X,Y))
while sliceflow.nextSolution():
    print("sliceflow("+X.value.__str__()+","+Y.value.__str__()+").")
sliceflow.closeQuery()#remember to close the query

