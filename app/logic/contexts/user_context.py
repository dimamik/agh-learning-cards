from app import User
from app.database.session import Session
from app.logic.contexts.base_context import BaseContext


class UserContext(BaseContext):
    """
    Class wrapping User Instance
    """

    def __init__(self, user: User):
        super(UserContext, self).__init__()
        self.instance = user

    def set_username(self, username: str):
        self.instance.userName = username
        Session.commit()

    def set_user_info(self, info: str):
        self.instance.userInfo = info
        Session.commit()

    def set_password_hash(self, new_password_hash: str):
        self.instance.userPasswordHash = new_password_hash
        Session.commit()

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def is_active(self) -> bool:
        return True

    @property
    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        return self.instance.userEmail

    @staticmethod
    def exists_by_username(user_name: str) -> bool:
        return Session.query(User).filter(User.userName == user_name).first() is not None

    @staticmethod
    def exists_by_email(email: str) -> bool:
        return Session.query(User).filter(User.userEmail == email).first() is not None

    @staticmethod
    def get_user_instance_by_id(uid: int):
        user = Session.query(User).filter(User.userID == uid).first()
        return UserContext(user) if user else None

    @staticmethod
    def get_user_instance_by_username(username: str):
        user = Session.query(User).filter(User.userName == username).first()
        return UserContext(user) if user else None

    @staticmethod
    def get_user_instance_by_email(email: str):
        user = Session.query(User).filter(User.userEmail == email).first()
        return UserContext(user) if user else None

    @staticmethod
    def add_new_user(username: str, email: str, password_hash: str):
        user = User()
        user.userName = username
        user.userEmail = email
        user.userPasswordHash = password_hash

        Session.add_and_commit(user)
        user_context = UserContext(user)

        return user_context
