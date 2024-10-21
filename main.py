from util_email import send_email
import jinja2
user_info = {
    'name': 'Timur',
    'age': 12,
    'hobbies': [
        'IT',
        'basketball',
        'monopoly'
    ]

}
with open('user_welcome_letter.html', encoding='utf-8') as file:
    user_letter = file.read()
def render_html(html_path: str, params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(html_path)
    output = template.render(params)
    return output
send_email(
    ['timov31@ukr.net'],
    user_letter,
    'mail subject',
    'README.md'
)

send_email(
    ['timov31@ukr.net'],
    render_html('user_welcome_letter.html', user_info),
    'mail subject2',

)