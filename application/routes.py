from flask import current_app as app
from flask_restx import Api, Namespace, Resource

from application import models, schema
from application.models import db

api: Api = app.config['api']
movies_ns: Namespace = api.namespace('movies')

movie_schema = schema.Movie()
movies_schema = schema.Movie(many=True)


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies = db.session.query(models.Movie).all()
        return movies_schema.dump(movies), 200


@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()
        if movie is None:
            return {}, 404
        return movie_schema.dump(movie), 200
