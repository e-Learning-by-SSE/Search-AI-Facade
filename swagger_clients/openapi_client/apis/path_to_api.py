import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.auth_register import AuthRegister
from openapi_client.apis.paths.auth_login import AuthLogin
from openapi_client.apis.paths.skill_repositories import SkillRepositories
from openapi_client.apis.paths.skill_repositories_show_own import SkillRepositoriesShowOwn
from openapi_client.apis.paths.skill_repositories_show_all_skills import SkillRepositoriesShowAllSkills
from openapi_client.apis.paths.skill_repositories_repository_id import SkillRepositoriesRepositoryId
from openapi_client.apis.paths.skill_repositories_resolve_repository_id import SkillRepositoriesResolveRepositoryId
from openapi_client.apis.paths.skill_repositories_skill_create import SkillRepositoriesSkillCreate
from openapi_client.apis.paths.skill_repositories_repository_id_skill_add_skill import SkillRepositoriesRepositoryIdSkillAddSkill
from openapi_client.apis.paths.skill_repositories_skill_skill_id import SkillRepositoriesSkillSkillId
from openapi_client.apis.paths.nuggets_show_all_nuggets import NuggetsShowAllNuggets
from openapi_client.apis.paths.nuggets_add_nugget import NuggetsAddNugget
from openapi_client.apis.paths.nuggets_nugget_id import NuggetsNuggetId
from openapi_client.apis.paths.learningpaths_show_all_learning_paths import LearningpathsShowAllLearningPaths
from openapi_client.apis.paths.learningpaths_add_learningpath import LearningpathsAddLearningpath
from openapi_client.apis.paths.learningpaths_learningpath_id import LearningpathsLearningpathId
from openapi_client.apis.paths.learning_units_show_all_learning_units import LearningUnitsShowAllLearningUnits
from openapi_client.apis.paths.learning_units_add_learning_unit import LearningUnitsAddLearningUnit
from openapi_client.apis.paths.learning_units_learning_unit_id import LearningUnitsLearningUnitId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_REGISTER: AuthRegister,
        PathValues.AUTH_LOGIN: AuthLogin,
        PathValues.SKILLREPOSITORIES: SkillRepositories,
        PathValues.SKILLREPOSITORIES_SHOW_OWN: SkillRepositoriesShowOwn,
        PathValues.SKILLREPOSITORIES_SHOW_ALL_SKILLS: SkillRepositoriesShowAllSkills,
        PathValues.SKILLREPOSITORIES_REPOSITORY_ID: SkillRepositoriesRepositoryId,
        PathValues.SKILLREPOSITORIES_RESOLVE_REPOSITORY_ID: SkillRepositoriesResolveRepositoryId,
        PathValues.SKILLREPOSITORIES_SKILL_CREATE: SkillRepositoriesSkillCreate,
        PathValues.SKILLREPOSITORIES_REPOSITORY_ID_SKILL_ADD_SKILL: SkillRepositoriesRepositoryIdSkillAddSkill,
        PathValues.SKILLREPOSITORIES_SKILL_SKILL_ID: SkillRepositoriesSkillSkillId,
        PathValues.NUGGETS_SHOW_ALL_NUGGETS: NuggetsShowAllNuggets,
        PathValues.NUGGETS_ADD_NUGGET: NuggetsAddNugget,
        PathValues.NUGGETS_NUGGET_ID: NuggetsNuggetId,
        PathValues.LEARNINGPATHS_SHOW_ALL_LEARNING_PATHS: LearningpathsShowAllLearningPaths,
        PathValues.LEARNINGPATHS_ADD_LEARNINGPATH: LearningpathsAddLearningpath,
        PathValues.LEARNINGPATHS_LEARNINGPATH_ID: LearningpathsLearningpathId,
        PathValues.LEARNING_UNITS_SHOW_ALL_LEARNING_UNITS: LearningUnitsShowAllLearningUnits,
        PathValues.LEARNING_UNITS_ADD_LEARNING_UNIT: LearningUnitsAddLearningUnit,
        PathValues.LEARNING_UNITS_LEARNING_UNIT_ID: LearningUnitsLearningUnitId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_REGISTER: AuthRegister,
        PathValues.AUTH_LOGIN: AuthLogin,
        PathValues.SKILLREPOSITORIES: SkillRepositories,
        PathValues.SKILLREPOSITORIES_SHOW_OWN: SkillRepositoriesShowOwn,
        PathValues.SKILLREPOSITORIES_SHOW_ALL_SKILLS: SkillRepositoriesShowAllSkills,
        PathValues.SKILLREPOSITORIES_REPOSITORY_ID: SkillRepositoriesRepositoryId,
        PathValues.SKILLREPOSITORIES_RESOLVE_REPOSITORY_ID: SkillRepositoriesResolveRepositoryId,
        PathValues.SKILLREPOSITORIES_SKILL_CREATE: SkillRepositoriesSkillCreate,
        PathValues.SKILLREPOSITORIES_REPOSITORY_ID_SKILL_ADD_SKILL: SkillRepositoriesRepositoryIdSkillAddSkill,
        PathValues.SKILLREPOSITORIES_SKILL_SKILL_ID: SkillRepositoriesSkillSkillId,
        PathValues.NUGGETS_SHOW_ALL_NUGGETS: NuggetsShowAllNuggets,
        PathValues.NUGGETS_ADD_NUGGET: NuggetsAddNugget,
        PathValues.NUGGETS_NUGGET_ID: NuggetsNuggetId,
        PathValues.LEARNINGPATHS_SHOW_ALL_LEARNING_PATHS: LearningpathsShowAllLearningPaths,
        PathValues.LEARNINGPATHS_ADD_LEARNINGPATH: LearningpathsAddLearningpath,
        PathValues.LEARNINGPATHS_LEARNINGPATH_ID: LearningpathsLearningpathId,
        PathValues.LEARNING_UNITS_SHOW_ALL_LEARNING_UNITS: LearningUnitsShowAllLearningUnits,
        PathValues.LEARNING_UNITS_ADD_LEARNING_UNIT: LearningUnitsAddLearningUnit,
        PathValues.LEARNING_UNITS_LEARNING_UNIT_ID: LearningUnitsLearningUnitId,
    }
)
