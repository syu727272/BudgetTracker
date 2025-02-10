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

        # 金額入力の説明
        st.markdown("""
        ##### 金額入力
        - 入力は**千円単位**です（例：5千円なら「5」と入力）
        """)

        # 金額入力（千円単位）
        col1, col2 = st.columns([3, 1])
        with col1:
            amount_thousands = st.number_input(
                "金額（千円）",
                min_value=0,
                step=1,
                key="expense_amount",
                help="1 = 1,000円"
            )

        # 実際の金額を計算（円単位）
        amount = amount_thousands * 1000

        # 金額の確認表示
        if amount > 0:
            st.info(f"""
            💰 入力内容の確認
            - 入力値: {amount_thousands:,}（千円）
            - 実際の金額: ¥{amount:,}（円）
            """)

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