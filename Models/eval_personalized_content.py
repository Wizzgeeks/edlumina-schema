from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField, CASCADE, DictField, IntField
from datetime import datetime, timezone
from Models.user_course_personalized_content import UserCoursePersonalizedContent
from Models.user_subject_personalized_content import UserSubjectPersonalizedContent
from Models.user import Users
from Models.user_subtopic_personalized_content import UserSubTopicPersonalizedContent
from Models.user_topic_personalized_content import UserTopicPersonalizedContent


class EvalPersonalizedContent(Document):
    user_course_personalized_content=ReferenceField(UserCoursePersonalizedContent,reverse_delete_rule=CASCADE)
    user_subject_personalized_content=ReferenceField(UserSubjectPersonalizedContent,reverse_delete_rule=CASCADE)
    user_topic_personalized_content=ReferenceField(UserTopicPersonalizedContent,reverse_delete_rule=CASCADE)
    user_subtopic_personalized_content=ReferenceField(UserSubTopicPersonalizedContent,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,reverse_delete_rule=CASCADE)
    evalution_score=DictField()
    overall_score = IntField(min_value=0, max_value=10, required=True)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalPersonalizedContent, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "user_course_personalized_content_id": str(self.user_course_personalized_content.id) if self.user_course_personalized_content else None,
            "user_subject_personalized_content_id": str(self.user_subject_personalized_content.id) if self.user_subject_personalized_content else None,
            "user_topic_personalized_content_id": str(self.user_topic_personalized_content.id) if self.user_topic_personalized_content else None,
            "user_subtopic_personalized_content_id": str(self.user_subtopic_personalized_content.id) if self.user_subtopic_personalized_content else None,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,

        }