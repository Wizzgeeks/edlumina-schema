from mongoengine import Document, ReferenceField, DateTimeField,ListField,DictField,CASCADE,NULLIFY,StringField
from datetime import datetime, timezone
from Models.user import Users
from Models.institution_users import InstitutionUsers
from Models.batches import Batches
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic

class SubtopicHomework(Document):
    batch=ReferenceField(Batches,required=True,reverse_delete_rule=CASCADE)
    teacher=ReferenceField(InstitutionUsers,required=True,reverse_delete_rule=CASCADE)
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,required=True, reverse_delete_rule=CASCADE)
    topic=ReferenceField(Topic,required=True, reverse_delete_rule=CASCADE)
    subtopic=ReferenceField(Subtopic,required=True,reverse_delete_rule=CASCADE)
    name=StringField()
    content=ListField(DictField(),default=[])
    users = ListField(ReferenceField(Users, reverse_delete_rule=NULLIFY))
    deadline=DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(SubtopicHomework, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            'teacher':str(self.teacher.id),
            "name":self.name,
            "content":self.content,
            'users':[str(s.id)for s in self.users],
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def to_user_homework(self):
        return {
            "id": str(self.id),
            'teacher':str(self.teacher.id),
            "name":self.name,
            "content":self.content,
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }