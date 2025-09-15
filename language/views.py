from django.utils.translation import gettext as _
from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    context = {
        "greeting": _("Salom! Xush kelibsiz!"),
        "about": _("Bu bizning vebsaytimiz."),
        "change_language": _("Tilni o'zgartirish"),
        "help": _("Yordam"),
        "name": _("Ism"),
    } 
    return render(request, "index.html", context)


# core/views.py
from django.conf import settings
from django.shortcuts import redirect
from django.utils import translation
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def change_language(request):
    if request.method == 'POST':
        lang = request.POST.get('language', 'uz')
        translation.activate(lang)
        response = redirect(f'/{lang}/')
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
        return response