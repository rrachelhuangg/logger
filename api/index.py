"""Vercel serverless entrypoint.

Vercel looks for a WSGI/ASGI callable named ``app`` in this module and routes
every request here (see the rewrite in ``vercel.json``).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app  # noqa: E402

app = create_app()
