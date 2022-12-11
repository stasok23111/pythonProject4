from flask import Flask, jsonify
from utils import get_one_query, get_result
import json

app = Flask(__name__)


@app.get('/movie/<title>')
def get_by_title(title):
    query = f""" 
        SELECT * FROM netflix 
        WHERE title = {title}
        ORDER BY date_added DESC
    """

    query_result = get_one_query(query)

    if query_result is None:
        return jsonify(status=404)

    movie = {
        "title": query_result['title'],
        "country": query_result['country'],
        "release_year": query_result['release_year'],
        "genre": query_result['listed_in'],
        "description": query_result['description'],
    }

    return jsonify(movie)


@app.get('/movie/<year1>/to/<year2>')
def get_movie_year(year1, year2):
    query = f"""
        SELECT * FROM NETFLIX
        WHERE release_year BETWEEN {year1} AND {year2}
        LIMIT 100
    """

    result = []
    for i in get_result(query):
        result.append(
            {
                'title': i['title'],
                'release_year': i['release_year'],
            }
        )
    return jsonify(result)


@app.get('/movie/rating/<value>')
def get_rating(value):
    query = """
            SELECT * FROM netflix
            """
    if value == 'children':
        query += "WHERE rating = 'G'"
    elif value == 'family':
        query += "WHERE  rating = 'G' or rating =  'PG' or rating =  'PG-13'"
    elif value == 'adult':
        query += "WHERE rating = 'R' or rating = 'NC-17'"
    else:
        return jsonify(status=404)

    result = []
    for i in get_result(query):
        result.append(
            {
                'title': i['title'],
                'rating': i['rating'],
                'description': i['description'],
            }
        )
    return jsonify(result)


@app.get('/genre/<genre>')
def get_by_genre(genre):
    query = f"""
            SELECT * FROM netflix
            WHERE listed_in LIKE %{genre}%
            ORDER BY date_added DESC
            LIMIT 10
            
    
    """
    result = []
    for i in get_result(query):
        result.append(
            {
                'title': i['title'],
                'description': i['description'],
            }
        )
    return jsonify(result)



if __name__ == '__main__':
    app.run()
