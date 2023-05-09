#!/usr/bin/env python3
"""module creates a unique FileStorage instance for the
application
"""
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
