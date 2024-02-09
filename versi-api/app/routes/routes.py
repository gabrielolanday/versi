from flask import jsonify
from app.services.dashboard_service import DashboardService

def init_routes(app):
    @app.route('/')
    def home():
        result = DashboardService.get_book_ratings()
        return result