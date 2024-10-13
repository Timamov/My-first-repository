equipment1 = {
    'price': 1263400,
    'sale_price:': 1173400,
    'has_rear_LED_lights_with_dynamic_turn_indicators': False,
    'exterior_design': ['layers_on_the_roof', 'protective_cover_on_the_bumper',
    'additional_tining_of_rear_windows', 'Alloy wheels 2-color 18'' new design with diamond grinding',
    'metallic_paint'],
    'panoramic_glass_roof_with_hatch': {},
    'cruise_control': True,
    'airbag': True,
    'automatic_parking_help': False,
    'controlling_blind_zones_system': True,
    'rear_view_camera': True,
}
exterior_design_print_equipment1 = equipment1['exterior_design']
for element in exterior_design_print_equipment1:
    print(element)

equipment2 = {
    'price': 1263400,
    'sale_price:': 1173400,
    'has_rear_LED_lights_with_dynamic_turn_indicators': True,
    'exterior_design': ['layers_on_the_roof', 'protective_cover_on_the_bumper',
    'additional_tining_of_rear_windows', 'Alloy wheels 2-color 18'' new design with diamond grinding',
    'metallic_paint', 'special_black_amethyst_paint'],
    'panoramic_glass_roof_with_hatch': {'price': 29486},
    'cruise_control': True,
    'airbag': True,
    'automatic_parking_help': True,
    'controlling_blind_zones_system': True,
    'rear_view_camera': True,
}
exterior_design_print_equipment2 = equipment2['exterior_design']
for element in exterior_design_print_equipment2:
    print(element)

information_about_panoramic_glass_roof_with_hatch = equipment2['panoramic_glass_roof_with_hatch']
print(information_about_panoramic_glass_roof_with_hatch)
obj = {
    'Ukraine': 1_2_000
}
