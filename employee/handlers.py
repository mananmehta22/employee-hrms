"""Handlers.

All the different endpoints are used to identify a user based on a
login and a password.
"""

from employee.app import app


@app.route('/hello')
def hello_world():
    return 'Hello World', 200


