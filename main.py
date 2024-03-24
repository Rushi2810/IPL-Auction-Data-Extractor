import pandas as pd
from bs4 import BeautifulSoup
import requests

def extract_team_info(url):
  """
  Extracts team information from the IPL auction website, focusing on Oversea Players.

  Args:
      url: The URL of the IPL auction webpage.

  Returns:
      A list of dictionaries containing team information, including "Oversea Player".
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "lxml")

  teams = []
  # Loop through team names and fund details
  for team_name, fund_details, total_player_element in zip(soup.find_all("div", class_="agv-team-name"),
                                     soup.find_all("div", class_="avg-fund-remaining"),
                                     soup.find_all("li",class_="m-0 px-1")):
    # Find oversea player element using text content filter (assuming case-insensitive)
    oversea_player_element = soup.find("li", class_="m-0")
    # Create team info dictionary with only relevant data
    teams_info = {
        "Team Name": team_name.text.strip(),
        "Team Budget": fund_details.text.strip(),
        "Oversea Player": oversea_player_element.text.strip(),
        "Total Player": total_player_element.text.strip()
    }
    teams.append(teams_info)
  return teams

# Get team information
teams_data = extract_team_info("https://www.iplt20.com/auction")  

# Create and save DataFrame
df = pd.DataFrame(teams_data)
df.to_excel("Auction_Info.xlsx", index=False)
print("Auction information saved to Auction_Info.xlsx")
