from operator import itemgetter
from graph import plotter
from random import uniform
def combine(megaArray): #combines the elements together
    startIndex = 0 #start at the beginning of the large array
    for array in megaArray: #goes through the array
        index = 0
        for dictionary in array: #for each dictionary in each of five arrays
            if dictionary["gesture"] != "Unknown":
               if index > startIndex:
                  startIndex = index
                  break
            else:
               index = index + 1
    endIndices = [len(array) for array in megaArray] #this is the end index itself- picks smallest index to be found
    endIndex = min(endIndices)
    for array in megaArray: #loops through array in megaarray
        array = array[startIndex:endIndex]
    newArray = [0] * len(megaArray[0])
    for i in range(len(newArray)): #goes through and averages the angles and accelerations for combination
        pitch = (megaArray[0][i]["pitch"] + megaArray[1][i]["pitch"] + megaArray[2][i]["pitch"] + megaArray[3][i]["pitch"] + megaArray[4][i]["pitch"]) / 5.0
        roll =  (megaArray[0][i]["roll"] + megaArray[1][i]["roll"] + megaArray[2][i]["roll"] + megaArray[3][i]["roll"] + megaArray[4][i]["roll"]) / 5.0
        yaw =  (megaArray[0][i]["yaw"] + megaArray[1][i]["yaw"] + megaArray[2][i]["yaw"] + megaArray[3][i]["yaw"] + megaArray[4][i]["yaw"]) / 5.0
        accelerationX =  (megaArray[0][i]["accelerationX"] + megaArray[1][i]["accelerationX"] + megaArray[2][i]["accelerationX"] + megaArray[3][i]["accelerationX"] + megaArray[4][i]["accelerationX"]) / 5.0
        accelerationY =  (megaArray[0][i]["accelerationY"] + megaArray[1][i]["accelerationY"] + megaArray[2][i]["accelerationY"] + megaArray[3][i]["accelerationY"] + megaArray[4][i]["accelerationY"]) / 5.0
        accelerationZ =  (megaArray[0][i]["accelerationZ"] + megaArray[1][i]["accelerationZ"] + megaArray[2][i]["accelerationZ"] + megaArray[3][i]["accelerationZ"] + megaArray[4][i]["accelerationZ"]) / 5.0
        rollDic = {} #this holds classification counts
        for j in range(5):
            if megaArray[j][i]["gesture"] not in rollDic:
               rollDic[megaArray[j][i]["gesture"]] = 1
            else:
               rollDic[megaArray[j][i]["gesture"]] += 1
        classification = max([(gesture, count) for gesture, count in rollDic.items()], key = itemgetter(1))[0]
        diction = {"pitch" : pitch, "roll" : roll, "yaw" : yaw, "accelerationX" : accelerationX,  "accelerationY" : accelerationY,  "accelerationZ" : accelerationZ,  "gesture" : classification}
        newArray[i] = diction
    return newArray

def compare(megaArray): #this method comapres the student and teacher arrays
    sInitial = 0
    tInitial = 0
    studentArray = megaArray[0]
    teacherArray = megaArray[1]
    for i in range(len(teacherArray)): #this method looops through the teacher array
        if teacherArray[i] != "Unknown":
           tInitial = i
           break
    for j in range(len(studentArray)): #this method loops through the student array
        if studentArray[j] != "Unknown":
           sInitial = j
           break
    startIndex = max(sInitial, tInitial)
    endIndices = [len(array) for array in megaArray] #this is the end index itself- picks smallest index to be found
    endIndex = min(endIndices)
    studentArray = studentArray[startIndex: endIndex]
    teacherArray = teacherArray[startIndex: endIndex]
    sumPercentError = 0
    numGestureMismatches = 0
    yawErrors = []
    pitchErrors = []
    rollErrors = []
    accelerXErrors = []
    accelerYErrors = []
    accelerZErrors = []
    for i in range(len(studentArray)): #this goes through the whole student array itself
             student = studentArray[i]
             teacher = teacherArray[i]
             yawError = abs(teacher["yaw"] - student["yaw"])/teacher["yaw"]
             pitchError = abs(teacher["pitch"] - student["pitch"])/teacher["pitch"]
             rollError = abs(teacher["roll"] - student["roll"])/teacher["roll"]
             yawErrors.append(yawError)
             pitchErrors.append(pitchError)
             rollErrors.append(rollError)
             accelXError = abs(teacher["accelerationX"] - student["accelerationX"])/teacher["accelerationX"]
             accelYError = abs(teacher["accelerationY"] - student["accelerationY"])/teacher["accelerationY"]
             accelZError = abs(teacher["accelerationZ"] - student["accelerationZ"])/teacher["accelerationZ"]
             accelerXErrors.append(accelXError)
             accelerYErrors.append(accelYError)
             accelerZErrors.append(accelZError)
             if teacher["gesture"] != student["gesture"]: #if gestures dont match, skip and just add to mismatches
                     numGestureMismatches += 1
             else:
                averageError = (yawError + pitchError + rollError + accelXError + accelYError + accelZError)/6.0
                sumPercentError += averageError
    plotter((yawErrors,pitchErrors, rollErrors), "angle")
    plotter((accelerXErrors, accelerYErrors, accelerZErrors), "accel")
    totalError = (100) - (100*sumPercentError/len(studentArray)) - ((100.0/(len(studentArray))) * numGestureMismatches) #this is percent correct equation with a discount based on gesture mismatches
    return totalError




testDict = {"pitch" : 10.0, "roll":20.0, "yaw":35.0, "accelerationX":32.0, "accelerationY":40.0, "accelerationZ":75.0, "gesture":"FingersSpread"}
testDictTwo = {"pitch" : 9.0, "roll":22.0, "yaw":31.5, "accelerationX":35.2, "accelerationY":44.0, "accelerationZ":67.5, "gesture":"FingersSpread"}
testDictThree = {"pitch" : 20, "roll":43, "yaw":31, "accelerationX":40, "accelerationY":60, "accelerationZ":35,"gesture":"Fist"}
testDictFour = {"pitch" : 20, "roll":43, "yaw":31, "accelerationX":40, "accelerationY":60, "accelerationZ":35, "gesture":"Fingers"}
testDictFive = {"pitch" : 20, "roll":43, "yaw":31, "accelerationX":40, "accelerationY":60, "accelerationZ":35, "gesture":"WaveIn"}

li = []
liTwo = []
liThree = []
for i in range(300):
    li.append({"pitch" : uniform(20, 70), "roll":uniform(40, 95), "yaw":uniform(30, 90), "accelerationX":32.0, "accelerationY":40.0, "accelerationZ":75.0, "gesture":"FingersSpread"})
for j in range(300):
    liTwo.append({"pitch" : uniform(20, 70), "roll":uniform(40, 95), "yaw":uniform(30, 90), "accelerationX":35.2, "accelerationY":44.0, "accelerationZ":67.5, "gesture":"FingersSpread"})
liThree.append(liTwo)
liThree.append(li)
print compare(liThree)
