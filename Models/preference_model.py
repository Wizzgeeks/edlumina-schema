from mongoengine import Document, DateTimeField, BooleanField, ListField, DictField,StringField
from datetime import datetime, timezone


class PreferenceQuestion(Document):
    name=StringField(required=True)
    content = ListField(DictField(), default=[])
    is_active = BooleanField(default=True)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(PreferenceQuestion, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "content": self.content,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }