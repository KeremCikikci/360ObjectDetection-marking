#from object_detection import *
#import virtual_room
import time


from sensors import *

def scann2(maxXStep, maxYStep, scanningPrecision, delay):
    xPartStep = int(maxXStep / scanningPrecision)  # Hassasiyete göre bir haraketteki motor adımı sayısı
    yPartStep = int(maxYStep / scanningPrecision)

    for xPart in range(scanningPrecision):
        for yPart in range(scanningPrecision):  # Y ekseninde hassasiyete göre durarak tarıyor
            for y in range(yPartStep):
                yForward()
            time.sleep(delay)

        for back in range(
                scanningPrecision):  # Y eksenindeki tarama bittiğinde en altta olduğundan tekrardan üste alıyor
            for y in range(yPartStep):
                yBack()

        if xPart < scanningPrecision:
            for x in range(xPartStep):  # X ekseninde hassasiyete göre durarak tarıyor
                xForward()
            time.sleep(delay)

""" Mod1 """
# Bütün ortamı tarar ve nesneleri kaydeder

#reset()
# Go(startX, startY) #Başlangış kordinatları x,y
# time.sleep(5)
#takePhotos()
markTheObjects('diningtable')
while True:
    lazer.write(1)

""" Mod2 """
# Ayarlanmış yerde nesneleri tanır

