from random import randint
def create_random_game_id(gameIds: []):
    uuid = 0
    for id in gameIds:
        uuid += id
    uuid += randint(0, 9)
    return uuid
