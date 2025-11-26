from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField,BooleanField,EmbeddedDocument,DictField,EmbeddedDocumentField,CASCADE
from datetime import datetime, timezone


class AdminPermissions(EmbeddedDocument):
    permission_type=StringField(choices=["student","course","batches","questionbank"],required=True)
    read=BooleanField(default=False)
    write=BooleanField(default=False)
    def to_json(self):
        return {
            "permission_type":self.permission_type,
            "read":self.read,
            "write":self.write
        }

class TeachersPermissions(EmbeddedDocument):
    permission_type=StringField(choices=["student","course","batches","questionbank"],required=True)
    read=BooleanField(default=False)
    write=BooleanField(default=False)
    def to_json(self):
        return {
            "permission_type":self.permission_type,
            "read":self.read,
            "write":self.write
        }



class Institution(Document):
    name = StringField(required=True, unique=True)
    description = StringField()
    created_by=StringField()
    updated_by = StringField()
    mobile=StringField()
    admin_permissions = ListField(
        EmbeddedDocumentField(AdminPermissions)
    )
    teacher_permissions = ListField(
        EmbeddedDocumentField(TeachersPermissions)
    )
    is_deleted = BooleanField(default=False)
    disabled=BooleanField(default=False)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Institution, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "admin_permissions": [p.to_json() for p in self.admin_permissions],
            "teacher_permissions": [t.to_json() for t in self.teacher_permissions],
            "description": self.description,
            "mobile": self.mobile,
            "disabled": self.disabled if self.disabled else False,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "is_deleted": self.is_deleted,
        }