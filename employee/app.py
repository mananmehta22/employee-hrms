"""Employee Flask App."""
from flask import Flask

app = Flask(__name__)

from employee import handlers  # noqa
