from django import template

# from menu_drawer.models import

register = template.Library()

@register.inclusion_tag('menu_drawer/menu_tree.html', takes_context=True)
def draw_menu(context, menu_name):
    pass