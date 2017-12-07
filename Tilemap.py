import pygame
import sys
import random as Random
from pygame.locals import *
from createMap import start

class Tilemap:
	start()
	def __init__(self):
		global FILENAME
		global level
		global PLAYER


		FILENAME = "map.txt"
		try:
			# create tilemap
			with open(FILENAME) as textFile:
				level = [list(row) for row in file.read(textFile).split('\n')]

		except IOError:
			print "Filename nout found!"

	# colors
		BLACK = (0,   0,   0  )
		DIRT  = (140, 85,  67 )
		GREEN = (0,   255, 0  )
		BLUE  = (0,   0,   255)
		GRAY  = (100, 100, 100)
		WHITE = (255, 255, 255)

	# tiles
		WALL   = "#"
		PLAYER = "@"
		FLOOR  = "."
		ITEM   = "X"
		BLANK  = "_"

	# Link colors to tiles
		colors = {
				PLAYER : GREEN,
				WALL   : GRAY,
				FLOOR  : DIRT,
				ITEM   : BLUE,
				BLANK  : WHITE
				}

	def setPlayer(self, posX, posY):
		level[posX][posY] = "@"

	def setFloor(self, posX, posY):
		level[posX][posY] = "."


	def getHeight(self):
		MAPHEIGHT = len(level)-1
		return MAPHEIGHT

	def getWidth(self):
		MAPWIDTH = len(level[0])
		return MAPWIDTH


	def placeItem(self, numItems):
		placedItems = 0
		while placedItems < numItems:
			row = Random.randint(1, (len(level)-2))
			column = Random.randint(1, (len(level[0])-1))

			if level[row][column] == ".":
				level[row][column] = "X"
				placedItems += 1
			else:
				pass




	def getMap(self):
		return level

	def getPosX(self):
		for row in range(len(level[0])):
			for column in range(len(level)):
				if level[row][column] == PLAYER:
					return row
	def getPosY(self):
		for row in range(len(level[0])):
			for column in range(len(level)):
				if level[row][column] == PLAYER:
					return column
