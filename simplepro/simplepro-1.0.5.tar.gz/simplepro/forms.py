from django .forms import ModelForm 
def create_dynamic_model_form (**O00000O00OO000000 ):
    ""
    class OOO00OO0O0OOO0OO0 :
        model =O00000O00OO000000 .get ('model')
        fields =O00000O00OO000000 .get ('fields')
    OO00O00O00OOO000O =type ('DynamicModelForm',(ModelForm ,),{'Meta':OOO00OO0O0OOO0OO0 })
    return OO00O00O00OOO000O 
