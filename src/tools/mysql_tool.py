from src.database.mysql_client import get_connection


def save_question(
    session_id,
    question,
    answer
):

    conn = get_connection()
    cur = conn.cursor()

    session_id = str(session_id)[:255]

    cur.execute(
        """
        INSERT INTO chat_history
        (
            session_id,
            question,
            answer
        )
        VALUES
        (
            %s,
            %s,
            %s
        )
        """,
        (
            session_id,
            question,
            answer
        )
    )

    conn.commit()

    cur.close()
    conn.close()