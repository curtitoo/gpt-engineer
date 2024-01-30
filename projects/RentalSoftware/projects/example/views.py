from flask import Blueprint

# Define your blueprints here, for example:
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return "Welcome to the Car Rental Service!"

# Define other routes and views for your application

def register_blueprints(app):
    app.register_blueprint(main_bp)
    # Register other blueprints