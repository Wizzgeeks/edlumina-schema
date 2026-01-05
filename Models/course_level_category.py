from mongoengine import CASCADE, NULLIFY, Document,StringField,BooleanField,EnumField,ReferenceField,ListField,DictField,EmbeddedDocument,DateTimeField,IntField,EmbeddedDocumentField
from datetime import datetime,timezone
from Models.course_page_content import CoursePageContent
from Models.course import Course


class CourseLevelCategory(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE)
    page_content=ReferenceField(CoursePageContent,reverse_delete_rule=CASCADE)
    direct=IntField(default=0)
    reasoning=IntField(default=0)
    critical_thinking=IntField(default=0)
    application=IntField(default=0)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(CourseLevelCategory, self).save(*args, **kwargs)

    def to_json(self):
        return{
            "id": str(self.id),
            "page_content":str(self.page_content.id) if self.page_content else None,
            "direct": self.direct,
            "reasoning": self.reasoning,
            "critical_thinking": self.critical_thinking,
            "application": self.application,
            "created_at": self.created_at,
            "updated_at": self.updated_at,            
        }
