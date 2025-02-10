import streamlit as st
import pandas as pd
from datetime import datetime
from components.expense_form import show_expense_form
from components.data_view import show_data_view
from utils.data_handler import load_data, save_data

def main():
    st.set_page_config(
        page_title="家計簿アプリ",
        page_icon="💰",
        layout="wide"
    )

    # アプリケーションタイトル
    st.title("💰 家計簿アプリ")
    st.markdown("---")

    # サイドバーにアプリの説明を追加
    with st.sidebar:
        st.header("アプリについて")
        st.write("このアプリでは以下のことができます：")
        st.write("- 日々の支出を記録")
        st.write("- 支出の可視化と分析")
        st.write("- データのCSV保存と読み込み")

    # データの読み込み
    df = load_data()

    # 2カラムレイアウト
    col1, col2 = st.columns([1, 2])

    with col1:
        # 支出入力フォーム
        new_expense = show_expense_form()
        if new_expense:
            # 新しい支出を追加
            df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
            save_data(df)
            st.success("支出が記録されました！")

    with col2:
        # データ表示と可視化
        if not df.empty:
            show_data_view(df)
        else:
            st.info("支出データを入力してください。")

if __name__ == "__main__":
    main()
