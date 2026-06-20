from src.database.mysql_client import get_connection


def save_feedback(
    session_id,
    question,
    answer,
    rating,
    comment
):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO feedback
        (
            session_id,
            question,
            answer,
            rating,
            comment
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            session_id,
            question,
            answer,
            rating,
            comment
        )
    )

    conn.commit()

    cur.close()
    conn.close()


def get_feedback_summary():

    conn = get_connection()

    cur = conn.cursor(
        dictionary=True
    )

    cur.execute(
        """
        SELECT
            rating,
            COUNT(*) AS count
        FROM feedback
        GROUP BY rating
        """
    )

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data