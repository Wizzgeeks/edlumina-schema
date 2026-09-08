from mongoengine import Document, StringField


class ClassName(Document):
    name = StringField(required=True)
    key = StringField(required=True, unique=True)

    def clean(self):
        self.name = self.name.strip()
        self.key = self.name.lower()

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "key": self.key,
        }

