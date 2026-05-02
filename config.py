import os
from tg_bot.sample_config import Config

class Development(Config):
    LOGGER = True

    # Pull these values from Railway's Environment Variables
    API_KEY = os.environ.get("TOKEN", "")
    
    # OWNER_ID is usually required as an integer
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    except ValueError:
        OWNER_ID = 0
        
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    
    # Fetch the Railway Database URL
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    
    # Crucial fix for Railway + SQLAlchemy:
    # Railway gives a URL starting with 'postgres://' but newer SQLAlchemy needs 'postgresql://'
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
        
    # Add any extra overrides here
    WEBHOOK = False
