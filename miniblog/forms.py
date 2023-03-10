from django import forms
import os

VALID_EXTENSIONS = ['.jpg']
class UploadFileForm(forms.Form):
    image = forms.ImageField(label='Select a file')
    def clean_image(self):
        image = self.cleaned_data['myfile']
        extension = os.path.splitext(image.name)[1]  # 拡張子を取得
        if not extension.lower() in VALID_EXTENSIONS:
            raise forms.ValidationError('jpgファイルを選択してください！')
        return image