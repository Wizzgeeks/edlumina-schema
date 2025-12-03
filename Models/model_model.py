from mongoengine import Document,StringField,ValidationError,BooleanField

class Model(Document):
    name = StringField(required=True,unique=True)
    api_key = StringField(required=True)
    type = StringField(required=True)
    provider = StringField(choices=['gemini','openai','claude'],required=True)
    is_active = BooleanField(default=False)
    page_type=StringField(choices=['content','quiz','ai-tutor','all'], required=True)

    
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Model name cannot be empty")
        if not self.api_key.strip():
            raise ValidationError("Api key cannot be empty")
        if not self.type.strip():
            raise ValidationError("model type cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "type":self.type,
            "provider":self.provider,
            "is_active":self.is_active if self.is_active else False
        }
    def to_admin(self):
        return{
            "id": str(self.id),
            "name":self.name,
            "type":self.type,
            "provider":self.provider,
            "api_key":self.api_key,
            "is_active":self.is_active if self.is_active else False
        }
    
        
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)