""" Module core.service_layer.services """
from core.domain.models.common_task import CommonTask
from core.service_layer.unit_of_work.abstract_unit_of_work import \
    AbstractUnitOfWork


def distribute_statuses(uow: AbstractUnitOfWork):
    """ Method to distribute statuses """
    with uow:
        common_tasks = uow.common_tasks.list()
        CommonTask.distribute_statuses(common_tasks)
        uow.commit()
