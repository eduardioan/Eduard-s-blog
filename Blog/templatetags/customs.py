from django import template

register = template.Library()

@register.filter(name='string_to_list')
def string_to_list(value) -> list:
    return str(value).replace(" ", "").split(",")
@register.filter(name='extract_unique_tags_from_post')
def extract_unique_tags_from_post(posts) -> set:
    buffer = []
    for post in posts:
        for tag in string_to_list(post.tags):
            buffer.append(tag)
    unique = set(buffer)
    return unique

