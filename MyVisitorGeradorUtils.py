def getType(fieldType):
        switcher = {
            'string': 'Char',
            'number': 'Integer',
            'float': 'Decimal'
        }
        return switcher.get(fieldType, 'Invalid type')

def listModels(models):
    string = ''
    for index, model in enumerate(models):
        string = string + model.Id().getText()
        if index != len(models) -1:
            string = string + ', '
    return string

def listSerializers(models):
    string = ''
    for index, model in enumerate(models):
        string = string + model.Id().getText() + 'Serializer'
        if index != len(models) -1:
            string = string + ', '
    return string

def listFields(fields):
    string = ''
    for index, field in enumerate(fields):
        string = string + '"' + field.fieldName.text + '"'
        if index != len(fields) -1:
            string = string + ', '
    return string

def alterar_linha(file_name, line_num, text):
    with open(file_name,'r') as f:
        get_all=f.readlines()
    with open(file_name,'w') as f:
        for i,line in enumerate(get_all,1):    
            if i == line_num:
                f.writelines(text)
            else:
                f.writelines(line)

def nova_linha(file_name, line_num, text):
    with open(file_name,'r') as f:
        get_all=f.readlines()
    if not text in get_all:
        get_all.insert(line_num, text)
    with open(file_name,'w') as f:
        for i,line in enumerate(get_all,1):
            f.writelines(line)