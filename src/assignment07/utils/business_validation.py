from cerberus import Validator

def is_weight_business_rule(weight : float, message) -> bool:
    if weight > 0 and weight <= 10:
        return True
    else:
        print(message)
        return False