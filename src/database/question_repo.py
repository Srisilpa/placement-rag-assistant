from src.database.mysql_client import get_connection

def update_stats(question):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO question_stats(question, count)
        VALUES (%s, 1)
        ON DUPLICATE KEY UPDATE count = count + 1
    """, (question,))

    conn.commit()