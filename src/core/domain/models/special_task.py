""" Module core.domain.models.special_task """
from dataclasses import dataclass

from core.domain.models.base_task import BaseTask


@dataclass
class SpecialTask(BaseTask):
    """ Special class for special tasks. """
