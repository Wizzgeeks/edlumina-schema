from mongoengine import BooleanField, Document, StringField


class Board(Document):
    name = StringField(required=True)
    key = StringField(required=True, unique=True)
    is_course = BooleanField(default=False)
    is_institution = BooleanField(default=False)

    def clean(self):
        self.name = self.name.strip()
        self.key = self.name.lower()

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "is_course": self.is_course,
            "is_institution": self.is_institution,
        }



