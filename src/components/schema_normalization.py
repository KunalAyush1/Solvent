import sys
import pandas as pd
from datetime import datetime
from src.utils.logging import get_logger
from src.utils.exceptions import SolventException

logger = get_logger(__name__)

def normalize_schema(df: pd.DataFrame, start_date: datetime = datetime(2026, 1, 1)) -> tuple[pd.DataFrame, pd.DataFrame]:
    """ 
    Takes PaySim data, returns general transactions and transfer transactions
    both normalized to Solvent's Schema: date, amount, description, account_id, currency
    """
    try:
        logger.info("Normalizing PaySim data")
        df['date'] = pd.to_timedelta(df['step'], unit="hours") + start_date
        
        solvent_df = pd.DataFrame(columns=['date', 'amount', 'description', 'account_id', 'currency'])
        solvent_df['date'] = df['date']
        solvent_df['amount'] = df['amount']
        solvent_df['description'] = df['type']
        solvent_df['account_id'] = df['nameOrig']
        solvent_df['currency'] = 'USD'
        
        general_df = solvent_df[solvent_df['description'].isin(["PAYMENT", "CASH_OUT"])].copy()
        transfer_df = solvent_df[solvent_df['description'] == "TRANSFER"].copy()
        
        logger.info(f"Normalized {len(general_df)} general rows, {len(transfer_df)} transfer rows")
        return general_df, transfer_df
    
    except Exception as e:
        raise SolventException(e, sys) from e
        
        
    