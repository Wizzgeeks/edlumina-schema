from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, ListField,DictField,IntField,StringField,EmbeddedDocument,EmbeddedDocumentField
from datetime import datetime, timezone
from Models.initialOnboardingTest import InitialOnboardingTest

class CategoryScores(EmbeddedDocument):
    cognitive_function = IntField(default=0)
    social_emotional_skill = IntField(default=0)
    physical_development_skill = IntField(default=0)
    creative_imagination = IntField(default=0)
    critical_thinking_curiosity = IntField(default=0)
    language_communication = IntField(default=0)
    self_regulation_behavior = IntField(default=0)

class InitialOnboardingTestResult(Document):
    initial_onboarding_test=ReferenceField(InitialOnboardingTest,required=True)
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    attempt_questions=IntField()
    score=IntField()
    category_scores = EmbeddedDocumentField(CategoryScores, default=CategoryScores)

    duration=IntField(default=0)
    
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at=DateTimeField(default=datetime.now(timezone.utc))
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InitialOnboardingTestResult, self).save(*args, **kwargs)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "initial_onboarding_test": str(self.initial_onboarding_test.id) if self.initial_onboarding_test else None,
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "attempt_questions": self.attempt_questions,
            "score": self.score,
            "category_scores": {
                "cognitive_function": self.category_scores.cognitive_function,
                "social_emotional_skill": self.category_scores.social_emotional_skill,
                "physical_development_skill": self.category_scores.physical_development_skill,
                "creative_imagination": self.category_scores.creative_imagination,
                "critical_thinking_curiosity": self.category_scores.critical_thinking_curiosity,
                "language_communication": self.category_scores.language_communication,
                "self_regulation_behavior": self.category_scores.self_regulation_behavior,
            } if self.category_scores else None,
            "duration": self.duration,
            "created_at": self.created_at if self.created_at else None,
            "updated_at": self.updated_at if self.updated_at else None,
        }

    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "score": self.score,
            "completed": self.completed,
            "duration": self.duration,
            "attempt_questions": self.attempt_questions,
            "created_at": self.created_at if self.created_at else None,
        }

    
    