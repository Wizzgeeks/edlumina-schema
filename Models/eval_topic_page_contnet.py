from mongoengine import CASCADE,DictField, Document, ReferenceField, BooleanField, StringField, DateTimeField,IntField
from Models.topic import Topic
from Models.subject import Subject
from Models.topic_page_content import TopicPageContent
from datetime import datetime, timezone
from Models.course import Course


class EvalTopicPageContent(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE)
    topic_page_content = ReferenceField(TopicPageContent, reverse_delete_rule=CASCADE)
    is_evaluated = BooleanField(default=False)
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)


    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by =StringField()
    updated_by =StringField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalTopicPageContent, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "topic_page_content": str(self.topic_page_content.id) if self.topic_page_content else None,
            "is_evaluated": self.is_evaluated,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }