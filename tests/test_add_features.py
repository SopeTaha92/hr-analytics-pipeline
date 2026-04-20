


import pandas as pd
import pytest 
from src.features import add_features
from datetime import datetime

path_csv = "tests/out_put.csv"


def test_add_features():
    data = {
        'experience_years': [10, 5, 2],
        'salary': [79612, 79612, 79612],
        'bonus': [0.03, 0.03, 0.03],
        'hire_date': [pd.Timestamp('2010-02-18'), pd.Timestamp('2016-06-10'), pd.Timestamp('2020-01-01')]
    }

    fake_df = pd.DataFrame(data)

    result = add_features(fake_df)

    assert result['level'][0] == 'Expert'
    assert result['level'][1] == 'Sénior'
    assert result['level'][2] == 'Junior'
    assert result['bonus_amount'][0] == pytest.approx(79612*0.03)
    assert result['total_compensation'][0] == pytest.approx(79612+(79612*0.03))
    assert result['year_in_company'][0] == round((datetime.now() - pd.Timestamp('2010-02-18')).days / 365.25, 1)
    assert result['anciennete'][0] == 'Ancien'
    assert result['anciennete'][1] == 'Sénior'
    assert result['anciennete'][2] == 'Junior'
    assert result['annuel_compensation'][0] == pytest.approx((79612+(79612*0.03))*12)
    



    
