from src.database.mysql_client import get_connection


def save_question_stat(question):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO question_stats
        (
            question,
            count
        )
        VALUES
        (
            %s,
            1
        )
        ON DUPLICATE KEY UPDATE
            count = count + 1,
            last_asked = NOW()
        """,
        (question,)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_top_questions(limit=5):

    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT question,count
        FROM question_stats
        ORDER BY count DESC
        LIMIT %s
        """,
        (limit,)
    )

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


def get_recent_questions(
    session_id,
    limit=10
):

    conn = get_connection()

    cur = conn.cursor(
        dictionary=True
    )

    cur.execute(
        """
        SELECT
            question,
            MAX(answer) AS answer,
            MAX(created_at) AS created_at
        FROM chat_history
        WHERE session_id=%s
        GROUP BY question
        ORDER BY MAX(created_at) DESC
        LIMIT %s
        """,
        (
            session_id,
            limit
        )
    )

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


def get_total_questions():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT COUNT(*)
        FROM chat_history
        """
    )

    total = cur.fetchone()[0]

    cur.close()
    conn.close()

    return total


def clear_session_history(session_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM chat_history
        WHERE session_id=%s
        """,
        (session_id,)
    )

    conn.commit()

    cur.close()
    conn.close()