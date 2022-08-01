import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
            host='localhost',
            database='flask_db',
            user='admin',
            password='admin')
    cur = connection.cursor()
    return connection, cur

def close_db_connection(connection):
    connection.commit()
    connection.close()

def to_str(xs):
    return '\n'.join([x[1] for x in xs])

def get_seeds(topic_id):
    conn, cur = get_db_connection()
    cur.execute('SELECT * FROM seed_papers WHERE topic_id=%s', (topic_id,))
    seeds = cur.fetchall()
    close_db_connection(conn)
    return seeds
    
def get_keywords(topic_id):
    conn, cur = get_db_connection()
    cur.execute('SELECT * FROM keywords WHERE topic_id=%s', (topic_id,))
    keywords = cur.fetchall()
    close_db_connection(conn)
    return keywords

def insert_keywords(topic_id, keywords):
    conn, cur = get_db_connection()
    for keyword in keywords:
        cur.execute('INSERT INTO keywords (keyword, topic_id) VALUES (%s, %s)',
                (keyword, topic_id))
    close_db_connection(conn)

def delete_keywords(topic_id):
    conn, cur = get_db_connection()
    cur.execute('DELETE FROM keywords WHERE topic_id=%s', (topic_id,))
    close_db_connection(conn)

def delete_topic(topic_id):
    conn, cur = get_db_connection()
    cur.execute('DELETE FROM seed_papers WHERE topic_id=%s', (topic_id,))
    cur.execute('DELETE FROM keywords WHERE topic_id=%s', (topic_id,))
    cur.execute('DELETE FROM topics WHERE topic_id = %s', (topic_id,))
    close_db_connection(conn)

def create_topic(title, seed_papers, keywords):
    conn, cur = get_db_connection()
    cur.execute('INSERT INTO topics (title) VALUES (%s) RETURNING topic_id',
                 (title,))
                 
    topic_id = cur.fetchone()[0]
    for seed in seed_papers:
        cur.execute('INSERT INTO seed_papers (paper_id, topic_id) VALUES (%s, %s)',
                (seed, topic_id))
    for keyword in keywords:
        cur.execute('INSERT INTO keywords (keyword, topic_id) VALUES (%s, %s)',
                (keyword, topic_id))
    
    close_db_connection(conn)                
    return topic_id

def update_topic(topic_id, title, seed_papers, keywords):
    conn, cur = get_db_connection()
    cur.execute('UPDATE topics SET title=%s where topic_id=%s',
                 (title,topic_id))
    cur.execute('DELETE FROM seed_papers WHERE topic_id=%s', (topic_id,))
    cur.execute('DELETE FROM keywords WHERE topic_id=%s', (topic_id,))
    for seed in seed_papers:
        cur.execute('INSERT INTO seed_papers (paper_id, topic_id) VALUES (%s, %s)',
                (seed, topic_id))
    for keyword in keywords:
        cur.execute('INSERT INTO keywords (keyword, topic_id) VALUES (%s, %s)',
                (keyword, topic_id))
    
    close_db_connection(conn)                
    return topic_id

def get_topic(topic_id):
    conn, cur = get_db_connection()
    if topic_id < 0:
        cur.execute('SELECT * FROM topics')
        topic = cur.fetchall()
    else:
        cur.execute('SELECT * FROM topics WHERE topic_id = %s',
                (topic_id,))
        topic = cur.fetchone()
    
    close_db_connection(conn)
    return topic

