import logging
from app import app

logger = logging.getLogger(__name__)

def test_health():

    logger.info("Starting health endpoint test")

    client = app.test_client()

    response = client.get("/health")

    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response JSON: {response.json}")

    assert response.status_code == 200
    assert response.json["status"] == "UP"

    logger.info("Health endpoint test completed")