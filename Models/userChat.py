from Models.course_page_content import CoursePageContent
from Models.subject_page_content import SubjectPageContent
from Models.topic_page_content import TopicPageContent
from Models.subtopic_page_content import SubtopicPageContent
from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField, BooleanField, CASCADE
from datetime import datetime, timezone
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic
from Models.user import Users

class UserChat(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE)
    subtopic = ReferenceField(Subtopic, reverse_delete_rule=CASCADE)
    subtopic_page_content = ReferenceField(SubtopicPageContent, reverse_delete_rule=CASCADE)
    course_page_content = ReferenceField(CoursePageContent, reverse_delete_rule=CASCADE)
    topic_page_content = ReferenceField(TopicPageContent, reverse_delete_rule=CASCADE)
    subject_page_content = ReferenceField(SubjectPageContent, reverse_delete_rule=CASCADE)
    messages = ListField(StringField())
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(UserChat, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "course": self.course.to_json() if self.course else None,
            "subject": self.subject.to_json() if self.subject else None,
            "topic": self.topic.to_json() if self.topic else None,
            "subtopic": self.subtopic.to_json() if self.subtopic else None,
            "page_content": self.page_content.to_json() if self.page_content else None,
            "messages": self.messages,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }