import matplotlib.pyplot as plt
import csv
import pymysql as MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="Ajom", passwd="special313", db="mysql")
cursor = db.cursor()


plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）
print("123")
list=[]    #年
listhappen=[]   #發生件數[件]
listCarR=[]     #車輛肇事率[件/萬輛]
listCarC=[]     #肇事相關車輛數/汽車[輛]
listMotoC=[]     #肇事相關車輛數/機車[輛]
listOtherC=[]     #肇事相關車輛數/其他[輛]
listDeadC=[]     #死亡人數[人]
listHertC=[]     #受傷人數[人]



with open('ps00035mc.csv', 'r') as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)
    print(header)

    for row in read:

        list.append(row[0])
        listhappen.append(int(row[1].replace('-','0')))
        listCarR.append(float(row[2].replace('-','0')))
        listCarC.append(int(row[3].replace('-','0')))
        listMotoC.append(int(row[4].replace('-','0')))
        listOtherC.append(int(row[5].replace('-','0')))
        listDeadC.append(int(row[6].replace('-','0')))
        listHertC.append(int(row[7].replace('-','0')))


plt.subplot(4, 1, 1)
plt.plot(list, listhappen, 'r-', label="發生件數[件]")
plt.title('87~110年台北車禍數據')
labelListx=[]
for x in range(87,110):
    labelListx.append((str(x)+'年1月'))
plt.xticks(labelListx)
plt.grid()
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(list, listCarR, 'b-', label="車輛肇事率[件/萬輛]")
labelList=[]
for x in range(87,110):
    labelList.append((str(x)+'年1月'))
plt.xticks(labelList)
plt.grid()
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(list, listCarC, 'y-', label="肇事相關車輛數/汽車[輛]")
plt.plot(list, listMotoC, 'k-', label="肇事相關車輛數/機車[輛]")
plt.plot(list, listOtherC, 'g-', label="肇事相關車輛數/其他[輛]")
labelList=[]
for x in range(87,110):
    labelList.append((str(x)+'年1月'))
plt.xticks(labelList)
plt.yticks(range(0,31,3))
plt.grid()
plt.legend()
#死亡人數,受傷人數圖
plt.subplot(4, 1, 4)
plt.plot(list, listDeadC, 'c-', label="死亡人數[人]")
plt.plot(list, listHertC, 'm-', label="受傷人數[人]")

labelList=[]
for x in range(87,110):
    labelList.append((str(x)+'年1月'))
plt.xticks(labelList)
plt.yticks(range(0,31,3))
plt.grid()
plt.legend()
plt.show()