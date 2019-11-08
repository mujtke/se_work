from model import *



#从文件中读取路径的数据，并存储在列表中返回	
def LoadPath(pathFile):
	pass
	return loadPath
	
#path中的元素为格子在地图中所处的位置，均为整型数
path += LoadPath(pathFile)	
	
def MoveAlongPath(attacker,path,blockSize):	#分别为具体的攻击者类型和路径信息，以及格子尺寸
#初始位置的初始化，以像素为单位
	attacker.position[0] = (path[0][0] + 0.5)*blockSize
	attacker.position[1] = (path[0][1] + 0.5)*blockSize
	
#计算路径上的格子数
	pathLength = len(path)		#路径上的总格子数
	presentBlock = 0			#当前攻击者所处的格子
	nextBlock = 1				#攻击者按照路径需要移动到的一下个格子
	
#开始进行路径移动并刷新攻击者位置
	while nextBlock <= pathLength:
	#计算移动方向
		x = path[nextBlock][0] - path[presentBlock][0]
		y = path[nextBlock][1] - path[presentBlock][1]
		if(x == 0):
			if(y == 1): attacker.direction = 2  #down
			else: 		attacker.direction = 0  #update
		if(y == 0):
			if(x == -1): attacker.direction = 1 #left
			else:		 attacker.direction = 3 #right
	#暂存移动前的位置	
		beforeMove = (attacker.position[0],attacker.position[1])	
	#向一个方向移动，对于障碍物没有处理，因此attackers.position不一定是正确的位置
		attack.move()
	#计算移动长度，像素为单位
		moveLen = attacker.position[0] - beforeMove[0] + attacker.position[1] - beforeMove[1]	
		if(moveLen < 0): moveLen = -moveLen
	#更正攻击者移动后的位置和所处的格子
		path = path[presentBlock:]	#从当前格子开始之后的所有格子组成剩余路径
		tmp = ()
		tmp += MoveCorrect(path,moveLen,beforeMove,presentBlock,blockSize)
		attacker.position[0] = tmp[0][0]
		attacker.position[1] = tmp[0][1]
		presentBlock = tmp[1]
		nextBlock = presentBlock + 1

#计算攻击者移动后的正确位置，并返回（最终坐标，presentBlock）的元组
def moveCorrect(path,moveLen,beforeMove,presentBlock,blockSize):
	xPos = 0
	yPos = 0	#记录最终坐标的横纵坐标
	#如果当前Block是路径中最后一个Block，则将攻击者的最终位置设置为Block中央
	if(len(path) == 1):
		xPos = (path[0][0] + 0.5)*blockSize
		yPos = (path[0][1] + 0.5)*blockSize
		return((xPos,yPos),presentBlock)
	L = (path[1][0] + 0.5)*blockSize - beforeMove[0] + (path[1][1] + 0.5)*blockSize - beforeMove[1]
	if(L < 0): L = -LoadPath
	#如果攻击者前进一次后尚未运动到下一个Block
	if(length <= (L - 0.5*blockSize)):
		x = path[1][0] - path[0][0]
		y = path[1][1] - path[0][1]
		if(x == 0): 
			yPos = beforeMove[1] + L*y
			xPos = beforeMove[0]
		if(y == 0): 
			xPos = beforeMove[0] + L*x
			yPos = beforeMove[1]
		return((xPos,yPos),presentBlock)
	#如果运动结束后位于下一个Block
	if(length > (L - 0.5*blockSize) and length <= (L - 0.5*blockSize)):
		x = path[1][0] - path[0][0]
		y = path[1][1] - path[0][1]
		if(x == 0): 
			yPos = beforeMove[1] + L*y
			xPos = beforeMove[0]
		if(y == 0): 
			xPos = beforeMove[0] + L*x
			yPos = beforeMove[1]
		return((xPos,yPos),presentBlock + 1)
	#如果运动后的位置已经超出了下一个Block，则通过递归的方式进行计算
	if(length > (L + 0.5*blockSize)):
		beforeMove[0] = (path[1][0] + 0.5)*blockSize
		beforeMove[1] = (path[1][1] + 0.5)*blockSize
		xPos = MoveCorrect(path[1:],length - L,beforeMove,presentBlock + 1,blockSize)[0][0]
		yPos = MoveCorrect(path[1:],length - L,beforeMove,presentBlock + 1,blockSize)[0][1]
		presentBlock = MoveCorrect(path[1:],length - L,beforeMove,presentBlock + 1,blockSize)[1]
		return((xPos,yPos),presentBlock)
		
		
	
	
