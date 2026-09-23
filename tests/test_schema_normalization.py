import pandas as pd
from datetime import datetime
from src.components.schema_normalization import normalize_schema

def test_schema_normalization():
    sample = pd.DataFrame({
        'step': [1, 2, 3, 4],
        'type': ['PAYMENT', 'CASH_OUT', 'TRANSFER', 'CASH_IN'],
        'amount': [100, 200, 300, 400],
        'nameOrig': ['A', 'B', 'C', 'D']
    })
    
    general_df, transfer_df = normalize_schema(sample)
    
    assert len(general_df) == 2
    assert len(transfer_df) == 1
    assert "TRANSFER" not in general_df['description'].values