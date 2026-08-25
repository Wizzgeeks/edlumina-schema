from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField, CASCADE, DictField, IntField
from datetime import datetime, timezone
from Models.subtopic_page_completed import SubtopicPageCompleted
from Models.user import Users
from Models.topic_page_completed import TopicPageCompleted
from Models.subject_page_completed import SubjectPageCompleted
from Models.course_page_completed import CoursePageCompleted


class EvalPersonalizedQuiz(Document):
    subtopic_page_completed=ReferenceField(SubtopicPageCompleted,reverse_delete_rule=CASCADE)
    topic_page_completed=ReferenceField(TopicPageCompleted,reverse_delete_rule=CASCADE)
    subject_page_completed=ReferenceField(SubjectPageCompleted,reverse_delete_rule=CASCADE)
    course_page_completed=ReferenceField(CoursePageCompleted,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,reverse_delete_rule=CASCADE)
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalPersonalizedQuiz, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "subtopic_page_completed_id": str(self.subtopic_page_completed.id) if self.subtopic_page_completed else None,
            "topic_page_completed_id": str(self.topic_page_completed.id) if self.topic_page_completed else None,
            "subject_page_completed_id": str(self.subject_page_completed.id) if self.subject_page_completed else None,
            "course_page_completed_id": str(self.course_page_completed.id) if self.course_page_completed else None,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,

        }