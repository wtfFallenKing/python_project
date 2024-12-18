from utils.parser_utils import get_cards_tierlist, get_card_info
from .connection_db import get_db_connection


def create_db():
  try:
    connection = get_db_connection()
    cursor = connection.cursor()

    CREATE_TABLE_CARDS = """
    CREATE TABLE IF NOT EXISTS cards (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        tier VARCHAR(255) NOT NULL,
        link VARCHAR(255),
        info VARCHAR(4096)
    );
    """

    cursor.execute(CREATE_TABLE_CARDS)
    
    connection.commit()
    
    cursor.close()
    connection.close()
    print("Database initialized successfully")

  except Exception as e:
    print(f"Error initializing database: {e}")



def clear_db():
  try:
    connection = get_db_connection()
    cursor = connection.cursor()
    
    CLEAR_DB = """
    DELETE FROM cards;
    """

    cursor.execute(CLEAR_DB)
    
    connection.commit()

    cursor.close()
    connection.close()
    print("Database cleared successfully")

  except Exception as e:
    print(f"Error clearing database: {e}")



def init_data_db():
  try:
    connection = get_db_connection()
    
    QUERY = """
    INSERT INTO cards (name, tier, link, info) 
    VALUES (%s, %s, %s, %s);
    """

    cursor = connection.cursor()

    data = get_cards_tierlist()

    for tier, cards in data.items():
      for card in cards:
        card_name = card["card_name"]
        card_link = card["card_link"]
        card_info = get_card_info(card_link)
        cursor.execute(QUERY, (card_name, tier, card_link, card_info))

    connection.commit()
    
    cursor.close()
    connection.close()
    print("Initial data inserted successfully")

  except Exception as e:
    print(f"Error inserting initial data into database: {e}")