import os
import time
from pyfirmata import Arduino, util
import os, os.path
import cv2

objects = [[339, 15, 709, 422, 369, 397, 'person'], [67, 256, 709, 422, 145, 92, 'diningtable'], [225, 134, 709, 422, 90, 203, 'refrigerator'], [90, 280, 709, 422, 61, 74, 'chair'], [322, 241, 709, 422, 82, 177, 'bed'], [5, 289, 709, 422, 74, 113, 'chair']]

# oran 25x13

maxXStep = 300 #1500
maxYStep = 156 #500
scanningPrecision = 5
delay = 1

startX = 1000
startY = 200

"""               Main                 """

board = Arduino('COM4')

iterator = util.Iterator(board)
iterator.start()

lazer = board.get_pin('d:8:o')
xSwitch = board.get_pin('d:9:i')
ySwitch = board.get_pin('d:10:i')

xMotorDir = board.get_pin('d:5:o')
xMotorPulse = board.get_pin('d:2:o')
yMotorDir = board.get_pin('d:6:o')
yMotorPulse = board.get_pin('d:3:o')

def xForward():
    xMotorDir.write(1)
    xMotorPulse.write(1)
    xMotorPulse.write(0)

def xBack():
    xMotorDir.write(0)
    xMotorPulse.write(1)
    xMotorPulse.write(0)

def yForward():
    yMotorDir.write(0)
    yMotorPulse.write(1)
    yMotorPulse.write(0)

def yBack():
    yMotorDir.write(1)
    yMotorPulse.write(1)
    yMotorPulse.write(0)

def reset():
    while True:
        yBack()
        yLastPoint = ySwitch.read()
        print("y0")
        if yLastPoint is None:
            yLastPoint = 0
        if yLastPoint == 1:
            print("y1")
            yForward()

            while True:
                xBack()
                xLastPoint = xSwitch.read()
                print("x0")
                if xLastPoint is None:
                    xLastPoint = 0
                if xLastPoint == 1:
                    xForward()
                    print("x1")
                    break
            break

def scann(maxXStep, maxYStep, scanningPrecision, delay):
    xPartStep = int(maxXStep / scanningPrecision)  # Hassasiyete göre bir haraketteki motor adımı sayısı
    yPartStep = int(maxYStep / scanningPrecision)

    for xPart in range(scanningPrecision):
        for yPart in range(scanningPrecision):  # Y ekseninde hassasiyete göre durarak tarıyor
            for y in range(yPartStep):
                yForward()
            time.sleep(delay)

        for back in range(scanningPrecision):  # Y eksenindeki tarama bittiğinde en altta olduğundan tekrardan üste alıyor
            for y in range(yPartStep):
                yBack()

        if xPart < scanningPrecision:
            for x in range(xPartStep):  # X ekseninde hassasiyete göre durarak tarıyor
                xForward()
            time.sleep(delay)

def Go(startX, startY):
    for x in range(startX):
        xForward()
    for y in range(startY):
        yForward()


def takePhotos(): # bütün fotolar bir klasöre

    for i in range(startX):
        xForward()
    for i in range(startY):
        yForward()

    FOTOS_FOLDER = 'C:/Users/kerem/PycharmProjects/pythonProject2/fotos/'

    totalFiles = 0
    totalDir = 0

    for base, dirs, files in os.walk(FOTOS_FOLDER):
        print('Searching in : ', base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1

    print(totalDir)
    dir = "fotos/" + str(totalDir + 1)
    os.mkdir(dir)

    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)

    xPartStep = int(maxXStep / scanningPrecision)  # Hassasiyete göre bir haraketteki motor adımı sayısı
    yPartStep = int(maxYStep / scanningPrecision)

    fotos = 0
    for yPart in range(scanningPrecision):
        for xPart in range(scanningPrecision):
            fotos += 1

            ret, frame = cap.read()
            for x in range(xPartStep):
                xForward()
            time.sleep(delay)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(dir + '/c' + str(fotos) + '.png', frame)
            cv2.destroyAllWindows()

        for back in range(scanningPrecision * xPartStep):  # X eksenindeki tarama bittiğinde en sonda olduğundan tekrardan geri dönüyor
            xBack()
        time.sleep(1)

        if yPart < scanningPrecision:
            for y in range(yPartStep):  # Y ekseninde hassasiyete göre durarak tarıyor
                yForward()


    cap.release()

def takePhotos2(): # fotolar satır satır bölünür

    for i in range(startX):
        xForward()
    for i in range(startY):
        yForward()

    FOTOS_FOLDER = 'C:/Users/kerem/PycharmProjects/pythonProject2/fotos/'

    totalFiles = 0
    totalDir = 0

    for base, dirs, files in os.walk(FOTOS_FOLDER):
        print('Searching in : ', base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1

    print(totalDir)
    dir = "fotos/" + str(totalDir + 1)
    os.mkdir(dir)

    cap = cv2.VideoCapture(0)

    xPartStep = int(maxXStep / scanningPrecision)  # Hassasiyete göre bir haraketteki motor adımı sayısı
    yPartStep = int(maxYStep / scanningPrecision)

    fotos = 0
    for yPart in range(scanningPrecision):
        dir2 = dir + '/row' + str(yPart)
        os.mkdir(dir2)
        for xPart in range(scanningPrecision):

            for base, dirs, files in os.walk(FOTOS_FOLDER + str(totalDir + 1)):
                for Files in files:
                    fotos += 1

            ret, frame = cap.read()
            for x in range(xPartStep):
                xForward()
            time.sleep(delay)
            cv2.imwrite(dir2 + '/c' + str(fotos) + '.png', frame)
            cv2.destroyAllWindows()

        for back in range(scanningPrecision * xPartStep):  # X eksenindeki tarama bittiğinde en sonda olduğundan tekrardan geri dönüyor
            xBack()
        time.sleep(1)

        if yPart < scanningPrecision:
            for y in range(yPartStep):  # Y ekseninde hassasiyete göre durarak tarıyor
                yForward()


    cap.release()


def markTheObjects(object):
    for i in range(len(objects)):
        objectName = objects[i][6]

        x = objects[i][0] # objenin resimdeki konumu
        y = objects[i][1]
        width = objects[i][2]  # resmin boyutu
        height = objects[i][3]
        objectW = objects[i][4]   # Obje kutusunun boyutu
        objectH = objects[i][5]

        if objectName == object:
            objectX = (maxXStep - int((maxXStep / width) * x)) + startX - int(maxXStep * objectW / width / 2)
            objectY = int((maxYStep / height) * y) + startY + int(maxYStep * objectH / height / 2)

            print('x: ' + str(objectX) + "   y: " + str(objectY))

            for x in range(objectX):
                xForward()
            for y in range(objectY):
                yForward()
