import uvicorn
from fastapi import FastAPI, Query, Path, Body, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from starlette import status

router = APIRouter(
    prefix="/api/v1",
    tags=["Basics"]
)


class User(BaseModel):
    username: str
    email: str
    age: int


class UserResponse(BaseModel):
    username: str
    email: str
    message: str

def validate_min_age(min_age: int = 18):
    def checker(user: User):
        if user.age < min_age:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User must be at least {min_age} years old."
            )
        return user
    return checker

app = FastAPI(title="basics")


@router.get("/basics/{item_id}")
async def get_basics(
        name: str = Query(
            default="Alice",
            description="Basic name",
        ),
        item_id: int = Path(
            ...,
            description="Item ID",
        )
):
    return {f"message: Hello, FastApi Basics, {name},"
            f"description: Item number {item_id}"}


@router.post("/basics/users", response_model=UserResponse)
async def create_user(user: User = Body(..., description="Данные нового пользователя")):
    return UserResponse(
        username=user.username,
        email=user.email,
        message="Юзер создан успешно"
    )

@router.post("/basics/register", summary="Регистрация нового пользователя с проверкой возраста")
async def register_user(user: User = Depends(validate_min_age(21))):
    return {
        "message": f"User {user.username} registered successfully!",
        "email": user.email,
        "age": user.age,
    }



app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "fastapi_basics:app",
        host="127.0.0.1",
        port=8010,
        reload=True,
        log_level="info",
    )
