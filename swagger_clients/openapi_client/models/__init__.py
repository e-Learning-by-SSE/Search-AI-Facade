# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.auth_dto import AuthDto
from openapi_client.model.learning_path_creation_dto import LearningPathCreationDto
from openapi_client.model.learning_path_dto import LearningPathDto
from openapi_client.model.learning_path_list_dto import LearningPathListDto
from openapi_client.model.login_ack_dto import LoginAckDto
from openapi_client.model.login_dto import LoginDto
from openapi_client.model.nugget_creation_dto import NuggetCreationDto
from openapi_client.model.nugget_dto import NuggetDto
from openapi_client.model.path_goal_creation_dto import PathGoalCreationDto
from openapi_client.model.path_goal_dto import PathGoalDto
from openapi_client.model.resolved_skill_repository_dto import ResolvedSkillRepositoryDto
from openapi_client.model.search_learning_unit_creation_dto import SearchLearningUnitCreationDto
from openapi_client.model.search_learning_unit_dto import SearchLearningUnitDto
from openapi_client.model.search_learning_unit_list_dto import SearchLearningUnitListDto
from openapi_client.model.skill_creation_dto import SkillCreationDto
from openapi_client.model.skill_dto import SkillDto
from openapi_client.model.skill_repository_creation_dto import SkillRepositoryCreationDto
from openapi_client.model.skill_repository_dto import SkillRepositoryDto
from openapi_client.model.skill_repository_list_dto import SkillRepositoryListDto
from openapi_client.model.skill_repository_search_dto import SkillRepositorySearchDto
from openapi_client.model.unresolved_skill_repository_dto import UnresolvedSkillRepositoryDto
