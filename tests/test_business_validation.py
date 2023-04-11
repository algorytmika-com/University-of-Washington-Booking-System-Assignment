from src.assignment07.utils import business_validation as b


def test_is_weight_business_rule_pass():
    assert b.is_weight_business_rule(0.01)
    assert b.is_weight_business_rule(3.1415)
    assert b.is_weight_business_rule(5)
    assert b.is_weight_business_rule(10)


def test_is_weight_business_rule_fail():
    assert not b.is_weight_business_rule(0)  
    assert not b.is_weight_business_rule(-1)
    assert not b.is_weight_business_rule(10.01)


def test_is_dimension_business_rule_pass():
    assert b.is_dimension_business_rule(0.01)
    assert b.is_dimension_business_rule(3.1415)
    assert b.is_dimension_business_rule(5)


def test_is_dimension_business_rule_fail():
    assert not b.is_dimension_business_rule(0)
    assert not b.is_dimension_business_rule(-1)
    assert not b.is_dimension_business_rule(5.01)
