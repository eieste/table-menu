from tm.config import settings


def default_text():
    return {
        "font": settings.get_font()
    }
