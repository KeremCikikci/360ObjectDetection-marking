import os
import time

import cv2

def rowStitch():
	fotoSet = '7'

	mainFolder = 'fotos/' + fotoSet
	myFolders = os.listdir(mainFolder)
	print(myFolders)

	panoramaticDir = 'panoramaImages/' + fotoSet

	os.mkdir(panoramaticDir)

	for folder in myFolders:
		path = mainFolder + '/' + folder
		images = []
		myList = os.listdir(path)
		print(f'Total number of images detected {len(myList)}')
		for imgN in myList:
			curImg = cv2.imread(f'{path}/{imgN}')
			images.append(curImg)

		stitcher = cv2.Stitcher.create()
		(status, result) = stitcher.stitch(images)
		if (status == cv2.STITCHER_OK):
			print('Panorama Generated')
			cv2.imshow(folder, result)
			cv2.waitKey(1)
			dir = 'panoramaImages/' + fotoSet + '/' + folder
			os.mkdir(dir)
			cv2.imwrite(dir + '/panoramaticResult.png', result)
		else:
			print('Panorama Generatation Unsuccessful')
	cv2.waitKey(0)

def normalStitch():
	fotoSet = '2'

	mainFolder = 'fotos'
	myFolders = os.listdir(mainFolder)
	print(myFolders)

	for folder in myFolders:
		path = mainFolder + '/' + folder
		images = []
		myList = os.listdir(path)
		print(f'Total number of images detected {len(myList)}')
		for imgN in myList:
			curImg = cv2.imread(f'{path}/{imgN}')
			images.append(curImg)

		stitcher = cv2.Stitcher.create()
		(status, result) = stitcher.stitch(images)
		if (status == cv2.STITCHER_OK):
			print('Panorama Generated')
			cv2.imshow(folder, result)
			cv2.waitKey(1)
			dir = 'panoramaImages/' + fotoSet
			os.mkdir(dir)
			cv2.imwrite(dir + '/panoramaticResult.png', result)
		else:
			print('Panorama Generatation Unsuccessful')
	cv2.waitKey(0)

normalStitch()