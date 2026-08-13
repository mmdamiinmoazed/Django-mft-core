from django import forms



class ContactForm(forms.Form) :
    fullname = forms.CharField(max_length=50 , min_length=10 , required=True , widget=forms.TextInput({"placeholder" : 
                                                                                                       "Please Enter the first_name" , "id" : "c-first"})) 
    last_name = forms.CharField(max_length=50 , min_length=10 , required=True , widget=forms.TextInput({"placeholder" : 
                                                                                                       "Please Enter the last_name" , "id" : "c-last"})) 
    # fullname = forms.CharField(max_length=50 , min_length=10 , required=True , widget=forms.TextInput({"placeholder" : 
    #                                                                                                    "Please Enter the input"})) 
    # fullname = forms.CharField(max_length=50 , min_length=10 , required=True , widget=forms.TextInput({"placeholder" : 
    #                                                                                              "Please Enter the input"})) 
    email = forms.EmailField(max_length=50 , min_length=10 , required=True , error_messages={
        "required" : "This field should not be empty"
    } , widget=forms.EmailInput({"placeholder" : "You can write your email here"}))
    phone = forms.CharField(max_length=12 ,required=True , error_messages={""
    "required" : "This field should not be empty" } , label="Your phone" , widget=forms.TextInput({"placeholder" : "Phone number" , "id" : "c-phone"}))
    subject = forms.ChoiceField(choices=[("login" , "Login problem"),
                                          ("register" , "Register problem") , 
                                          ("complain" , "complain about other things")] , )
    message = forms.CharField(max_length=10000  , required=True  , widget=forms.Textarea({"placeholder" : "You can write your message here"}))
