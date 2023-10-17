from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

# """
# GET /books
# Returns a list of books
# """
# def test_get_books(web_client, db_connection):
#   db_connection.seed('seeds./book_store.sql')
#   response =web_client.get('/books')
#   assert response.status_code == 200
#   assert response.data.decode("utf-8") == "\n".join([
#         "Book(1, Invisible Cities, Italo Calvino)",
#         "Book(2, The Man Who Was Thursday, GK Chesterton)",
#         "Book(3, Bluets, Maggie Nelson)",
#         "Book(4, No Place on Earth, Christa Wolf)",
#         "Book(5, Nevada, Imogen Binnie)"
#     ])

# === End Example Code ===

"""
GET /albums
"""


# Note web_client fixture, see conftest.py
def test_get_albums(web_client, db_connection):
    # We seed our database with the music_web_app seed file
    db_connection.seed("seeds/music_web_app.sql")

    # We make a GET request to /albums
    response = web_client.get("/albums")

    # We assert that the response status code is 200
    assert response.status_code == 200

    # We assert that the response data is the same as the string we expect
    assert response.data.decode("utf-8") == "\n".join([
        "Album(1, Doolittle, 1989, 1)\n" +
        "Album(2, Surfer Rosa, 1988, 1)\n" +
        "Album(3, Waterloo, 1974, 2)\n" +
        "Album(4, Super Trouper, 1980, 2)\n" +
        "Album(5, Bossanova, 1990, 1)\n" +
        "Album(6, Lover, 2019, 3)\n" +
        "Album(7, Folklore, 2020, 3)\n" +
        "Album(8, I Put a Spell on You, 1965, 4)\n" +
        "Album(9, Baltimore, 1978, 4)\n" +
        "Album(10, Here Comes the Sun, 1971, 4)\n" +
        "Album(11, Fodder on My Wings, 1982, 4)\n" +
        "Album(12, Ring Ring, 1973, 2)"
    ])


"""
GET /albums/<id>
"""


def test_find_album(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")

    response = web_client.get("/albums/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)"


# """
# POST /albums
# """


def test_create_album(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")

    response = web_client.post("/albums", data={
        "title": "Voyage",
        "release_year": 2022,
        "artist_id": 2
    })

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album added successfully"

    response = web_client.get("/albums")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Album(1, Doolittle, 1989, 1)\n" +
        "Album(2, Surfer Rosa, 1988, 1)\n" +
        "Album(3, Waterloo, 1974, 2)\n" +
        "Album(4, Super Trouper, 1980, 2)\n" +
        "Album(5, Bossanova, 1990, 1)\n" +
        "Album(6, Lover, 2019, 3)\n" +
        "Album(7, Folklore, 2020, 3)\n" +
        "Album(8, I Put a Spell on You, 1965, 4)\n" +
        "Album(9, Baltimore, 1978, 4)\n" +
        "Album(10, Here Comes the Sun, 1971, 4)\n" +
        "Album(11, Fodder on My Wings, 1982, 4)\n" +
        "Album(12, Ring Ring, 1973, 2)\n" +
        "Album(13, Voyage, 2022, 2)"
    ])


# """
# # # DELETE /albums/<id>
# # # """


def test_delete_album(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")

    response = web_client.delete("/albums/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "album deleted successfully"

    response = web_client.get("/albums")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Album(2, Surfer Rosa, 1988, 1)\n" +
        "Album(3, Waterloo, 1974, 2)\n" +
        "Album(4, Super Trouper, 1980, 2)\n" +
        "Album(5, Bossanova, 1990, 1)\n" +
        "Album(6, Lover, 2019, 3)\n" +
        "Album(7, Folklore, 2020, 3)\n" +
        "Album(8, I Put a Spell on You, 1965, 4)\n" +
        "Album(9, Baltimore, 1978, 4)\n" +
        "Album(10, Here Comes the Sun, 1971, 4)\n" +
        "Album(11, Fodder on My Wings, 1982, 4)\n" +
        "Album(12, Ring Ring, 1973, 2)"
    ])
