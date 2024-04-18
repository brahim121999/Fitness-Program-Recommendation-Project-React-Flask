# app/views.py

from flask import render_template
from flask import Blueprint

user_interface = Blueprint('user_interface', __name__)

@user_interface.route('/user-interface', methods=['GET'])
def user_interface_route():
    return render_template('index.html')
