from django import template

register = template.Library()

stop_list = ['редиска', 'фуфло', 'косяк', 'фигня']


@register.filter()
def censor(value):
    try:
        if not isinstance(value, str):
            raise AttributeError("Ошибка! Вы применяете фильтр не к строковому типу данных.")
        value = value.split()
        for i, word in enumerate(value):
            if any(stor_word in word for stor_word in stop_list):
                value[i] = word[0] + "".join('*' if cen.isalpha() else cen for cen in word)
                value[i] = value[i].replace('*', '', 1)
        return " ".join(value)
    except TypeError:
        print('Error')