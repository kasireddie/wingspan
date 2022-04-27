import json
from psycopg2 import connect, Error
from bottle import run, route, response, request, redirect

from scheduler import DBHOST

PORT = 5432
DBHOST = 'localhost'
DBNAME = 'wingspan'
DBUSER = 'wingspan'
PASSWORD = 'wingspanpass'

def dbcon():
    """ Connect to the PostgreSQL database

    return:
        con: If it exists return the database connection otherwise None
    """
    msg = ''
    con = None
    try:
        con = connect(host=DBHOST, user=DBUSER, dbname=DBNAME, 
                        password=PASSWORD, port=PORT)
    except Error as e:
        msg = e

    return con, msg


@route('/')
def birds():
    """ List of birds in the database
    """
    res = None
    con, msg = dbcon()

    if con is not None:
        try:
            birds = []
            cursor = con.cursor()
            sql = 'select bird_name, wingspan, food_name, habitat_name from bird ' 
            sql += 'join food on (bird.main_food_id = food.food_id) '
            sql += 'join habitat on (bird.main_habitat_id = habitat.habitat_id)'
            
            cursor.execute(sql)

            for row in cursor.fetchall():
                bird = dict()
                bird['name'] = row[0]
                bird['wingspan'] = f'{row[1]}cm'
                bird['food'] = row[2]
                bird['habitat'] = row[3]

                birds.append(bird)

            res = json.dumps({'birds': birds})

        except Error as e:
            res = json.dumps({'error': f'Error: {e}'})
        finally:
            # Close connection to database
            con.close()
    else:
        res = json.dumps({'error': f'Error: {msg}'})
    
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'

    return res

if __name__ == '__main__':
    run(host='localhost', port=5000)