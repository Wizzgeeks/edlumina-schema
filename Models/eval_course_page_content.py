from Models.course import Course
from mongoengine import CASCADE, Document, ReferenceField, BooleanField, StringField, DateTimeField,IntField,ListField,DictField
from Models.course_page_content import CoursePageContent
from datetime import datetime, timezone


class EvalCoursePageContent(Document):
    course_page_content = ReferenceField(CoursePageContent, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    is_evaluated = BooleanField(default=False)
    evalution_score=DictField()
    overall_score= IntField(min_value=0, max_value=10, required=True)

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by =StringField()
    updated_by =StringField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(EvalCoursePageContent, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "course_page_content": str(self.course_page_content.id) if self.course_page_content else None,
            "is_evaluated": self.is_evaluated,
            "evalution_score": self.evalution_score,
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    