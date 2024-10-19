from util_email import send_email
import requests
import jinja2


url = 'https://script.googleusercontent.com/macros/echo?user_content_key=xHhBmCrj0B0DUKKFaByiPuDHtr41kEGhDUUspvtoxncJOcDpd-RiqU18imgPoShWW5PvOTyuPtVCxVFZiwhCYLma3BP4S5jAm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnNQGuJX8AREF9xUXhEgDIbPCZNp-XoumTYjFLBdleLR5GrTEPkKmZ5iOp2D5pmbqc3697XehTrJlc4nTBGwdfvmm6JqsHcHsmw&lib=M76dUUs45UzOi5zse8KSKohj_FdURCWWA'
response = requests.get(url)
response_json = response.json()
data: list[dict] = response_json['data']


cost = 0
for info in data:
    if info['Is it poisonous'] == True:
        cost += info['Price for keeping on eye']
        print(cost)
    elif info['Where did it come from'] == 'Africa':
        print(info)


with open('hw13.html', encoding='utf-8') as file:
    zoo_info = file.read()

def render_html(html_path: str, params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(html_path)
    output = template.render(params)
    return output


for info in data:
    send_email(
        ['timov31@ukr.net'],
        render_html('hw13.html', info),
        'mail subject',
    )
pass