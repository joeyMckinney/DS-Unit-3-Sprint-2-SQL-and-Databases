import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS = """
  SELECT COUNT(*)
  FROM CHARACTERCREATOR_character;
  """

mage = """
  SELECT COUNT(*)
  FROM charactercreator_mage;
"""
thief = """
  SELECT COUNT(*)
  FROM charactercreator_thief;
"""

cleric = """
  SELECT COUNT(*)
  FROM charactercreator_cleric;
"""

fighter = """
  SELECT COUNT(*)
  FROM charactercreator_fighter;
"""

necromancer = """
  SELECT COUNT(*)
  FROM charactercreator_necromancer;
"""

num_items = """
  SELECT COUNT(*)
  FROM armory_item;
"""

num_weapons = """
  SELECT COUNT(*)
  FROM armory_weapon;
"""

num_not_weapons = """
  SELECT COUNT(*) FROM armory_item
  LEFT JOIN armory_weapon
  ON item_ptr_id = item_id
  WHERE power IS NULL;
"""

char_items = """
  SELECT name, COUNT(*) FROM charactercreator_character
  INNER JOIN charactercreator_character_inventory
  GROUP BY name
  ORDER BY COUNT(*) DESC
  LIMIT 20;
"""
if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    results1 = execute_query(curs, GET_CHARACTERS)
    mages = execute_query(curs, mage)
    thiefs = execute_query(curs, thief)
    clerics = execute_query(curs, cleric)
    fighters = execute_query(curs, fighter)
    necromancers = execute_query(curs, necromancer)
    items = execute_query(curs, num_items)
    weapons = execute_query(curs, num_weapons)
    non_weapons = execute_query(curs, num_not_weapons)
    character_items = execute_query(curs, char_items)
    print(results1)
    print(mages, thiefs, clerics, fighters, necromancers)
    print(items)
    print(weapons, non_weapons)
    print(character_items)
