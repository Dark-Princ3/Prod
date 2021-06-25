""" init SQL """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from .. import DB_URI


def start() -> scoped_session:
    """ returns SQLAlchemy ScopedSession """
    if DB_URI.startswith("postgres://"):
        DB_URI.replace("postgres://", "postgresql://", 1)
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(
        sessionmaker(
            bind=engine,
            autoflush=False
        )
    )


BASE = declarative_base()
SESSION = start()
