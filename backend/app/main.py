"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd


app = FastAPI()


