from util_email import send_email
import requests
import jinja2


url = 'https://script.google.com/macros/s/AKfycbzqPlSA48GBjMpLu_Z4CfiOgD3-t3cHCODyQ0OacRoi5PBnXL1l6qyJamG0hV9Yw7w/exec'

response = requests.get(url)
response_json = response.json()
data: list[dict] = response_json['data']

cost = 0
for info in data:
    if info['Is_it_poisonous'] == True:
        cost += info['Price_for_keeping_on_eye']
        print(cost)
    elif info['Where_did_it_come_from'] == 'Africa':
        print(info)

most_expensive_animal = None
highest_cost = 0
for animal in data:
    if animal['Price_for_keeping_on_eye'] > highest_cost:
        most_expensive_animal = animal
        highest_cost = animal['Price_for_keeping_on_eye']

if most_expensive_animal:
    print(most_expensive_animal)
    print(highest_cost)

with open('hw13.html', encoding='utf-8') as file:
    zoo_info = file.read()

def render_html(html_path: str, params: dict) -> str:
    template_loader = jinja2.FileSystemLoader(searchpath='./')
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(html_path)
    output = template.render(params)
    return output
pass
params = {
    'animal_name': most_expensive_animal['Animal_name'],
    'animal_cost': most_expensive_animal['Price_for_keeping_on_eye'],
    'is_poisonous': most_expensive_animal['Is_it_poisonous']
}

output_html = render_html('hw13.html', params)
with open('hw13.html', 'w', encoding='utf-8') as file:
    file.write(output_html)


 
send_email(
        ['timov31@ukr.net'],
        output_html,
        'mail subject',
 )
