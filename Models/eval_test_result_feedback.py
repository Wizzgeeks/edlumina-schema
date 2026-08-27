from Models.test_result import TestResult
from Models.homework_completed import HomeworkCompleted
from mongoengine import CASCADE, NULLIFY, Document, ReferenceField, BooleanField, StringField, DateTimeField,IntField,DictField
from datetime import datetime, timezone
from Models.user import Users


class EvalTestResultFeedback(Document):
    test_result = ReferenceField(TestResult, reverse_delete_rule=CASCADE)
    homework_completed = ReferenceField(HomeworkCompleted, reverse_delete_rule=NULLIFY)
    # active_recall_completed stores the completed-record ObjectId as a plain string
    # because active recall results span 4 separate models (course/subject/topic/subtopic)
    active_recall_completed_id = StringField()
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
            "homework_completed": str(self.homework_completed.id) if self.homework_completed else None,
            "active_recall_completed_id": self.active_recall_completed_id,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }