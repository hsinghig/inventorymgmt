from flask import Flask, render_template
from app.dashboard.views import dashboard_blueprint
from .extensions import db
from .constants import username, pwd, server, database
from sqlalchemy.ext.automap import automap_base

def create_app():
    app = Flask(__name__)
    conn = 'mssql+pyodbc://'+username+':' + pwd + '@'+ server + '/' + database + '?driver=ODBC+Driver+17+for+SQL+Server'
    print(conn)
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = conn
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)    
    #app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.errorhandler(404)  
    def page_not_found(e):
        return render_template("404.html"), 404
   
    return app


