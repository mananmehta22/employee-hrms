"""Auth Application.

The auth application is responsible for providing the different endpoints
that allows a user to log in and other applications to verify the validity
of a token.
"""

from flask import Flask



app = Flask(__name__)

