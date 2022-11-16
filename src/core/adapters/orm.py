""" Module core.adapters.orm """
from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, MetaData,
                        String, Table)
from sqlalchemy.orm import mapper, relationship

from core.domain.models.common_task import CommonTask
from core.domain.models.registrator import Registrator
from core.domain.models.registrator_item import RegistratorItem
from core.domain.models.special_task import SpecialTask

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
    Column("eta", Integer, nullable=False),
    Column("partition_title", String(75), nullable=True),
    Column("partition_count", Integer, nullable=True),
    Column("partition_progress", Integer, nullable=True),
)

special_task = Table(
    "special_task",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(75), nullable=False),
    Column("deadline", DateTime, nullable=False),
    Column("period", Integer, nullable=False),
    Column("description", String(255), nullable=False),
    Column("status", String(25), nullable=False),
)

registrator = Table(
    "registrator",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(75), nullable=False),
    Column("description", String(255), nullable=False),
)

registrator_item = Table(
    "registrator_item",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("registrator_id", Integer, ForeignKey("registrator.id")),
    Column("what", String(75), nullable=False),
    Column("how_much", Float, nullable=False),
    Column("when", DateTime, nullable=False),
)


def start_mappers():
    common_task_mapper = mapper(CommonTask, common_task)
    special_task_mapper = mapper(SpecialTask, special_task)
    registrator_mapper = mapper(
        Registrator, registrator,
        properties={
            "items": relationship(RegistratorItem, backref="registrator", order_by=registrator_item.c.when)
        }
    )
    registrator_item_mapper = mapper(RegistratorItem, registrator_item)
