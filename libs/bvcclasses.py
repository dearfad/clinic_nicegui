from enum import Enum

class Role(Enum):
    VISITOR = "游客"
    STUDENT = "学生"
    TEACHER = "教师"
    ADMIN = "管理员"

    def __str__(self):
        return self.value