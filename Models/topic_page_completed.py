from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,IntField, ListField, DictField
from datetime import datetime, timezone
from Models.topic_page_content import TopicPageContent
from Models.user import Users
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic

class TopicPageCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE, required=True)
    topic_page_content = ReferenceField(TopicPageContent, reverse_delete_rule=CASCADE, required=True)
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    hierarcy_level=IntField(default=0)
    page_type=StringField(choices=['content','quiz','question_bank','test','mcq','match','fillups','content','expand','update','trueorfalse','analysis'], required=True)
    
    question=ListField(DictField(),default=[])
    content_quiz_completed=BooleanField(default=False)
    no_of_questions_attempted=IntField()
    no_of_question_correct=IntField()
    user_answers=ListField(DictField(),default=[])
    feedback=ListField(DictField(),default=[])
    total_questions=IntField()
    no_of_attempts=IntField(default=0)
    question_attempt_history = ListField(DictField(), default=[])
    last_attempted_at = DateTimeField() 
    
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TopicPageCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.id if self.course else None,
            # "subject": self.subject.id if self.subject else None,
            # "topic": self.topic.id if self.topic else None,
            # "topic_page_content": self.topic_page_content.id if self.topic_page_content else None,
            # "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "page_type": self.page_type,
        }

    def to_dict(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "subject": str(self.subject.id) if self.subject else None,
            "topic": str(self.topic.id) if self.topic else None,
            "topic_page_content": str(self.topic_page_content.id) if self.topic_page_content else None,
            "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "question": self.question,
            "content_quiz_completed": self.content_quiz_completed,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
            "user_answers": self.user_answers,
            "feedback": self.feedback,
            "total_questions": self.total_questions,
            "no_of_attempts": self.no_of_attempts,
            "question_attempt_history": self.question_attempt_history,
            "last_attempted_at": self.last_attempted_at,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }