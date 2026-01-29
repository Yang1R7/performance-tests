from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserSchema(BaseModel):
    """
    Схема данных для представления пользователя.
    """
    model_config = ConfigDict(validate_by_alias=True)
    id: str
    email: EmailStr
    lastName: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")
    phoneNumber: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
    Схема данных для запроса на создание нового пользователя.
    """
    model_config = ConfigDict(validate_by_alias=True)
    email: EmailStr
    lastName: str = Field(alias="lastName")
    firstName: str = Field(alias="firstName")
    middleName: str = Field(alias="middleName")
    phoneNumber: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Схема данных для ответа на запрос создания пользователя.
    """
    model_config = ConfigDict(validate_by_alias=True)
    user: UserSchema
