import os
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from app import create_app

# Create the Flask app
app = create_app()

# Export the app for Vercel
handler = app
