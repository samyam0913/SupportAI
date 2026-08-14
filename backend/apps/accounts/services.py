from .models import User

def register_user(*, email: str, password: str, full_name: str = "") -> User:
    """Create a new user with a correctly hashed password."""
    user = User(email=email.lower(), full_name=full_name)
    user.set_password(password)
    user.save()
    return user