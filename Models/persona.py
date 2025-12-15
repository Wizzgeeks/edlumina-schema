from mongoengine import Document, StringField  ,BooleanField


class Persona(Document):
    name = StringField(required=True, unique=True)
    persona=StringField()
    persona_type=StringField(choices=['ai_tutor','analysis_validation'],required=True)
    is_active= BooleanField(default=False)


    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "persona": self.persona,
            "persona_type": self.persona_type,
            "is_active": self.is_active
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "persona_type": self.persona_type,
            "is_active": self.is_active
        }