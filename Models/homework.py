from mongoengine import Document, ReferenceField, DateTimeField,ListField,DictField,CASCADE,NULLIFY
from datetime import datetime, timezone
from Models.user import Users
from Models.institution_users import InstitutionUsers
from Models.batches import Batches

class Homework(Document):
    batch=ReferenceField(Batches,reverse_delete_rule=CASCADE)
    teacher=ReferenceField(InstitutionUsers,reverse_delete_rule=CASCADE)
    content=ListField(DictField(),default=[])
    users = ListField(ReferenceField(Users, reverse_delete_rule=NULLIFY))
    deadline=DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Homework, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            'teacher':str(self.teacher.id),
            "content":self.content,
            'users':[str(s.id)for s in self.users],
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
