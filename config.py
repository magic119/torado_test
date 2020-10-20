import os
BASE_DIR = os.path.dirname(__file__)
UP_FILE_PATH = os.path.join(BASE_DIR, "upfiles")

settings = {
    "debug": True,
    "template_path": os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(BASE_DIR, "static"),
    "static_hash_cache": False,
}