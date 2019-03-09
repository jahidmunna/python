# Import pandas as pd
import pandas as pd

# Import the playerData(BaseBall).csv data: players_info
players_info = pd.read_csv("G:/CodePracticing/pythonCode/DataResources/playerData(BaseBall).csv")
# OR to avoid import the row labels as another column without a name.
# players_info = pd.read_csv("G:/CodePracticing/pythonCode/DataResources/playerData(BaseBall).csv", index_col=0)

# Print out players_info
print(players_info)

# Printing particular name
index_of_desire_parson = 10
print(players_info['Name'][index_of_desire_parson])
