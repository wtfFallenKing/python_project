import requests
import bs4


def get_cards_tierlist() -> dict:

  base_tierlist_url = "https://www.noff.gg/clash-royale/tier-list"
  base_request = requests.get(base_tierlist_url)
  soup = bs4.BeautifulSoup(base_request.content, "html.parser")


  tiers = soup.find("div", id="tierList").find_all("div", class_="tier")
  tierlist = {}


  for tier_it in tiers:
    tier = tier_it["class"][1]
    cards = tier_it.find_all("div", class_="cards")
    current_data = []
    
    
    for card in cards:
      card_data = card.find_all("a")

      for card_names in card_data:
        current_object = {}
        name = card_names.find("img")["alt"]
        link = "-".join(name.lower().split(" ")) if " " in name.lower() else name.lower()
        current_object["card_name"] = name
        current_object["card_link"] = link
        current_data.append(current_object)

    tierlist[tier] = current_data
  
  return tierlist


def get_card_info(url):
  base_card_url = f"https://www.noff.gg/clash-royale/card/{url}"
  card_info_request = requests.get(base_card_url)
  soup = bs4.BeautifulSoup(card_info_request.content, "html.parser")

  info = soup.find("div", class_="page-description").find("p").text.strip()

  return str(info)