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
