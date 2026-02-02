from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    ListField,
    DateTimeField,
    CASCADE,
    NULLIFY
)
from datetime import datetime, timezone

from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic
from Models.course_page_content import CoursePageContent
from Models.subject_page_content import SubjectPageContent
from Models.topic_page_content import TopicPageContent
from Models.subtopic_page_content import SubtopicPageContent


class EvalBook(Document):

    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    subjects = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    topics = ReferenceField(Topic, reverse_delete_rule=CASCADE)
    subtopic = ReferenceField(Subtopic, reverse_delete_rule=CASCADE)

    course_pages = ListField(ReferenceField(CoursePageContent,reverse_delete_rule=NULLIFY))
    subject_pages = ListField(ReferenceField(SubjectPageContent,reverse_delete_rule=NULLIFY))
    topic_pages = ListField(ReferenceField(TopicPageContent,reverse_delete_rule=NULLIFY))
    subtopic_pages = ListField(ReferenceField(SubtopicPageContent,reverse_delete_rule=NULLIFY))

    book_id = StringField(required=True)
    book_name = StringField(required=True)

    created_by = StringField()
    updated_by = StringField()

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))



    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "book_id": self.book_id,
            "book_name": self.book_name,
            "course": str(self.course.id) if self.course else None,
            "subjects": [str(s.id) for s in self.subjects],
            "topics": [str(t.id) for t in self.topics],
            "subtopics": [str(st.id) for st in self.subtopic],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
