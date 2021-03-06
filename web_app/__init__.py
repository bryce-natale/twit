from flask import Flask

from web_app.model import db, migrate

from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

DATABASE_URI = "sqlite:///twitoff_18_dev.db"

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app



if __name__ == "__main__":
    my_app = create_app() 
    my_app.run(debug=True) 