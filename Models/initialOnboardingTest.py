from Models.course import Course
from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, ListField,DictField,IntField
from datetime import datetime, timezone
class InitialOnboardingTest(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    content=ListField(DictField(),default=[])
    pass_percentage=IntField(default=0)
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at=DateTimeField(default=datetime.now(timezone.utc))
    is_active=BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InitialOnboardingTest, self).save(*args, **kwargs)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "content": self.content or [],
            "pass_percentage": self.pass_percentage,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
    