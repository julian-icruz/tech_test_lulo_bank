import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from app.load.domain.models import WebChannel, Network, Show, Episode
from app.db_connections.container import DBConnectionsContainer


def init_db():

    db_container = DBConnectionsContainer()
    db_container.init_resources()

    engine = db_container.postgres_connector().engine

    try:
        WebChannel.metadata.create_all(bind=engine)
        Network.metadata.create_all(bind=engine)
        Show.metadata.create_all(bind=engine)
        Episode.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error creating database tables: {e}")


if __name__ == "__main__":
    init_db()
