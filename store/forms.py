from django.forms import ModelForm
from .models import *
class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields =[ 'title','slug','short_description','detail_description','sku','product_image','category','price','is_active','is_featured','Seller_Name']

    def __init__(self,*args,**kwargs):
        super(ProductForm, self).__init__(*args,**kwargs)

        

        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['slug'].widget.attrs.update({'class':'form-control'})
        self.fields['short_description'].widget.attrs.update({'class':'form-control'})
        self.fields['detail_description'].widget.attrs.update({'class':'form-control'})
        self.fields['sku'].widget.attrs.update({'class':'form-control'})
        self.fields['product_image'].widget.attrs.update({'class':'form-control'})
        self.fields['category'].widget.attrs.update({'class':'form-control'})
        self.fields['price'].widget.attrs.update({'class':'form-control'})
        self.fields['is_active'].widget.attrs.update({'class':''})
        self.fields['is_active'].widget.attrs.update({'class':''})
        self.fields['Seller_Name'].widget.attrs.update({'class':'form-control'})


        

