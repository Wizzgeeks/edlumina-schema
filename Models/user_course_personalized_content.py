from mongoengine import Document, ReferenceField, DateTimeField,StringField,DictField,ListField,CASCADE
from datetime import datetime,timezone
from Models.course import Course
from Models.user import Users
from Models.course_page_content import CoursePageContent

class UserCoursePersonalizedContent(Document):
    course = ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    user = ReferenceField(Users, required=True)
    # name = StringField()
    content = StringField(required=True)
    page_id=ReferenceField(CoursePageContent,required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(UserCoursePersonalizedContent, self).save(*args, **kwargs)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "course_name": self.course.name if self.course else None,
            "name": self.name,
            "content": self.content,
            "page_id": str(self.page_id),
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }