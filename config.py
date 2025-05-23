import os
from dotenv import load_dotenv
from supabase import create_client

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # Flask Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback-secret-key'
    UPLOAD_FOLDER = 'app/static/uploads'
    
    # Database Configuration
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST', 'db.krxhfokngnugmuvnqcgl.supabase.co')
    DB_PORT = os.environ.get('DB_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'postgres')
    
    # Construct SQLAlchemy URI
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Supabase Configuration
    SUPABASE_URL = os.environ.get('SUPABASE_URL')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
    MAX_IMAGE_SIZE = 50 * 1024 * 1024  # 50MB
    # Supabase Storage Bucket for car images
    SUPABASE_STORAGE_BUCKET = os.environ.get('SUPABASE_STORAGE_BUCKET', 'car-images')
    
    # M-Pesa API Configuration
    MPESA_CONSUMER_KEY = os.environ.get('MPESA_CONSUMER_KEY')
    MPESA_CONSUMER_SECRET = os.environ.get('MPESA_CONSUMER_SECRET')
    MPESA_BUSINESS_SHORTCODE = os.environ.get('MPESA_BUSINESS_SHORTCODE', '174379')  # Default is sandbox value
    MPESA_PASSKEY = os.environ.get('MPESA_PASSKEY')
    MPESA_CALLBACK_URL = os.environ.get('MPESA_CALLBACK_URL')
    
    SITE_URL = os.environ.get('SITE_URL', 'http://localhost:5000')  # Default for local testing
    
    # Other config settings...
    
    @classmethod
    def init_supabase(cls):
        if cls.SUPABASE_URL and cls.SUPABASE_KEY:
            return create_client(cls.SUPABASE_URL, cls.SUPABASE_KEY)
        return None