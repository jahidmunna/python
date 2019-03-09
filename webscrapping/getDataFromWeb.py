import requests
import bs4
import csv

res = requests.get(
    'http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights#Data_Table')
soup = bs4.BeautifulSoup(res.text, 'lxml')
#select = soup.select('.wikitable')
table = soup.find("table", {"class": "wikitable"})
rows = table.findAll("tr")
name = []
team = []
postion = []
height = []
weight = []
age = []

for row in rows:
    cells = row.findAll("td")
    if(len(cells) != 0):
        name.append(str(cells[0].text))
        team.append(str(cells[1].text))
        postion.append(str(cells[2].text))
        height.append(str(cells[3].text))
        weight.append(str(cells[4].text))
        age.append(str(cells[5].text))


def nullChecker(listName):
    try:
        listName[listName.index('')] = listName[listName.index('')-1]
    finally:
        return listName


nullChecker(height)
nullChecker(weight)
nullChecker(age)

# height = list(map(int, height))
# weight = list(map(int, weight))
# age = list(map(float, age))
#print(name)
with open("G:/CodePracticing/pythonCode/DataResources/playerData(BaseBall).csv","w") as f:
    f.write("Name,Team,Position,Height,Weight,Age\n")
    for i in range(len(height)):
        f.write(name[i]+","+team[i]+","+postion[i]+","+height[i]+","+weight[i]+","+age[i])