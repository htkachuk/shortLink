from app import db


class Urls(db.Model):

    __tablename__ = "url"

    id = db.Column('initiate_id', db.Integer,
                   primary_key=True, autoincrement=True)
    long_url = db.Column('long_url', db.String())
    short_url = db.Column('short_url', db.String())
    expiration = db.Column('expiration', db.Integer)

    def __init__(self, long_url, short_url, expiration):
        self.long_url = long_url
        self.short_url = short_url
        self.expiration = expiration

    def as_dict(self):
        obj = {}
        for column in self.__table__.columns:
            if column.name != "initiate_id":
                obj[column.name] = getattr(self, column.name)
        return obj



if __name__ == "__main__":
    db.create_all()
