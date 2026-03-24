from mongoengine import Document, StringField, ListField, URLField, DateTimeField,DictField
from datetime import datetime, timezone

class ImageFolder(Document):
    name = StringField(required=True, unique=True)
    images_data=ListField(DictField())
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))