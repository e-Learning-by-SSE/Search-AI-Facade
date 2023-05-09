import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.authentication_api import AuthenticationApi
from openapi_client.apis.tags.learning_path_api import LearningPathApi
from openapi_client.apis.tags.learning_unit_api import LearningUnitApi
from openapi_client.apis.tags.nugget_api import NuggetApi
from openapi_client.apis.tags.skill_api import SkillApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.LEARNING_PATH: LearningPathApi,
        TagValues.LEARNING_UNIT: LearningUnitApi,
        TagValues.NUGGET: NuggetApi,
        TagValues.SKILL: SkillApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.LEARNING_PATH: LearningPathApi,
        TagValues.LEARNING_UNIT: LearningUnitApi,
        TagValues.NUGGET: NuggetApi,
        TagValues.SKILL: SkillApi,
    }
)
