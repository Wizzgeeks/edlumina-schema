from mongoengine import (
    Document,
    ReferenceField,
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

    subject = ReferenceField(
        Subject,
        required=True,
        reverse_delete_rule=CASCADE
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

    meta = {
    "indexes": [
        ("batch", "subject"),
        ("teacher",),
        ("course",),
        ("institution",),
    ]
    # a subject in a batch can only be assigned to one teacher.
    #
    # "indexes": [
    #     {
    #         "fields": ["batch", "subject"],
    #         "unique": True
    #     }
    # ]
}

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
        "id": str(self.id),
        "institution": self.institution.to_json() if self.institution else None,
        "course": self.course.to_json() if self.course else None,
        "batch": self.batch.to_json() if self.batch else None,
        "subject": self.subject.to_json() if self.subject else None,
        "teacher": self.teacher.to_user() if self.teacher else None,
        "created_at": self.created_at,
        "updated_at": self.updated_at,
    }