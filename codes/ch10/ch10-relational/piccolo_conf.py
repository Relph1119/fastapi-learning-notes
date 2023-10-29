from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "pccs",
        "user": "postgres",
        "password": "root",
        "host": "localhost",
        "port": 5432,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["survey.piccolo_app", "piccolo_admin.piccolo_app"]
)
