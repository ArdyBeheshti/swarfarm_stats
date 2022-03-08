import json
import requests


def monster_stats(name):
    # getting the response from Swarfarm api for monsters
    response = requests.get(f'https://swarfarm.com/api/v2/monsters/?name={name}')

    # dump json response to pretty syntax
    # deserialize json object to return a dict
    json_encoded = json.dumps(response.json(), indent=4)
    json_decoded = json.loads(json_encoded)

    monster_comparison = {'name': [], 'element': [], 'base_hp': [], 'base_attack': [],
                          'crit_rate': [], 'crit_damage': [], 'resistance': [], 'accuracy': [],
                          'raw_hp': [], 'raw_attack': [], 'raw_defense': [], 'max_lvl_hp': [],
                          'max_lvl_attack': [], 'max_lvl_defense': []}

    for monster in json_decoded['results']:
        monster_comparison['name'].append(monster['name'])
        monster_comparison['element'].append(monster['element'])
        monster_comparison['base_hp'].append(monster['base_hp'])
        monster_comparison['base_attack'].append(monster['base_attack'])
        monster_comparison['crit_rate'].append(monster['crit_rate'])
        monster_comparison['crit_damage'].append(monster['crit_damage'])
        monster_comparison['resistance'].append(monster['resistance'])
        monster_comparison['accuracy'].append(monster['accuracy'])
        monster_comparison['raw_hp'].append(monster['raw_hp'])
        monster_comparison['raw_attack'].append(monster['raw_attack'])
        monster_comparison['raw_defense'].append(monster['raw_defense'])
        monster_comparison['max_lvl_hp'].append(monster['max_lvl_hp'])
        monster_comparison['max_lvl_attack'].append(monster['max_lvl_attack'])
        monster_comparison['max_lvl_defense'].append(monster['max_lvl_defense'])

    return monster_comparison


monster_list = monster_stats('Chakram Dancer')

monster_list

print('Collected monster variables!')


