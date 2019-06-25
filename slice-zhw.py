'''
-*- coding: utf-8 -*-

@author: user
'''
import operator as op

from pyswip import Prolog
from pyswip import *
from pyswip import Functor,Variable,Query

from functools import wraps
from threading import Timer
#from wrapt_timeout_decorator import *

import time
import random
from datetime import datetime
from pip._vendor.distlib.compat import raw_input


prolog = Prolog()

#file = raw_input("file name:")
# flag = True
# while flag:
#     criterion = raw_input("slice criterion in form (statelab,{variable1,variable2}): ")
#     if criterion.startswith("(") and criterion.endswith("})") and criterion.find(",{") != -1:
#         flag = False
#     else:
#         print("Invalid input! Please try again!")
file = "sCircle.pl"
criterion = "(fD__workspace_antlr_C_SCircle_c___mprintSCircle_r22c7,{type_int(iv)})"

# file = "problem01_label00_true_unreach_call_false_termination.pl"
# criterion = "(fD__workspace_antlr_fileC_problem01_label00_true_unreach_call_false_termination_c___mcalculate_output_r381c6,{})"

period1StartTime = time.time()#get input time
sliceLab = criterion.split(",",1)[0][1:]
sliceVar = criterion.split(",",1)[1][1:-2]
sliceVar = str(sliceVar).replace("(", "_").replace(")","")
# print(sliceVar)
prolog.consult(file)

defF = Functor("defF",2)
refF = Functor("refF",2)
flow = Functor("flow",2)
control = Functor("control",2)
dataDepF = Functor("dataDepF",3)

varStack = []
loopStack = {}
iteStack = {}
switchStack = {}
callMStack = {} #the location where callMethod ,its next lab 
jumpStack = {} #jumpStack[lab] = jumpToLab
controlStack = {}
callCount={}
# timeStack = [period1StartTime]

timeStack = {"period1StartTime":period1StartTime}

raiseErrorTime = 0
depth = 0

def dealWithAssignInstr(lab,instr,toLab):    
    assDef = instr.split(",",1)
    #deal with var= 
    var = assDef[0][7:]
    defFact = 'defF(' + lab + ',' + str(var).replace("(", "_").replace(")","") + ')'
#     varT = str(var).replace("(", "_").replace(")","")
#     if varT not in varStack:
#         varStack.append(varT)
    fact = defFact
    #deal with =exp
    exp = assDef[1]
    rightValue = exp[1:-1]
#     rightValue = instr[instr.find(",")+1:-1]
    if rightValue.find("call_m") != -1:
        call_beg = rightValue.find("call_m")
        callIns = rightValue[call_beg:]
        rVFact = str()

        if lab in switchStack.keys():
            if toLab != switchStack[lab].split(";")[0] and toLab != switchStack[lab].split(";")[-1]:
                switchStack[toLab] = switchStack[lab]
            else:
                toLab = switchStack[lab].split(";")[0]
            rVFact = dealWithCallMInstr(lab, callIns,toLab)
        elif lab in iteStack.keys():
            if toLab != iteStack[lab].split(";")[0] and toLab != iteStack[lab].split(";")[-1]:
                iteStack[toLab] = iteStack[lab]
            else:
                toLab = iteStack[lab].split(";")[0]
            rVFact = dealWithCallMInstr(lab, callIns,toLab)    
        elif lab in loopStack.keys():
            if toLab in loopStack.keys():
                toLab = loopStack[lab]
            elif bt(loopStack[lab],toLab):
                loopStack[toLab] = loopStack[lab]
            rVFact = dealWithCallMInstr(lab, callIns,toLab)                          
        if rVFact.find(";")!=-1:                
            callMEntryLab = rVFact[:rVFact.find(";")]
            fact = callMEntryLab +";"+fact
            if rVFact.find(";defF("):
                defParaFact =  rVFact[rVFact.find(";"):rVFact.find(";refF")]
                fact = fact+defParaFact
                
    while rightValue.find("type_") != -1:
        beg = rightValue.find("type_")
        rightValue = rightValue[beg:]
        if rightValue.find("pointer") == -1:
            end = rightValue.find(")")+1
        else:
            end = rightValue.find("))")+2
        temp = rightValue[:end]
        fact = fact + ";refF(" + lab+"," + str(temp).replace("(", "_").replace(")","") + ")"
        rightValue = rightValue[end+1:]
    return fact
 
def dealWithForInstr(lab,instr,jumpLab):
    forLab = lab
    tempInstr = instr
    forNextLab = tempInstr[tempInstr.rfind(", ")+2:-1]
    fact = forNextLab
    loopStack[forLab] = jumpLab
    controlStack[forNextLab] = forLab
    controlStack[forLab] = jumpLab
    
    declaration = tempInstr.split(", ;")[0][6:]
    if declaration.startswith("assign("):
        declarationF = dealWithAssignInstr(lab,declaration,jumpLab)
        fact = fact + ";" + declarationF
    end = tempInstr.split(", ;")[1].find(")), f")
    conAndExp = tempInstr.split(", ;")[1][1:end]
    conEnd = conAndExp.find(", assign")
    con = conAndExp[:conEnd]
    while con.find("type_") != -1:
        beg = con.find("type_")
        if con.find("pointer") == -1:
            end = con.find(")")+1
        else:
            end = con.find("))")+2
        temp = con[beg:end]
        fact = fact + ';refF(' + lab+',' + str(temp).replace("(", "_").replace(")","") + ')'
        con = con[end+1:]
    exp = conAndExp[conEnd+2:]
    expfact = dealWithAssignInstr(lab, exp,jumpLab)
    fact = fact + ";" + expfact
    controlfact = "control("+forLab+","+forNextLab+")"
    #flowfact = "flow("+forLab+","+forNextLab+")"
    flowfact = "flow("+forLab+","+forNextLab+")"
    fact = fact+";"+controlfact+";"+flowfact    
    return fact

def dealWithWhileInstr(lab,instr,jumpLab):
    whileLab = lab
    tempInstr = instr
    whileNextLab = tempInstr[tempInstr.rfind(", ")+2:-1]
    fact = whileNextLab
    loopStack[whileLab] = jumpLab
    controlStack[whileNextLab] = whileLab
    controlStack[whileLab] = jumpLab
    controlfact = "control("+whileLab+","+whileNextLab+")"
    flowfact = "flow("+whileLab+","+whileNextLab+")"
    
    conEnd = tempInstr.find(")), f")
    con = tempInstr[6:conEnd+2]
    while con.find("type_") != -1:
        beg = con.find("type_")
        if con.find("pointer") == -1:
            end = con.find(")")+1
        else:
            end = con.find("))")+2
        temp = con[beg:end]
        fact = fact + ';refF(' + lab+',' + str(temp).replace("(", "_").replace(")","") + ')'
        con = con[end+1:]
    fact = fact+";"+controlfact+";"+flowfact  
    return fact

def dealWithIteInstr(lab,instr,jumpLab):
    ifLab = lab
    tempInstr = instr
    beg = tempInstr.find(", f")
    rfind = tempInstr.rfind(", f")
    con = tempInstr[:beg]
    thenLab = tempInstr[beg+2:rfind]
    elseLab = tempInstr[rfind+2:-1]
    fact = thenLab
    iteStack[ifLab] = thenLab+";"+elseLab+";"+jumpLab
    iteStack[thenLab] = elseLab+";"+jumpLab
    iteStack[elseLab] = jumpLab
    #iteStack[jumpLab] = jumpLab
    while con.find("type_") != -1:
        beg = con.find("type_")
        if con.find("pointer") == -1:
            end = con.find(")")+1
        else:
            end = con.find("))")+2
        temp = con[beg:end]
        fact = fact + ";refF(" + lab+"," + str(temp).replace("(", "_").replace(")","") + ")"
        con = con[end+1:]       
    controlStack[thenLab] = ifLab
    controlStack[elseLab] = ifLab
    controlStack[ifLab] = jumpLab #control end at jumoLab
    
    controlfact = "control("+ifLab +","+thenLab+")" 
    #flowfact = "flow("+ifLab +","+thenLab+");flow("+ifLab +","+elseLab+")"
    flowfact = "flow("+ifLab +","+thenLab+");flow("+ifLab +","+elseLab+")"
    if elseLab!=jumpLab:
        controlfact = controlfact +";control("+ifLab +","+elseLab+")"
    
    fact = fact+";"+controlfact+";"+flowfact
    return fact

def dealWithSwitchInstr(lab, instr, jumpLab):
    switchLab = lab
    tempInstr = instr
    beg = tempInstr.find("), ,(")
    caseInstr = tempInstr[beg+4:]
    end = caseInstr.find(")")
    firstCaseLab = caseInstr[caseInstr.find(", f")+2:end]
    fact = firstCaseLab
    caseInstr = caseInstr[end+4:]
#     caseCount = caseInstr.find(", f")+1
#     caseRP = 1/caseCount
    
    exp = tempInstr[:tempInstr.find(", ,(")]
    while exp.find("type_") != -1:
        beg = exp.find("type_")
        if exp.find("pointer") == -1:
            end = exp.find(")")+1
        else:
            end = exp.find("))")+2
        temp = exp[beg:end]
        fact = fact + ";refF(" + switchLab+"," + str(temp).replace("(", "_").replace(")","") + ")"
        exp = exp[end+1:]
    controlfact = "control("+switchLab+","+firstCaseLab+")"
    #flowfact = ("+switchLab+","+firstCaseLab+")"
    flowfact = "flow("+switchLab+","+firstCaseLab+")"
    elseCase = str()
    while caseInstr.find(", f") != -1:
        beg = caseInstr.rfind(", f")
        end = caseInstr.rfind(")")
        tempCase = caseInstr[beg+2:end]
        controlStack[tempCase] = lab
        controlfact = controlfact+";control("+lab+","+tempCase+")"
        flowfact = flowfact+";flow("+lab+","+tempCase+")"
        switchStack[tempCase] = elseCase+jumpLab
        elseCase = tempCase+";"+elseCase        
        caseInstr = caseInstr[:beg]
    switchStack[firstCaseLab] = elseCase+jumpLab
    switchStack[switchLab] = firstCaseLab+";"+elseCase+jumpLab
    #switchStack[jumpLab] = jumpLab+";"+elseCase[:-1]
    controlStack[lab] = jumpLab
    
    fact = fact+";"+controlfact+";"+flowfact

    return fact

def dealWithCallMInstr(lab,instr,toLab):
    tempInstr = instr[5:]
    methodNameEnd = tempInstr.find("(")
    methodName = tempInstr[:methodNameEnd]
    filePathEnd = lab.find("_c___m")
    filePath = lab[:filePathEnd+3]
    
    methodStr = "method("+ filePath+",B,C,D,E)"
    entryP = str()
    paraList = str()
    flowfact = str()
    fact = str()
    for solution in prolog.query(methodStr):
        queryMethod = solution["C"] 
        queryMethodBeg = queryMethod.find("(m")
        queryMethod = queryMethod[queryMethodBeg+1:-1]   
        if queryMethod == methodName:
            entryP = solution["E"]
            paraList = solution["D"] 
            break
    if entryP != "":#self-definition method
        entryLabStr = "entry_point("+ entryP+",ELab)"
        for solution in prolog.query(entryLabStr):  
            entryLab = solution["ELab"]
        fact = entryLab
        flowfact = ";flow("+lab+","+entryLab+")"
        fact = fact+flowfact
        if toLab.find(";"):
            callMStack[entryLab] = toLab.split(";")[0]
        else:
            callMStack[entryLab] = toLab
            
        if lab in callMStack.keys():
             callMStack[lab] = toLab+";"+callMStack[lab]
        else:
            callMStack[lab] = toLab
        while paraList.find("type_")!=-1:
            paraList = paraList[paraList.find("type_"):]
            fact = fact+";defF("+lab+","+str(paraList[:paraList.find(")")+1]).replace("(", "_").replace(")","")+")"
#             varT = str(paraList[:paraList.find(")")+1]).replace("(", "_").replace(")","")
#             if varT not in varStack:
#                 varStack.append(varT)
            paraList = paraList[paraList.find(")"):]
                
    if tempInstr.find("type_") == -1 and fact != "":
        fact = fact + ";"
    while tempInstr.find("type_") != -1:
        if tempInstr.find("assign(type_") == -1:  
            beg = tempInstr.find("type_")
            tempInstr = tempInstr[beg:]      
            if tempInstr.find("pointer") == -1:
                end = tempInstr.find(")")+1
            else:
                end = tempInstr.find("))")+2
            temp = tempInstr[:end]
            if fact != "":
                fact = fact + ";refF(" + lab+"," + str(temp).replace("(", "_").replace(")","") + ")"
            else:
                fact = fact + "refF(" + lab+"," + str(temp).replace("(", "_").replace(")","") + ")"
            tempInstr = tempInstr[end+1:]
        else:
            beg = tempInstr.find("assign(type_")+7
            tempInstr = tempInstr[beg:]      
            if tempInstr.find("pointer") == -1:
                end = tempInstr.find(")")+1
            else:
                end = tempInstr.find("))")+2
            temp = tempInstr[:end]
            fact = fact + ";defF(" + lab+"," + str(temp).replace("(", "_").replace(")","") + ")"
#             varT = str(temp).replace("(", "_").replace(")","")
#             if varT not in varStack:
#                 varStack.append(varT)
            tempInstr = tempInstr[end+1:]   
            
    if fact.startswith("; "):#may call_mprintf()
        fact = fact[2:]  
    #fact = fact+flowfact
    return fact
        
def computeControl(lab1,lab2):
    controlQ = Query(control(X,lab1))
    controlF = '_' 
    while controlQ.nextSolution():
        controlLab = X.value.__str__()
        endControlLab = controlStack[controlLab]
        if bt(endControlLab,lab2):
            controlF = "control("+controlLab+","+lab2+")"
    controlQ.closeQuery()
    return controlF
      

def bt(lab1,lab2):#lab1 is bigger than lab2
#     if lab1 != "ret" and lab1 != "end":
    if not lab1.endswith("ret") and not lab1.endswith("end") and not lab2.endswith("ret") and not lab2.endswith("end"):
        r1 = int(lab1[lab1.rfind("_r")+2:lab1.rfind("c")])
        c1 = int(lab1[lab1.rfind("c")+1:])
        
        r2 = int(lab2[lab2.rfind("_r")+2:lab2.rfind("c")])
        c2 = int(lab2[lab2.rfind("c")+1:])
        if r1>r2:
            return True
        elif r1 == r2 and c1>c2:
            return True
        else:
            return False
    elif lab1.endswith("ret") or lab1.endswith("end"):
        method1 = lab1[lab1.rfind("_c___m")+5:lab1.rfind("_end")]
        method2 = lab2[lab2.rfind("_c___m")+5:lab2.rfind("_end")]
        if method1 != method2:
            return False
#         else:
#             return True
    else:    
        return True                 

def notExsitFact(factStr):
    tempFact = factStr
    if tempFact.startswith("flow("):
        para1 = str(tempFact.split(",")[0][5:])
        para2 = str(tempFact.split(",")[1][:-1])
        query = Query(flow(para1,para2))
    elif tempFact.startswith("control("):
        para1 = str(tempFact.split(",")[0][8:])
        para2 = str(tempFact.split(",")[1][:-1])
        query = Query(control(para1,para2))
    elif tempFact.startswith("refF("):
        para1 = str(tempFact.split(",")[0][5:])
        para2 = str(tempFact.split(",")[1][:-1])
        query = Query(refF(para1,para2))
    elif tempFact.startswith("defF("):
        para1 = str(tempFact.split(",")[0][5:])
        para2 = str(tempFact.split(",")[1][:-1])
        query = Query(defF(para1,para2))
    elif tempFact.startswith("dataDepF("):
        para1 = str(tempFact.split(",")[0][8:])
        para2 = str(tempFact.split(",")[1])
        para3 = str(tempFact.split(",")[2][:-1])
        query = Query(dataDepF(para1,para2,para3))
    if query.nextSolution():
        #print("already exsit")
        query.closeQuery()
        return False
    query.closeQuery()
    return True

       
mainStr = "method(A,B,C,D,E)"
entryP = str()
entryLab = str()
mainDefFact = str()
mainM = str()
for solution in prolog.query(mainStr):
    queryMethod = solution["C"]        
    queryMethodBeg = queryMethod.find("(m")
    queryMethod = queryMethod[queryMethodBeg+1:-1]   
    if queryMethod == "mmain":
        mainM = solution["A"] +solution["C"]
        mainParaList = solution["D"]
#         print(mainParaList)
        if isinstance(mainParaList, str):
            while mainParaList.find("(type_") != -1:
                mainDefFact = mainDefFact + "defF(" + mainM + "," + mainParaList[mainParaList.find("type_"):mainParaList.find("),")+1].replace("(", "_").replace(")","") + ");"
                mainParaList = mainParaList[mainParaList.find("),")+1:]
            mainDefFact = mainDefFact + "defF(" + mainM + "," + mainParaList[mainParaList.find("type_"):mainParaList.rfind(")))))")].replace("(", "_").replace(")","") + ")"
        entryP = solution["E"]
        break

while mainDefFact.find('defF(') != -1:
#     print(mainDefFact.split(';',1)[0])
    prolog.assertz(mainDefFact.split(';',1)[0])
    try:
        mainDefFact = mainDefFact.split(';',1)[1]
    except:
        mainDefFact = str()


if entryP != "":#self-definition method
    entryLabStr = "entry_point("+ entryP+",ELab)"
    for solution in prolog.query(entryLabStr):  
        entryLab = solution["ELab"]
      
find_instr = Functor("find_instr",3)#add new fact,rule to the .pl file
prolog.assertz("find_instr(X,Y,Z):-instr(X,Y,Z)")#the definition of fact or gule
X = Variable()
# lab1 = "fD__workspace_antlr_C_DynamixMem_c___mmain_r3c3"
lab1 = entryLab
flowM2Ep = "flow("+mainM+","+lab1+")"
prolog.assertz(flowM2Ep)

Y = Variable()
Z = Variable()
V = Variable()
# lab1 = "fD__workspace_swipl_tryEX_c___mmain_r17c3"
q = Query(find_instr(lab1,Y,Z))

while True:
#     if q.nextSolution() and (Z.value.__str__() != ("ret" or "end")) :
    if q.nextSolution() :        
#         print("The instr of " + lab1 + " is:    " + Y.value.__str__())
#         print(" and the next instr is in:" + Z.value.__str__())
        instr = Y.value.__str__()
        tempLab = lab1
        lab1 = Z.value.__str__()
        lab2 = Z.value.__str__()
        q.closeQuery()
        if not (instr.startswith("ite(") or instr.startswith("switch(")):
            if instr.startswith("for(") or instr.startswith("while("):
                IniflowFact = "flow("+tempLab+","+lab1+")"   
                controlFact = computeControl(tempLab,lab1)
                if controlFact.startswith("control(") and notExsitFact(controlFact):
                    prolog.assertz(controlFact)
            else:
                IniflowFact = "flow("+tempLab+","+lab1+")"
                controlFact = computeControl(tempLab,lab1)
                if controlFact.startswith("control(") and notExsitFact(controlFact):
                    prolog.assertz(controlFact)
                            

        if instr.startswith("case_"):
            beg = instr.find("(")
            instr = instr[beg+1:-1]            
        if instr.startswith("assign(") or instr.startswith("for(") or instr.startswith("while(") or instr.startswith("ite(") or instr.startswith("switch(") or instr.startswith("call_m"):
            fact = str() 
            if instr.startswith("assign("):
                fact = dealWithAssignInstr(tempLab,instr,lab1)
                
                if not fact.startswith("defF("):
                    nextLab = fact[:fact.find(";")]
                    lab1 = nextLab
                    fact = fact[fact.find(";")+1:]
            elif instr.startswith("for("):
                fact = dealWithForInstr(tempLab, instr, lab1)
                nextLab = fact[:fact.find(";")]
                lab1 = nextLab
                fact = fact[fact.find(";")+1:]
            elif instr.startswith("while("):
                fact = dealWithWhileInstr(tempLab, instr, lab1)
                nextLab = fact[:fact.find(";")]
                lab1 = nextLab
                fact = fact[fact.find(";")+1:]
            elif instr.startswith("ite("):
                fact = dealWithIteInstr(tempLab, instr, lab1)
                nextLab = fact[:fact.find(";")]
                lab1 = nextLab
                fact = fact[fact.find(";")+1:]
            elif instr.startswith("switch("):
                fact = dealWithSwitchInstr(tempLab, instr, lab1)
                nextLab = fact[:fact.find(";")]
                lab1 = nextLab
                fact = fact[fact.find(";")+1:]
            elif instr.startswith("call_m"):
                if tempLab in iteStack.keys():
                    fact = dealWithCallMInstr(tempLab, instr, iteStack[tempLab])
                elif  tempLab in switchStack.keys():
                    fact = dealWithCallMInstr(tempLab, instr, switchStack[tempLab])
                elif tempLab in loopStack.keys():
                    fact = dealWithCallMInstr(tempLab, instr, loopStack[tempLab])
                else:
                    fact = dealWithCallMInstr(tempLab, instr, lab1)
                if not fact.startswith("refF") and len(fact) > 0:
                    nextLab = fact[:fact.find(";")]
                    lab1 = nextLab
                    fact = fact[fact.find(";")+1:]
                                  
            while fact.find(";") != -1:   
                end = fact.find(";")
                if notExsitFact(fact[0:end]):
                    prolog.assertz(fact[0:end])
                fact = fact[end+1:]
            if len(fact) > 0 and notExsitFact(fact):
                prolog.assertz(fact) 
                 
    else:
        break
    #Computing control dependencies in control module 
    controlFact = computeControl(tempLab,lab1)

    if controlFact.startswith("control(") and notExsitFact(controlFact):
        prolog.assertz(controlFact)
    
   
    if tempLab in iteStack.keys():
        if lab1 != iteStack[tempLab].split(";")[0] and bt(iteStack[tempLab].split(";")[-1],lab1):
            iteStack[lab1] = iteStack[tempLab]
        elif not tempLab in callMStack.keys() and tempLab != iteStack[tempLab].split(";")[0]:
            lab1 = iteStack[tempLab].split(";")[0]
        #del iteStack[tempLab]       
    if tempLab in switchStack.keys():
        if lab1 != switchStack[tempLab].split(";")[0] and bt(switchStack[tempLab].split(";")[-1],lab1):
            switchStack[lab1] = switchStack[tempLab]
        elif not tempLab in callMStack.keys() and tempLab != switchStack[tempLab].split(";")[0]:
            lab1 = switchStack[tempLab].split(";")[0]
    
    if tempLab in loopStack.keys() and not lab1 in loopStack.keys() and bt(loopStack[tempLab],lab1):
        loopStack[lab1] = loopStack[tempLab]
    elif tempLab in loopStack.keys() and lab1 in loopStack.keys():
        lab1 = loopStack[tempLab] 
        IniflowFact = IniflowFact.split(",",1)[0]+",r"+IniflowFact.split(",",1)[1]

    
    if tempLab in callMStack.keys() and tempLab[tempLab.rfind("_c___m")+6:tempLab.rfind("_r")] != "main":#method which is not main,deal its return or end 
#         if lab1 != "ret" and lab1 != "end":
        if not lab1.endswith("ret") and not lab1.endswith("end"):
            callMStack[lab1] = callMStack[tempLab]
            del callMStack[tempLab]
        else:
            if callMStack[tempLab].find(";")!=-1:
                lab1 = callMStack[tempLab].split(";",1)[0] 
                callMStack = callMStack[tempLab].split(";",1)[1]
            else:
                lab1 = callMStack[tempLab]
    if notExsitFact(IniflowFact):      
        prolog.assertz(IniflowFact)
    q = Query(find_instr(lab1,Y,Z))
q.closeQuery()


print("%flowFact")
controlQ = Query(flow(X,Y))
while controlQ.nextSolution():
    print("flow("+X.value.__str__()+","+Y.value.__str__()+").")
controlQ.closeQuery()#remember to close the query
print("%defFact")
controlQ = Query(defF(X,Y))
while controlQ.nextSolution():
    print("defF("+X.value.__str__()+","+Y.value.__str__()+").")
controlQ.closeQuery()#remember to close the query
print("%refFact")
controlQ = Query(refF(X,Y))
while controlQ.nextSolution():
    print("refF("+X.value.__str__()+","+Y.value.__str__()+").")
controlQ.closeQuery()#remember to close the query
print("%controlFact")
controlQ = Query(control(X,Y))
while controlQ.nextSolution():
    print(controlQ.nextSolution())
    print("control("+X.value.__str__()+","+Y.value.__str__()+").")
# print(controlQ.nextSolution())
controlQ.closeQuery()#remember to close the query
#compute data dependence
# dataDep = Functor("dataDep",3)
# prolog.assertz("dataDep(M,N,X):-flow(M,N),refF(N,X),defF(M,X)")
# prolog.assertz("dataDep(M,N,X):-purepath(M,T,X),flow(T,N),refF(N,X),defF(M,X)")
#   
# purepath = Functor("purepath",3)
# prolog.assertz("purepath(M,N,X):-flow(M,N),\+defF(N,X)")
# prolog.assertz("purepath(M,N,X):-purepath(M,T,X),flow(T,N),\+defF(T,X),M \== N")
# purepath = Functor("purepath",3)
# prolog.assertz("purepath(X,Y,V):-flow(X,Y),\+defF(Y,V)")
# prolog.assertz("purepath(X,Y,V):-flow(T,Y),purepath(X,T,V),\+defF(Y,V)")

purepath = Functor("purepath",3)
# prolog.assertz("purepath(X,Y,V):-!")
prolog.assertz("purepath(X,Y,V):-flow(X,Y),defF(X,V)")
prolog.assertz("purepath(X,Y,V):-flow(T,Y),purepath(X,T,V),\+defF(T,V)")

# purepath = Functor("purepath",3)
# # prolog.assertz("purepath(X,Y,V):-!")
# prolog.assertz("purepath(X,Y,V):-flow(X,Y),defF(X,V)")
# prolog.assertz("purepath(X,Y,V):-flow(T,Y),purepath(X,T,V),\+refF(T,V)")

# path = Functor("path",2)
# prolog.assertz("path(X,Y):-flow(X,Y)")
# prolog.assertz("flow(X,Y)")
# prolog.assertz("path(X,Y):-path(X,T),flow(T,Y)") 
# prolog.assertz("path(X,Y):-flow(X,T),path(T,Y)") 

print("%purepathFact")
purepathQ = Query(purepath(X,Y,V))
while purepathQ.nextSolution():
    print("purepath("+X.value.__str__()+","+Y.value.__str__()+","+V.value.__str__()+").")
#     print(purepathQ.nextSolution())
#     print("1")
purepathQ.closeQuery()

print("1")
dataDep = Functor("dataDep",3)
prolog.assertz("dataDep(X,Y,V):-flow(X,Y),refF(Y,V),defF(X,V)")
prolog.assertz("dataDep(X,Y,V):-flow(T,Y),purepath(X,T,V),refF(Y,V),defF(X,V)")
  



dataDepStack = {}

def time_limit(interval):
    @wraps(interval)
    def deco(func):
        def time_out():
            print("time_out_error")
            period1EndTime = time.time()
#             timeStack.append(period1EndTime)
            timeStack["period1EndTime"] = period1EndTime
            print()
            print("time_limit:")
            print(timeStack)
#             print("end Compute Data Dependence Time:"+str(timeStack[1]-timeStack[0]))
            print("end Compute Data Dependence Time:"+str(timeStack["period1EndTime"]-timeStack["period1StartTime"]))
#             pthread_exit()
            raise TimeoutError()
        @wraps(func)
        def deco(*args, **kwargs):
            timer = Timer(interval, time_out)
            timer.start()
            res = func(*args, **kwargs)
            return res
        return deco
    return deco

# @time_limit(2)
# # @timeout(5)
# def computeDataDep(q):
# #     q = Query(dataDep(X,Y,V))
#     while q.nextSolution():
#         keyStr = X.value.__str__()
#         valueStr = Y.value.__str__()+"^"+V.value.__str__()
#         print("dataDep:"+keyStr+","+valueStr)
#         if keyStr in dataDepStack.keys():
#             if dataDepStack[keyStr].find(valueStr) == -1:
#                 dataDepStack[keyStr] = dataDepStack[keyStr]+valueStr+";"
#         else:
#             dataDepStack[keyStr] = valueStr+";"
#         period1EndTime = time.time()
#         timeStack["period1EndTime"] = period1EndTime

@time_limit(10)
# @timeout(5)
def computeDataDep(q,var):
#     q = Query(dataDep(X,Y,V))
    print()
    print("computeDataDep: 1")
    print(var+" query")
    while q.nextSolution():
#     if q.nextSolution():
        print("computeDataDep: 2")
        keyStr = X.value.__str__()
        print("computeDataDep: 3")
        valueStr = Y.value.__str__()+"^"+var
        print("computeDataDep: 4")
        print("dataDep:"+keyStr+","+valueStr)
        if keyStr in dataDepStack.keys():
            print("computeDataDep: 5")
            if dataDepStack[keyStr].find(valueStr) == -1:
                print("computeDataDep: 6")
                dataDepStack[keyStr] = dataDepStack[keyStr]+valueStr+";"
                print("computeDataDep: 7")
        else:
            print("computeDataDep: 8")
            dataDepStack[keyStr] = valueStr+";"
            print("computeDataDep: 9")
        period1EndTime = time.time()
        print("computeDataDep: 10")
        timeStack["period1EndTime"] = period1EndTime
        print("computeDataDep: 11")
#         continue
#     q.closeQuery()
          
# # q = Query(dataDep(X,"fD__workspace_antlr_C_sqrtTest_c___mmain_r5c1",V))
# q = Query(dataDep(X,Y,V))
# try:    
#     computeDataDep(q)
# except TimeoutError:
#     print("query end close")
# finally:
#     q.closeQuery()
#     period2StartTime = time.time()
# #     timeStack.append(period2StartTime)
#     timeStack["period2StartTime"] = period2StartTime
# #     print("1"+str(timeStack))
#     print("time error time:"+str(timeStack["period2StartTime"]-timeStack["period1EndTime"]))
#     print("Input To EDataDepTime:"+str(timeStack["period1EndTime"]-timeStack["period1StartTime"]))
paraStr = "defF(A,B)"
for solution in prolog.query(paraStr):
    para = solution["B"]
    print(para)
    if para not in varStack:
        varStack.append(para)

print("varStack:")
print(varStack)
while varStack:
    var = varStack.pop()
    q = Query(dataDep(X,Y,var))
    print("dead lock")
    try:  
        print('error here 1')  
        computeDataDep(q,var)
        print("error here 2")
    except TimeoutError:
        print(var+" query end close")
    finally:
        q.closeQuery()  
print('error here 3')
period2StartTime = time.time()
#     timeStack.append(period2StartTime)
timeStack["period2StartTime"] = period2StartTime
#     print("1"+str(timeStack))
print("time error time:"+str(timeStack["period2StartTime"]-timeStack["period1EndTime"]))

print("Input To EDataDepTime:"+str(timeStack["period1EndTime"]-timeStack["period1StartTime"]))
    
ks = dataDepStack.keys()
count = 0
for key in ks:
#     print(key+dataDepStack[key])
    while dataDepStack[key].find(";") != -1:
        count = count+1
        dataDepFact = "dataDepF("+key+","+dataDepStack[key].split(";",1)[0].split("^")[0]+","+str(dataDepStack[key].split(";",1)[0].split("^")[1]).replace("(","_").replace(")","")+")"
        print("assert: "+dataDepFact)
        prolog.assertz(dataDepFact)
        dataDepStack[key] = dataDepStack[key].split(";",1)[1]


#compute the depth of the sliceS
# path = Functor("path",3)
# prolog.assertz("path(X,Y,D):-flow(X,Y),D is 1")
# prolog.assertz("path(X,Y,D):-path(X,T,TD),flow(T,Y),D is TD+1")
# depth = {}        
# 
# D = Variable()
# @time_limit(1)
# def computeDepth(query):
#     while query.nextSolution():
#         if int(D.value.__str__()) > depth[sliceLab]:
#             depth[sliceLab] = int(D.value.__str__())
#             
# depth[sliceLab] = 0
# depQuery = Query(path(entryLab,sliceLab,D))
# try:   
#     endTime = time.time()
#     print("depth start:"+str(endTime-startTime))  
#     computeDepth(depQuery)
# except TimeoutError as e:
#     print("query end close")
# finally:
#     depQuery.closeQuery()
#     endTime = time.time()
#     print("depth query time_out_error:"+str(endTime-startTime))
#  
# print(depth)

print("SLICE BELOW:-----------------------------")

# print("%flowFact")
# controlQ = Query(flow(X,Y))
# while controlQ.nextSolution():
#     print("flow("+X.value.__str__()+","+Y.value.__str__()+").")
# controlQ.closeQuery()#remember to close the query
# print("%defFact")
# controlQ = Query(defF(X,Y))
# while controlQ.nextSolution():
#     print("defF("+X.value.__str__()+","+Y.value.__str__()+").")
# controlQ.closeQuery()#remember to close the query
# print("%refFact")
# controlQ = Query(refF(X,Y))
# while controlQ.nextSolution():
#     print("refF("+X.value.__str__()+","+Y.value.__str__()+").")
# controlQ.closeQuery()#remember to close the query
# print("%controlFact")
# controlQ = Query(control(X,Y))
# while controlQ.nextSolution():
#     print("control("+X.value.__str__()+","+Y.value.__str__()+").")
# controlQ.closeQuery()#remember to close the query
print("%dataDepFact")
controlQ = Query(dataDepF(X,Y,"type_int_iv"))
while controlQ.nextSolution():
    count = count+1
    print("dataDepF("+X.value.__str__()+","+Y.value.__str__()+","+V.value.__str__()+").")
controlQ.closeQuery()#remember to close the query

# depth = {}  
# depth[sliceLab] = 0
# endTime = time.time()
# print("start slice:"+str(endTime-startTime))
# 
# weightQ = [sliceLab]
# M = {sliceLab:2**depth[sliceLab]}
# depPre = []
# dDepPre = []
# wFlag = False
# R = []
# #count = 0
# sliceflow = Functor("sliceflow",2)
# 
# while weightQ:
#     n = weightQ.pop()
#     wFlag = False
#     if n in R:
#         continue
#     else:
#         R.append(n)
#     depPreQuery = Query(control(X,n))
#     while depPreQuery.nextSolution():
#         depPre.append(X.value.__str__())
#     depPreQuery.closeQuery()
#     depPreQuery = Query(dataDepF(X,n,Y))
#     while depPreQuery.nextSolution():
#         depPre.append(X.value.__str__())
#         dDepPre.append(X.value.__str__())
#     depPreQuery.closeQuery()
#     while depPre:
#         m = depPre.pop()
#         depth[m] = depth[n]-1
#         if m in M.keys():
#             wFlag = True
#             continue
#         weight = M[n]- (2**depth[m]/3)
#         if m in dDepPre:
#             weight = weight- (2**depth[m]/3)
#         else:
#             weight = weight- (2**depth[m]/3*2)
#         weightQ.append(m)
#         M[m] = weight
#     if wFlag:
#         continue     

depth = {}  
depth[sliceLab] = 0


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
print("slice time:"+str((timeStack["period1EndTime"]-timeStack["period1StartTime"])+(timeStack["period2EndTime"]-timeStack["period2StartTime"])))
      
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

if eaChoose == "Y":
    cc = rouletteWheelSelection(M)  
    print(cc)
    cc = rouletteWheelSelection(instrM)  
    print("rouletteWheelSelection"+str(cc))



# def computeSliceFlow(sliceStack,preLab,curLabel):
#     sliceflowFact = str()
#     if preLab in sliceStack:
# #         print(sliceStack)
#         sliceflowFact = "sliceflow("+preLab+","+curLabel+");"
# #         print("1:"+curLabel+" "+sliceflowFact)
#         return sliceflowFact
#     else:
#         preLabelQ = Query(flow(X,preLab))
#         ppreLabelS = []
#         while preLabelQ.nextSolution():
#             ppreLabelS.append(X.value.__str__())
#         preLabelQ.closeQuery()
#         while ppreLabelS:
#             ppreLabel = ppreLabelS.pop()
#             sliceflowFact = sliceflowFact + computeSliceFlow(sliceStack, ppreLabel,curLabel)
# #             print("2:"+curLabel+" "+sliceflowFact)
#         return sliceflowFact
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

