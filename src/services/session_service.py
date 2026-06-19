from src.database.mysql_client import get_connection


def get_history(session_id):

    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT
            question,
            answer,
            created_at
        FROM chat_history
        WHERE session_id=%s
        ORDER BY created_at ASC
        """,
        (session_id,)
    )

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data