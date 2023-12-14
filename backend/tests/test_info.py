import os
import sys
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from app.main import app

client = TestClient(app)