from flasgger import Flasgger

def configure(app):
    """Starts openapisec"""
    Flasgger(app)