from mongoengine import CASCADE, Document, ReferenceField, BooleanField, StringField, DateTimeField,IntField,DictField
from Models.subtopic import Subtopic
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic_page_content import SubtopicPageContent
from datetime import datetime, timezone
from Models.course import Course
class EvalSubtopicPageContent(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE)
    subtopic = ReferenceField(Subtopic, reverse_delete_rule=CASCADE)
    subtopic_page_content = ReferenceField(SubtopicPageContent, reverse_delete_rule=CASCADE)
    is_evaluated = BooleanField(default=False)
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by =StringField()
    updated_by =StringField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalSubtopicPageContent, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "subtopic_page_content": str(self.subtopic_page_content.id) if self.subtopic_page_content else None,
            "is_evaluated": self.is_evaluated,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }