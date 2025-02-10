import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

#print(doc.toprettyxml())

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
traincode = traincodenode.firstChild.nodeValue.strip()
print (traincode)

with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    dataList = []
    for retrieveTag in retrieveTags:
        datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
    dataList.append(datanode.firstChild.nodeValue.strip())
    train_writer.writerow(dataList)
traincode = traincodenode.firstChild.nodeValue.strip()

