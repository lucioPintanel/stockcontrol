from flask import Flask
import os, config

# application factory
def create_app(config):
    # create application instance
    app = Flask(__name__)
    app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    
    from api.resources.fornecedor import fornecedor_bp
    from api.resources.product import product_bp
    from api.resources.user import user_bp
    from api.resources.control import movement_bp
    
    app.register_blueprint(fornecedor_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(movement_bp)
    
    return app
