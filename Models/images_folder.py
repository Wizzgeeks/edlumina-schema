from mongoengine import Document, StringField, ListField, URLField, DateTimeField,DictField
from datetime import datetime, timezone

class ImageFolder(Document):
    name = StringField(required=True, unique=True)
    images_data=ListField(DictField())
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(ImageFolder, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "images_data": self.images_data,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    def to_json_medium(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }