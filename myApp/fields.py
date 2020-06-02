from django.db.models import TextField



class NonStrippingTextField(TextField):

    def formfield(self, **kwargs):
        kwargs['strip']=False
        return super(NonStrippingTextField,self).formfield(**kwargs)

