"""
Pour démontrer l'utilisation des templates
"""

import random

from flask import Flask, render_template

from bd import creer_connexion

app = Flask(__name__)


@app.route('/')
def index():
    """Page d'index"""
    return render_template(
        'index.jinja', titre='Acceuil', message='Bienvenu sur la démo des templates!')




app.run()