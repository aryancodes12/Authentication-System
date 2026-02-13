_current_user = None

def start_session(user):
    global _current_user
    _current_user = user


def end_session():
    global _current_user
    _current_user = None


def is_logged_in():
    return _current_user is not None


def get_current_user():
    return _current_user