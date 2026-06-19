from src.database.mysql_client import get_connection


def save_question_stat(question: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO question_stats (question, count)
        VALUES (%s, 1)
        ON DUPLICATE KEY UPDATE count = count + 1
    """, (question,))

    conn.commit()
    cur.close()
    conn.close()


def get_top_questions(limit=10):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT question, count
        FROM question_stats
        ORDER BY count DESC
        LIMIT %s
    """, (limit,))

    result = cur.fetchall()
    cur.close()
    conn.close()
    return result