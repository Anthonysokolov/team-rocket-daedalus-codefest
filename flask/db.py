import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'gym-app',
                        user = 'postgres', password = 'password')

cur = conn.cursor()

def add_visit(userid,gym,duration):
    query = "INSERT INTO visits VALUES ({}, '{}', {});".format(userid,gym,duration)
    cur.execute(query)

def make_user():
    query = "INSERT INTO users VALUES ('{}','{}',{});".format(name,passkey,userid)
    cur.execute(query)

def get_totals(userid):
    query = "SELECT SUM(duration) FROM visits WHERE (userid = {});".format(userid)
    cur.execute(query)
