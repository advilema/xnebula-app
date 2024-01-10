import os


class Config:
    SECRET_KEY = 'ciao'
    DEBUG = False

    # Database Configurations
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # File Upload Configurations
    UPLOAD_FOLDER = 'static/images'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # Bulk Material Categories
    BULK_MATERIAL_CATEGORIES = [
        'Vertikalstiel',
        'Anfagsstiel',
    ]
