
#这是从文件中加载关卡信息

#加载关卡i的数据(int值)，从文件读取到一个列表中
from map import Map

def dataLoad(i):
	level = "level" + str(i) + ".txt"
	fileP = open(level,mode = 'r')
	fileData = []
	while (1):
		a = fileP.read(1)
		if a == "":
			break
		if a == "\n" or a == "\r":
			continue
		fileData.append(int(a))
	fileP.close()
	levelData = fileData
	return levelData

#利用关卡的数据完成地图的初始化
def levelLoad(map,i):
	levelData = dataLoad(i)
	m = map.columnNumber
	n = map.rowNumber
	for i in range(m):
		for j in range(n):
			k = levelData[i*n + j]
			#如果为家，对应于数字4
			if k == 4:
				map.setHome(i,j)
			#如果为出生点，对应于数字5
			elif k == 5:
				map.setBornPoint(i,j)
			else:
				map.setSomeBlock(i,j,k)
			
a_map=Map()
levelLoad(a_map,1)

for i in range(a_map.columnNumber):
    for j in range(a_map.rowNumber):
        print (3-a_map.maps[i][j].canPlantOn-2*a_map.maps[i][j].canZombieOn,end='')
    print("\n")
