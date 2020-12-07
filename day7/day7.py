import re
from operator import concat
from functools import reduce


# Primera parte
print('==================== PRIMERA PARTE ====================')

rules = []
with open('sample_input.txt') as input:
    for r in input:
        r_sep = re.sub(r' |bags?|\d+|\.', '', r.strip()).split('contain')            
        rules.append((r_sep[0], r_sep[1].split(',') if r_sep[1] != 'noother' else []))

def get_bag_colors_1_level(color):
    parents = []
    for rule in rules:
        if color in rule[1]:
            parents.append(rule[0])
    return parents

def get_bag_colors(color):

    colors_1_level = get_bag_colors_1_level(color)
    if not colors_1_level:
        return []
    else:
        return colors_1_level + reduce(concat, map(get_bag_colors, colors_1_level))

print(len(set(get_bag_colors('shinygold'))))

    
# Segunda parte
print('==================== SEGUNDA PARTE ====================')

def split_num_color(num_color):
    num = re.search(r'^\d+', num_color)
    if num:
        return (int(num_color[num.span()[0]:num.span()[1]]), num_color[num.span()[1]:])
    else:
        return (0, num_color)

def num_bags_containing(color):
    try:
        rule = next(filter(lambda r: r[0] == color, rules))
    except:
        return 0

    if not rule[1]:
        return 0
    
    return sum(map(lambda bc: bc[0] + bc[0] * num_bags_containing(bc[1]), rule[1]))


rules = []
with open('input.txt') as input:
    for r in input:
        r_sep = re.sub(r' |bags?|\.', '', r.strip()).split('contain')
        bags_inside = [split_num_color(bi) for bi in (r_sep[1].split(',') if r_sep[1] != 'noother' else [])]
        rules.append((r_sep[0], bags_inside))


print(num_bags_containing('shinygold'))
        