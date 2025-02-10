import pandas as pd
import os

def load_data():
    """CSVファイルからデータを読み込む"""
    try:
        if os.path.exists("data/expenses.csv"):
            df = pd.read_csv("data/expenses.csv")
            df['日付'] = pd.to_datetime(df['日付'])
            return df
        return pd.DataFrame(columns=['日付', 'カテゴリ', '金額', 'メモ'])
    except Exception as e:
        print(f"データ読み込みエラー: {e}")
        return pd.DataFrame(columns=['日付', 'カテゴリ', '金額', 'メモ'])

def save_data(df):
    """データをCSVファイルに保存"""
    try:
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/expenses.csv", index=False)
    except Exception as e:
        print(f"データ保存エラー: {e}")
