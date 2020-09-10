from flask import Flask
from extensions.extensions import ma,db
from flask_apispec import MethodResource,marshal_with
# from app.seralize import MoviesSchema


class Movies(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(),nullable=False)
    poster = db.Column(db.String(),nullable=False)
    year = db.Column(db.Integer(),nullable=False)
    imdbRating = db.Column(db.String(),nullable=False)
    director = db.Column(db.String(),nullable=False)
    runtime = db.Column(db.String(),nullable=False)

    def savedb(self):
        db.session.add(self)
        db.session.commit()
    def deletedb(self):
        db.session.delete(self)
        db.session.commit()
    def updagte(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        self.savedb()


