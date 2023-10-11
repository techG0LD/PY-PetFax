from flask import (Blueprint, render_template)
import json

bp = Blueprint('pet',__name__, url_prefix = '/pets')

pets = json.load(open('pets.json', encoding='utf8'))
print(pets)

@bp.route('/')
def index():
    return render_template('pets/index.html',pets = pets)
    # return "This is the pet faxing center. We can fax your pitbull"

@bp.route('/<int:id>')
def show(id):
    pet = pets[ id- 1]
    return render_template('pets/show.html',pet =pet)