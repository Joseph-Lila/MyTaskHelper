from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    event,
    create_engine
)
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base
from allocation.domain import model

metadata = MetaData()

common_task = Table(
    "common_task",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(75), nullable=False),
    Column("deadline", DateTime, nullable=False),
    Column("period", Integer, nullable=False),
    Column("description", String(255), nullable=False),
    Column("status", String(25), nullable=False),
    Column("partition_title", String(75), nullable=True),
    Column("partition_count", Integer, nullable=True),
    Column("partition_progress", Integer, nullable=True),
)


def start_mappers():
    common_task_mapper = mapper(model.CommonTask, common_task)
    engine = create_engine('postgresql://loki:1111@localhost:5432/my_task_helper')
    metadata.create_all(engine)


start_mappers()
