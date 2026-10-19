import pytest
from shipping import shipping_fee

# Rule 1: weight must be > 0, otherwise ValueError
# FAILS: code breaks Rule 1. Weight 0 should raise ValueError ("more than 0 kg"), but the code only rejects weight < 0.
@pytest.mark.parametrize("weight", [0, -0.5, -10])
def test_rule1_non_positive_weight_is_rejected(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)

# Rule 2: up to and including 1 kg costs 40
# FAILS: code breaks Rule 2. Exactly 1 kg should cost 40 ("up to 1 kg"), but the code returns 60 because it uses weight < 1 instead of <= 1.
@pytest.mark.parametrize("weight, fee", [
    (0.1, 40),  
    (0.5, 40),   
    (1, 40),     
])
def test_rule2_up_to_1kg(weight, fee):
    assert shipping_fee(weight) == fee

# Rule 3: more than 1 kg and up to and including 5 kg costs 60
@pytest.mark.parametrize("weight, fee", [
    (1.1, 60),  
    (3, 60),     
    (5, 60),   
])
def test_rule3_over_1kg_up_to_5kg(weight, fee):
    assert shipping_fee(weight) == fee

# Rule 4: more than 5 kg costs 60 + 10 per started kg above 5
# FAILS: code breaks Rule 4. Every *started* kg above 5 should add 10 baht, but the code uses int(), which rounds down (5.2 -> 0 extra, 6.1 -> 1 extra).
@pytest.mark.parametrize("weight, fee", [
    (5.2, 70),   
    (6, 70),    
    (6.1, 80),   
    (7.5, 90),  
])
def test_rule4_over_5kg(weight, fee):
    assert shipping_fee(weight) == fee