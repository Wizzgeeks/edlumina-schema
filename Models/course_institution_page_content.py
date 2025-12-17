from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField,ListField,DictField,CASCADE,IntField
from datetime import datetime, timezone
from Models.course import Course
from Models.question_bank import QuestionBank
from Models.institution import Institution


class CourseInstitutionPageContent(Document):
    course=ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    # question_bank=ReferenceField(QuestionBank)
    institution=ReferenceField(Institution,required=True,reverse_delete_rule=CASCADE)
    name=StringField(required=True)
    page_type=StringField(choices=['content','quiz','question_bank'], required=True)
    content=ListField(DictField(),default=[])
    medium_content=ListField(DictField())
    hard_content=ListField(DictField())
    compulsory=BooleanField(default=False)
    start_initial=BooleanField(default=False)
    start_end=BooleanField(default=False)
    child_pages = ListField(ReferenceField("CoursePageContent", reverse_delete_rule=NULLIFY))
    hierarcy_level=IntField(default=0)
    
    duration=IntField(default=0)
    pass_percentage=IntField(default=0)

    sequence=IntField(default=0)


    is_deleted=BooleanField(default=False)
    created_by=StringField()
    updated_by=StringField()
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(CourseInstitutionPageContent, self).save(*args, **kwargs)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "institution": self.institution.to_json() if self.institution else None,
            "question_bank": self.question_bank.to_json() if self.question_bank else None,
            "page_type": self.page_type,
            "content": self.content,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }