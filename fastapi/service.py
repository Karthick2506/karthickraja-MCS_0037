from database import insert_player
from utils import database_retrieve


def service_insert(new_player, db):
    if new_player.jersey_no != 0:
        return insert_player(new_player, db)
    else:
        return "Failed to insert data"

def service_retrieve(db):
    return database_retrieve(db)
