from src.layers.domain.models.common_task import CommonTask
from src.layers.service_layer.unit_of_work.abstract_unit_of_work import AbstractUnitOfWork


def distribute_statuses(uow: AbstractUnitOfWork):
    with uow:
        common_tasks = uow.common_tasks.list()
        CommonTask.distribute_statuses(common_tasks)
        uow.commit()
