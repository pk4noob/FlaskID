from flask import Flask
from extensions.extensions import ma
from app.model import Movies
from marshmallow import validate,fields

class MoviesSchema(ma.SQLAlchemyAutoSchema):
    title = fields.String(required=True,validate=[validate.Length(min=2,max=20)])
    poster = fields.String(required=True,validate=[validate.Length(min=0,max=200)])
    year = fields.String(required=True,validate=[validate.Length(min=2,max=20)])
    imdbRating = fields.String(required=True,validate=[validate.Length(min=2,max=20)])
    director = fields.String(required=True,validate=[validate.Length(min=2,max=20)])
    runtime = fields.String(required=True,validate=[validate.Length(min=2,max=20)])


    class Meta:
        model = Movies
        load_instance = True

