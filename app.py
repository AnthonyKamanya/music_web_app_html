import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
# GET / a list of all the albums
# Returns a list of the albums
# Try it:
#   ; curl http://127.0.0.1:5001/albums

# @app.route('/hello', methods= ["GET"])
# def get_hello():
#     return render_template("hello.html", message="Hello, world!")

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums =repository.all()
    albums_strings = [f"{album}" for album in albums]
    return "\n".join(albums_strings)

# # GET /album/<id>
#     # Returns a single album
#     # Try it:
#     #   ; curl http://localhost:5001/album/1
@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository =AlbumRepository(connection)
    return str(repository.find(id))

# POST /albums
# # Creates a new album
# Try it:
#   ; curl -X POST -d  http://localhost:5001/albums

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repository.create(album)
    return "Album added successfully"      

# DELETE /albums
# Deletes an album
# Try it:
#   ; curl -X DELETE -d http://localhost:5001/albums

@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return "album deleted successfully"

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
