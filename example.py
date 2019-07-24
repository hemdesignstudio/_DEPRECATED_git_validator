from datetime import datetime

now = datetime.now()


def get_month():
    mm = str(now.month)
    return mm


def get_day():
    dd = str(now.day)
    return dd


def get_year():
    yyyy = str(now.year)
    return yyyy


def get_hour():
    hour = str(now.hour)
    return hour


def get_minute():
    mi = str(now.minute)
    return mi


def get_second():
    ss = str(now.second)
    return ss


if __name__ == "__main__":
    print(
        get_month()
        + "/"
        + get_day()
        + "/"
        + get_year()
        + " "
        + get_hour()
        + ":"
        + get_minute()
        + ":"
        + get_second()
    )
