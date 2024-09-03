from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Add this line

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'complete': self.complete,
            'user_id': self.user_id
        }