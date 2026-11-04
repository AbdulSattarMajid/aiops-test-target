"""Sample payment-service config loader with a deliberate bug."""
import os


def load_config():
    key = os.environ.get("STRIPE_API_KEY")
    if key is None:
        raise RuntimeError("Missing required environment variable: STRIPE_API_KEY")
    return {"stripe_key": key}
