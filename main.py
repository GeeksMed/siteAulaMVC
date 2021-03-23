from flask import Flask
import os

app = Flask(__name__, template+folder=os.path.abspath('application/viewqtemplates'), static_folder=os.path.abspath('application/view/static'))

