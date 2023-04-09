from cerberus import Validator

def is_valid(value, option):
    if option == 'weight':
        return is_weight_business_rule(value)
    else:
        print("The validation option not exists!!!")
        return False

def is_weight_business_rule(weight : float) -> bool:
    if weight > 0 and weight <= 10:
        return True
    else:
        print("The weight is too big. Packages can only be shipped if they weigh less than 10Kg.")
        return False