from mongoengine import (
    Document,
    ReferenceField,
    ListField,
    DateTimeField,
    CASCADE,
    StringField
)
from datetime import datetime, timezone

from Models.institution import Institution
from Models.course import Course
from Models.batches import Batches
from Models.subject import Subject
from Models.institution_users import InstitutionUsers


class BatchTeacherSubjectAssignment(Document):
    institution = ReferenceField(
        Institution,
        required=True,
        reverse_delete_rule=CASCADE
    )

    course = ReferenceField(
        Course,
        required=True,
        reverse_delete_rule=CASCADE
    )

    batch = ReferenceField(
        Batches,
        required=True,
        reverse_delete_rule=CASCADE
    )

    subjects = ListField(
        ReferenceField(Subject, reverse_delete_rule=CASCADE),
        default=list
    )

    teacher = ReferenceField(
        InstitutionUsers,
        required=True,
        reverse_delete_rule=CASCADE
    )

    created_at = DateTimeField(
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = DateTimeField(
        default=lambda: datetime.now(timezone.utc)
    )

    created_by = StringField()
    updated_by = StringField()


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
        "id": str(self.id),
        "institution": self.institution.to_json() if self.institution else None,
        "course": self.course.to_json() if self.course else None,
        "batch": self.batch.to_json() if self.batch else None,
        "subjects": [str(s) for s in self.subjects if s] if self.subjects else [],
        "teacher": self.teacher.to_user() if self.teacher else None,
        "created_at": self.created_at,
        "updated_at": self.updated_at,
    }