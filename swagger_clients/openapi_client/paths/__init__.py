# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTH_REGISTER = "/auth/register"
    AUTH_LOGIN = "/auth/login"
    SKILLREPOSITORIES = "/skill-repositories"
    SKILLREPOSITORIES_SHOW_OWN = "/skill-repositories/showOwn"
    SKILLREPOSITORIES_SHOW_ALL_SKILLS = "/skill-repositories/showAllSkills"
    SKILLREPOSITORIES_REPOSITORY_ID = "/skill-repositories/{repositoryId}"
    SKILLREPOSITORIES_RESOLVE_REPOSITORY_ID = "/skill-repositories/resolve/{repositoryId}"
    SKILLREPOSITORIES_SKILL_CREATE = "/skill-repositories/skill/create"
    SKILLREPOSITORIES_REPOSITORY_ID_SKILL_ADD_SKILL = "/skill-repositories/{repositoryId}/skill/add_skill"
    SKILLREPOSITORIES_SKILL_SKILL_ID = "/skill-repositories/skill/{skillId}"
    NUGGETS_SHOW_ALL_NUGGETS = "/nuggets/showAllNuggets"
    NUGGETS_ADD_NUGGET = "/nuggets/add_nugget"
    NUGGETS_NUGGET_ID = "/nuggets/{nuggetId}"
    LEARNINGPATHS_SHOW_ALL_LEARNING_PATHS = "/learningpaths/showAllLearningPaths"
    LEARNINGPATHS_ADD_LEARNINGPATH = "/learningpaths/add_learningpath"
    LEARNINGPATHS_LEARNINGPATH_ID = "/learningpaths/{learningpathId}"
    LEARNING_UNITS_SHOW_ALL_LEARNING_UNITS = "/learningUnits/showAllLearningUnits"
    LEARNING_UNITS_ADD_LEARNING_UNIT = "/learningUnits/add_learningUnit"
    LEARNING_UNITS_LEARNING_UNIT_ID = "/learningUnits/{learningUnitId}"
