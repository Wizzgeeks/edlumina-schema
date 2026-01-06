from typing import Required
from mongoengine import CASCADE, NULLIFY, Document,StringField,BooleanField,EnumField,ReferenceField,ListField,DictField,EmbeddedDocument,DateTimeField,IntField,EmbeddedDocumentField
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic
from datetime import datetime,timezone
from Models.user import Users


class ActiveRecallContent(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    topic=ReferenceField(Topic,reverse_delete_rule=CASCADE)
    subtopic=ReferenceField(Subtopic,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,reverse_delete_rule=CASCADE)
    completed = BooleanField(default=False)
    layer=StringField()
    active_date=DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(ActiveRecallContent, self).save(*args, **kwargs)

    def to_json(self):
        return{
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "subject":str(self.subject.id) if self.subject else None,
            "topic":str(self.topic.id) if self.topic else None,
            "subtopic":str(self.subtopic.id) if self.subtopic else None,
            "user":str(self.user.id) if self.user else None,
            "completed":self.completed, 
            "active_date":self.active_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,            
        }
