"""Dev File For Application."""
from application import app

if __name__ == '__main__':
    app.run(debug=True, port=8080, threaded=True)
