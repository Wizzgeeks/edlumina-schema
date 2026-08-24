from Models.test_result import TestResult
from mongoengine import CASCADE, Document, ReferenceField, BooleanField, StringField, DateTimeField,IntField,DictField
from datetime import datetime, timezone
from Models.user import Users


class EvalTestResultFeedback(Document):
    test_result = ReferenceField(TestResult, reverse_delete_rule=CASCADE)
    user=ReferenceField(Users, reverse_delete_rule=CASCADE)
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)    
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalTestResultFeedback, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "test_result": str(self.test_result.id) if self.test_result else None,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }