from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField,CASCADE,IntField,DictField
from datetime import datetime, timezone
from Models.ai_tutor_content import AiTutorContent


from Models.user import Users

class EvalAiTutorContent(Document):
    ai_tutor_content=ReferenceField(AiTutorContent,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,reverse_delete_rule=CASCADE)
    content=StringField()
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalAiTutorContent, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "ai_tutor_content_id": str(self.ai_tutor_content.id) if self.ai_tutor_content else None,
            "content": self.content,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,

        }