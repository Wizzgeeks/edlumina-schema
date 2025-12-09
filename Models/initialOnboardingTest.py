from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, ListField,DictField,IntField,StringField
from datetime import datetime, timezone
class InitialOnboardingTest(Document):
    name=StringField(required=True)
    content=ListField(DictField(),default=[])
    pass_percentage=IntField(default=0)
    duration=IntField(default=0)
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at=DateTimeField(default=datetime.now(timezone.utc))
    defaults=BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InitialOnboardingTest, self).save(*args, **kwargs)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "content": self.content or [],
            "pass_percentage": self.pass_percentage,
            "duration": self.duration,
            "defaults": self.defaults,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "pass_percentage": self.pass_percentage,
            "duration": self.duration,
            "defaults": self.defaults,
        }
    
    