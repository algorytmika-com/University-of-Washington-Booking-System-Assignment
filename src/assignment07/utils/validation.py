from cerberus import Validator
from datetime import datetime

def is_valid(value, option):
    if is_not_comma(input):
        if option == 'full_name':
            return is_full_name(value)
        elif option == 'true_false':
            return is_true_false(value)
        elif option == 'destination_country':
            return is_destination_country(value)  
        elif option == 'ssn':
            return is_ssn(value)          
        elif option == 'date_of_birth':
            return is_required_date(value)      
        elif option == 'job_title':
            return is_job_title(value)  
        elif option == 'start_date':
            return is_required_date(value)    
        elif option == 'end_date':
            return is_not_required_date(value)                 
        else:
            return False
    else:
        return False
    
def is_not_comma(input):
    schema = {'input': {'type' : 'string', 'contains' : ','}}
    v = Validator(schema)
    document = {'input' : input}
    return not v.validate(document)    
    
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




def is_job_title(input):
    schema = {'input': {'type' : 'string', 'minlength': 3}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_ssn(input):
    schema = {'input': {'type' : 'string',  'regex' : '^\d{3}-?\d{2}-?\d{4}$'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_required_date(input):
    if isinstance(input, str):
        format_str = '%m/%d/%Y'
        try:
            input = datetime.strptime(input, format_str)
        except ValueError:
            return False
    else:
        return False
    if isinstance(input, datetime):
        if input.date() > datetime.now().date():
            return False
        else:
            schema = {'input': {'type' : 'datetime'}}
            v = Validator(schema)
            document = {'input' : input}
            return v.validate(document)   
    else:
        return False
    
def is_not_required_date(input):
    if input == '':
        return True
    else:
        return is_required_date(input)