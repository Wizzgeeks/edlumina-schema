from Models.institution import Institution
from Models.course import Course
from Models.batches import Batches
from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, StringField
from datetime import datetime, timezone


class Users(Document):
    institution=ReferenceField(Institution, reverse_delete_rule=CASCADE,default=None)
    course=ReferenceField(Course, reverse_delete_rule=CASCADE,default=None)
    batch=ReferenceField(Batches, reverse_delete_rule=CASCADE,default=None)
    name=StringField(required=True)
    email=StringField(unique=True,sparse=True)
    register_no=StringField(unique=True,sparse=True)
    password=StringField(required=True)
    auth_token=StringField()
    disabled=BooleanField(default=False)
    is_deleted=BooleanField(default=False)
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Users, self).save(*args, **kwargs)
        
    def to_json(self):
        return {
            "id": str(self.id),
            "institution": self.institution.to_json() if self.institution else None,
            "course": self.course.to_json() if self.course else None,
            "batch": self.batch.to_json() if self.batch else None,
            "name": self.name,
            "email": self.email if self.email else "",
            "register_no": self.register_no if self.register_no else "",
            "disabled": self.disabled if self.disabled else False,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,

        }
    def to_user(self):
        return {
            "id": str(self.id),
            "institution": self.institution.to_json() if self.institution else None,
            "course": self.course.to_json() if self.course else None,
            "name": self.name,
            "email": self.email if self.email else "",
            "register_no": self.register_no if self.register_no else "",
            "auth_token": self.auth_token if self.auth_token else "",
           
        }
    