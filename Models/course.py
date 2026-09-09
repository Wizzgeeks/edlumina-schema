from mongoengine import Document,StringField,IntField,DateTimeField,BooleanField,ReferenceField,NULLIFY
from datetime import datetime,timezone
from Models.initialOnboardingTest import InitialOnboardingTest

class Course(Document):
    initialOnboardingTest=ReferenceField(InitialOnboardingTest,reverse_delete_rule=NULLIFY)
    psychometricTest=ReferenceField(InitialOnboardingTest,reverse_delete_rule=NULLIFY)
    iqTest=ReferenceField(InitialOnboardingTest,reverse_delete_rule=NULLIFY)
    name = StringField(required=True,unique=True)
    key = StringField(required=True, unique=True)
    board = StringField()
    class_name = StringField()
    is_deleted = BooleanField(default=False)
    active_recall_interval_days= IntField(default=0)
    pass_percentage=IntField(default=80)
    total_number_quizes=IntField(default=3)
    publish=BooleanField(default=False)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Course, self).save(*args, **kwargs)



    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "key": self.key,
            "publish": self.publish,
            "initialOnboardingTest":str(self.initialOnboardingTest.id) if self.initialOnboardingTest else None,
            "psychometricTest":str(self.psychometricTest.id) if self.psychometricTest else None,
            "iqTest":str(self.iqTest.id) if self.iqTest else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "active_recall_interval_days":self.active_recall_interval_days,
            "pass_percentage": self.pass_percentage,
            "total_number_quizes": self.total_number_quizes,
            "board": self.board if getattr(self, 'board', None) else "",
            "class_name": self.class_name if getattr(self, 'class_name', None) else "",
        }
