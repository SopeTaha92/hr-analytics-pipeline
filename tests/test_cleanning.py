

import pandas as pd
import pytest
from src.clean import cleaning_data


path_csv = "tests/out_put.csv"

def test_cleaning():
    data = {
        'employee_id' : ['EMP-001'],
        'full_name' : ['  Kevin Legrand  '],
        'department' : ['  R&d  '],
        'position' : ['  Research Scientist  '],
        'salary' : ['79612'],
        'experience_years' : [' 10 '],
        'hire_date' : ['2010-02-18'],
        'city' : [' Bordeaux '],
        'performance_rating' : ['a'],
        'bonus' : ['  3%  ']
    }
    fake_df = pd.DataFrame(data)

    result = cleaning_data(fake_df, path_csv)

    assert result['full_name'][0] == "Kevin Legrand"
    assert result['position'][0] == "Research Scientist"
    assert result['city'][0] == "Bordeaux"
    assert result['performance_rating'][0] == "A"
    assert result['department'][0] == "R&D" 
    assert result['salary'][0] == 79612
    assert result['experience_years'][0] == 10
    assert result['bonus'][0] == 0.03
    assert result['hire_date'][0] == pd.to_datetime('2010-02-18')