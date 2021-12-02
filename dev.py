import os

from application import app

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(debug=True, port=port, threaded=True)