from mongoengine import Document, IntField, ListField,ReferenceField,DateTimeField,BooleanField,CASCADE,DictField
from Models.course_homework import CourseHomework
from Models.subject_homework import SubjectHomework
from Models.topic_homework import TopicHomework
from Models.subtopic_homework import SubtopicHomework
from Models.user import Users
from datetime import datetime, timezone


class HomeworkCompleted(Document):
    course_homework=ReferenceField(CourseHomework,reverse_delete_rule=CASCADE)
    subject_homework=ReferenceField(SubjectHomework,reverse_delete_rule=CASCADE)
    topic_homework=ReferenceField(TopicHomework,reverse_delete_rule=CASCADE)
    subtopic_homework=ReferenceField(SubtopicHomework,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,required=True,reverse_delete_rule=CASCADE)
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    no_of_questions_attempted=IntField()
    no_of_question_correct=IntField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(HomeworkCompleted, self).save(*args, **kwargs)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
        }
    
    def to_user_list(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
        }