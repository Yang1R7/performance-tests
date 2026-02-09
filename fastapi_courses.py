from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, RootModel
from starlette import status

app = FastAPI()
courses_router = APIRouter(
    prefix="/api/v1/courses",
    tags=["courses-service"]
)

class CourseIn(BaseModel):
    title: str
    max_score: int
    min_score: int
    description: str


class CourseOut(CourseIn):
    id: int


class UserStore(RootModel):
    root: list[CourseOut]

    def find(self, course_id: int) -> CourseOut:
        return next(filter(lambda user: user.id == course_id, self.root), None)

    def create(self, course_in: CourseIn) -> CourseOut:
        user = CourseOut(id = len(self.root) + 1, **course_in.model_dump())
        self.root.append(user)
        return user

    def update(self, course_id: int, user_in: CourseIn) -> CourseOut:
        index = next(index for index, user in enumerate(self.root) if user.id == course_id)
        updated = CourseOut(id = course_id, **user_in.model_dump())
        self.root[index] = updated
        return updated

    def delete(self, course_id: int) -> None:
        self.root = [course for course in self.root if course.id != course_id]


store = UserStore(root=[])


@courses_router.get("/{user_id}", response_model=CourseOut)
async def get_course(course_id: int):
    if not (course := store.find(course_id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} not found")

    return course


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    return store.root


@courses_router.post("",response_model=CourseOut)
async def create_course(course: CourseIn):
    return store.create(course)

@courses_router.put("/{course_id}",response_model=CourseOut)
async def update_user(course_id: int, user: CourseIn):
    if not store.find(course_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} not found")
    return store.update(course_id, user)


@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(course_id: int):
    if not store.find(course_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} not found")
    store.delete(course_id)





app.include_router(courses_router)