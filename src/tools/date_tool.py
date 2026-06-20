from datetime import datetime


def get_date():

    now = datetime.now()

    return (
        f"Date: {now.strftime('%d-%m-%Y')}\n"
        f"Time: {now.strftime('%H:%M:%S')}"
    )