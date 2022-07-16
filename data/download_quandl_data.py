import quandl
from settings.default import ALL_QUANDL_CODES
import datetime as dt
import pytse_client as tse
import argparse
import os

DEPTH = 1


base_path = os.path.join("data", "tse")

def main(tickers : list):
    tse.download(tickers, adjust= True, base_path=base_path, write_to_csv=True)
    return


if __name__ == "__main__":
    main()
