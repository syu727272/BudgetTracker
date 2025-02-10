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

        # 金額入力（千円単位）
        st.markdown("##### 金額（千円単位）")
        amount = st.number_input(
            "",
            min_value=0,
            step=1,
            key="expense_amount",
            help="1単位 = 1,000円"
        ) * 1000  # 入力値を1000倍して保存

        # 現在の金額を表示
        if amount > 0:
            st.markdown(f"**入力金額: ¥{amount:,}**")

        # メモ入力
        memo = st.text_area(
            "メモ（任意）",
            key="expense_memo"
        )

        # 送信ボタン
        submitted = st.form_submit_button("記録する")

        if submitted:
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

    return None