import datetime

from app.database import db


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def to_dict(self):
        to_ret = self.__dict__.copy()
        if '_sa_instance_state' in to_ret:
            to_ret.pop('_sa_instance_state')
        return to_ret.items()

    def __repr__(self):
        return str(self.json())

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self.to_dict()
        }

    def save(self, commit=True):
        self.before_save()
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

        self.after_save()
