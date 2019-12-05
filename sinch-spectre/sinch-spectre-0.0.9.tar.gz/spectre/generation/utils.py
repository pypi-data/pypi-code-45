import os
import re
import copy

def make_form(entity):
    form = copy.deepcopy(entity)
    fields = form['fields']
    for field in fields:
        if is_id(field['name']):
            fields.remove(field)
            break
    return form

def is_id(field_name):
    id_pattern = r'(?:^(?:uu|gu)?id.*|.*(?:uu|gu)?id$)'
    if re.match(id_pattern, field_name):
        return True
    else:
        return False

def get_form_name(ent_name):
    return ent_name + '_form'

def to_pascal(text):
    words = text.split('_')
    output = []
    for word in words:
        output.append(word[0].upper() + word[1:])
    return ''.join(output)

def write_to_file(content, outfile):

    out_dir = 'out'

    def get_file_path(outfile):
        path = f'{out_dir}/{outfile}'
        path = os.path.abspath(path)
        return path

    def make_directory(file_path):
        dirpath = os.path.dirname(file_path)
        if not os.path.isdir(dirpath):
            os.makedirs(dirpath)

    file_path = get_file_path(outfile)
    make_directory(file_path)
    try:
        with open(file_path, 'w') as outfile:
            outfile.write(content)
    except:
        print(f'I/O error while writing {file_path}')