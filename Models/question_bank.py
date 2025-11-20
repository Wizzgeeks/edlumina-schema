from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField,DictField,BooleanField  
from datetime import datetime, timezone


class QuestionBank(Document):
    name =StringField(required=True)
    content =ListField(DictField(),default=[])
    question_bank_type =StringField(choices=['pdf','video','practise_test'],required=True)
    publish=BooleanField(default=False)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(QuestionBank, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "content": self.content,
            "question_bank_type": self.question_bank_type,
            "publish": self.publish,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }