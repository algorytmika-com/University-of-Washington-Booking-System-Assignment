from cerberus import Validator
from datetime import datetime

def is_valid(value, option):
    if option == 'full_name':
        return is_full_name(value)
    elif option == 'true_false':
        return is_true_false(value)
    elif option == 'destination_country':
        return is_destination_country(value) 
    elif option == 'description':
        return is_description(value)     
    elif option == 'positive_float':
        return is_positive_float(value)        
    elif option == 'future_date':
        return is_future_date(value)       
    else:
        print("The validation option not exists!!!")
        return False
    
def is_full_name(input):
    schema = {'input': {'type' : 'string', 'minlength': 5, 'regex' : r'[a-zA-Z \.]+'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_true_false(input):
    schema = {'input': {'type' : 'string', 'allowed' : ['y', 'n']}}
    v = Validator(schema)
    document = {'input' : input.lower()}
    return v.validate(document)       

def is_destination_country(input):
    schema = {'input': {'type' : 'string', 'minlength': 5, 'regex' : r'[a-zA-Z ]+'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_description(input):
    schema = {'input': {'type' : 'string', 'minlength': 3}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_positive_float(input):
    try:
        input = float(input)
    except ValueError:
        return False
    schema = schema = {'input': {'type' : 'float', 'empty': False, 'min' : 0}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)    

def is_future_date(input):
    if isinstance(input, str):
        format_str = '%m/%d/%Y'
        try:
            input = datetime.strptime(input, format_str)
        except ValueError:
            return False
    else:
        return False
    if isinstance(input, datetime):
        if input.date() < datetime.now().date():
            return False
        else:  
            schema = {'input': {'type' : 'datetime'}}
            v = Validator(schema)
            document = {'input' : input}
            return v.validate(document)   
    else:
        return False    
