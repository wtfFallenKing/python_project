import flask
from utils.parser_utils import get_cards_tierlist
from .connection_db import get_db_connection


def main_route(): # route "/"
  try:
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cards")
    ans = cursor.fetchone()

    cursor.close()
    connection.close()

    if ans:
      return flask.jsonify(get_cards_tierlist())
    else:
      return flask.jsonify({ "Cards": "No cards found" })
    
  except Exception as e:
    return flask.jsonify({ "error": str(e) }), 500
  

def card_route(card_name):
  try:
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cards WHERE link = %s", (card_name,))
    response = cursor.fetchone()

    cursor.close()
    connection.close()

    if response:
      return flask.jsonify(response)
    else:
      return flask.jsonify({ card_name: "No card found" })

  except Exception as e:
    return flask.jsonify({ "error": str(e) }, 500)
  
def deck_route():
  try:
    connection = get_db_connection()
    cursor = connection.cursor()

    QUERY = """
    SELECT id, name, tier, link, info
    FROM cards
    ORDER BY RANDOM()
    LIMIT 8;"""

    cursor.execute(QUERY)
    random_cards = cursor.fetchall()

    deck = [
      {
        "id": card[0],
        "name": card[1],
        "tier": card[2],
        "link": card[3],
        "info": card[4]
      }
      for card in random_cards
    ]

    cursor.close()
    connection.close()

    return flask.jsonify(deck)

  except Exception as e:
    return flask.jsonify({ "error": str(e) }), 500