from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError(f"Цена не должна быть отрицательной")
        return price

    def clean_name(self):
        banned_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        name = self.cleaned_data.get("name")
        for banned_word in banned_words:
            if banned_word == name.lower():
                raise ValidationError(f"Недопустимые слова")
        return name

    def clean_description(self):
        banned_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        description = self.cleaned_data.get("description")
        for banned_word in banned_words:
            if banned_word == description.lower():
                raise ValidationError(f"Недопустимые слова")
        return description


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ["publication_status"]
