from .. import db

class Sector(db.Model):
    """
    Type Sector Model
    """
    __tablename__ = 'sector'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sector = db.Column(db.String(5), unique=True, nullable=False)

    def __repr__(self):
        return '<id: typeunit: {}'.format(self.sector)
