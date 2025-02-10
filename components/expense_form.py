import streamlit as st
from datetime import datetime

def show_expense_form():
    """支出入力フォーム"""
    st.subheader("支出を記録")

    # カテゴリの選択肢
    categories = [
        "食費", "住居費", "光熱費", "通信費",
        "交通費", "娯楽費", "医療費", "教育費",
        "衣服費", "その他"
    ]

    with st.form("expense_form"):
        # 日付入力
        date = st.date_input(
            "日付",
            value=datetime.now(),
            key="expense_date"
        )

        # カテゴリ選択
        category = st.selectbox(
            "カテゴリ",
            options=categories,
            key="expense_category"
        )

        # 金額入力（円単位）
        amount_str = st.text_input(
            "金額（円）",
            value="",
            key="expense_amount"
        )

        # メモ入力
        memo = st.text_area(
            "メモ（任意）",
            key="expense_memo"
        )

        # 送信ボタン
        submitted = st.form_submit_button("記録する")

        if submitted:
            # 金額の検証
            try:
                amount = int(amount_str) if amount_str else 0
                if amount > 0:
                    return {
                        "日付": date,
                        "カテゴリ": category,
                        "金額": amount,
                        "メモ": memo
                    }
                else:
                    st.error("金額を入力してください。")
                    return None
            except ValueError:
                st.error("金額は整数で入力してください。")
                return None

    return None