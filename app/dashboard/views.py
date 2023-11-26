from flask import Blueprint, render_template, request, redirect

from app.models.width import tblwidth
from app.extensions import db

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard_blueprint.route('/')
def home():
    return render_template('dashboard.html')

@dashboard_blueprint.route('/user/<name>')
def create_tablewidth(name):
    width = tblwidth(name=name, isActive=True, comment='Added now')
    db.session.add(width)
    db.session.commit()
    return 'created width'