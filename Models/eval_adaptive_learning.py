from Models.adaptive_learning_test_mcq import AdaptiveLearningTestMcq
from mongoengine import CASCADE, Document, ReferenceField, BooleanField, StringField, DateTimeField,IntField,DictField
from datetime import datetime, timezone
from Models.user import Users


class EvalAdaptiveLearning(Document):
    adaptive_learning_test_mcq = ReferenceField(AdaptiveLearningTestMcq, reverse_delete_rule=CASCADE)
    user=ReferenceField(Users, reverse_delete_rule=CASCADE)
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)    
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalAdaptiveLearning, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "adaptive_learning_test_mcq": str(self.adaptive_learning_test_mcq.id) if self.adaptive_learning_test_mcq else None,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }