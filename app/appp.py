from flask import Flask,request,jsonify,Response
from app.model import Movies
from app.seralize import MoviesSchema
from app_init.app_factory import createAp
import requests
import os
from http import HTTPStatus
from marshmallow import ValidationError
from webargs import fields
from flask_apispec import use_kwargs, marshal_with,FlaskApiSpec,MethodResource
# from flask_json import FlaskJSON,as_json


settings_name = os.getenv("settings")
app = createAp(settings_name)





@app.route('/movies')
@use_kwargs({'title': fields.Str(),"poster":fields.Str(),"year":fields.Int(),"imdbRating":fields.Str(),"director":fields.Str(),"runtime":fields.Str()})
@marshal_with(MoviesSchema(many=True))
def list_pets(**kwargs):
    return Movies.query.filter_by(**kwargs).all()


@marshal_with(MoviesSchema)
class StoreResource(MethodResource):

    def get(self,movie_id):
        return Movies.query.filter_by(id=movie_id).one()
    @use_kwargs(MoviesSchema)
    def put(self, movie_id,**kwargs):
        movie = Movies.query.filter_by(id=movie_id).one()
        movie.updagte()
        return movie


@use_kwargs({"id":fields.Int()})
# @as_json
class DeleteMovies(MethodResource):
    # @marshal_with(MoviesSchema(many=True))
    def delete(self,movie_id,**kwargs):
        movie = Movies.query.filter_by(id=movie_id).first()
        if movie:
            movie.deletedb()
            # return {"result":"True"}
            return Response("Delete olundu",content_type='application/json',status=True)
        return {"result":"False"}
docs = FlaskApiSpec(app)
docs.register(list_pets)
app.add_url_rule('/movies', view_func=StoreResource.as_view('Movie'))
docs.register(StoreResource,endpoint="Movie")
app.add_url_rule("/movies/<int:movie_id>",view_func=DeleteMovies.as_view("movie"))
docs.register(DeleteMovies,endpoint="movie")


@app.route("/movies", methods=["POST"])
def createPost():
    data = request.get_json()
    try:
        x = MoviesSchema().load(data)
        x.savedb()
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    return MoviesSchema().jsonify(x), HTTPStatus.OK



# @app.route("/movies",methods=["GET"])
# def GetMovies():
#     data = Movies.query.filter_by(title = request.get_json().get("title")).all()
    
#     print(data)
#     if data:
#         responsee = MoviesSchema().dump(data,many=True)
        
#         return MoviesSchema().jsonify(responsee,many=True),HTTPStatus.OK
#     return jsonify(msg="Erro file"),HTTPStatus.NOT_FOUND


@app.route("/moviess",methods=["GET"])
def GetMoviess():
    dataTitle = Movies.query.filter_by(title = request.get_json().get("title")).all()
    if dataTitle:
        dataSchema = MoviesSchema().dump(dataTitle,many=True) 
        return MoviesSchema().jsonify(dataSchema,many=True),HTTPStatus.OK    

    dataDirector = Movies.query.filter_by(director = request.get_json().get("director")).all()
    if dataDirector:
        dataSchema = MoviesSchema().dump(dataDirector,many=True)
        return MoviesSchema().jsonify(dataSchema,many=True),HTTPStatus.OK    

    dataYear = Movies.query.filter_by(year = request.get_json().get("year")).all()
    print(dataYear)
    if dataYear:
        dataSchema = MoviesSchema().dump(dataYear,many=True)
        return MoviesSchema().jsonify(dataYear,many=True),HTTPStatus.OK    


    return jsonify(msg="Error"),HTTPStatus.BAD_REQUEST


    # if data:
    #     responsee = MoviesSchema().dump(data,many=True)

    #     return MoviesSchema().jsonify(responsee,many=True),HTTPStatus.OK
    # return jsonify(msg="Erro file"),HTTPStatus.NOT_FOUND


@app.route("/movies",methods=["GET"])
def GetMovies():
    data = Movies.query.all()
    return MoviesSchema().jsonify(data,many=True),HTTPStatus.OK













# @app.route("/movies",methods=["GET"])
# def GetMovies():
#     if request.args.get("years"):
#         if request.args.get("test"):
#             if request.args.get("splot") == "full" or request.args.get("splot") =="short":
#                 response = requests.get(f"https://www.omdbapi.com/", params={"t":request.args.get("test"),"plot":request.args.get("splot"),"y":request.args.get("years"),"apikey":"trilogy"})
#                 if response.status_code == 200:
#                     return jsonify(response.json())
#             return jsonify(msg = "No splot")
#         return jsonify(msg="test yoxdur")
#     return jsonify(msg="Il yoxdur")
    
