import streamlit as st
from utils.visualization import create_category_pie_chart, create_monthly_bar_chart
import pandas as pd

def show_data_view(df):
    """データ表示と可視化コンポーネント"""
    st.subheader("支出データの分析")

    # 期間選択
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("開始日", value=df['日付'].min())
    with col2:
        end_date = st.date_input("終了日", value=df['日付'].max())

    # フィルタリングされたデータフレーム
    filtered_df = df[(df['日付'] >= pd.Timestamp(start_date)) & 
                    (df['日付'] <= pd.Timestamp(end_date))]

    # タブで表示を切り替え
    tab1, tab2, tab3 = st.tabs(["支出一覧", "カテゴリ別分析", "月別推移"])

    with tab1:
        # 金額を見やすく整形
        display_df = filtered_df.copy()
        display_df['金額'] = display_df['金額'].apply(lambda x: f"¥{x:,}")

        st.dataframe(
            display_df.sort_values('日付', ascending=False),
            use_container_width=True
        )

        # 集計情報
        total_expense = filtered_df['金額'].sum()
        st.metric("期間中の総支出", f"¥{total_expense:,}")

    with tab2:
        # カテゴリ別の円グラフ
        pie_chart = create_category_pie_chart(filtered_df)
        st.plotly_chart(pie_chart, use_container_width=True)

        # カテゴリ別の集計表
        category_summary = filtered_df.groupby('カテゴリ')['金額'].agg(['sum', 'count']).reset_index()
        category_summary.columns = ['カテゴリ', '合計金額', '件数']
        # 金額をカンマ区切りで表示
        category_summary['合計金額'] = category_summary['合計金額'].apply(lambda x: f"¥{x:,}")

        st.dataframe(
            category_summary.sort_values('件数', ascending=False),
            use_container_width=True
        )

    with tab3:
        # 月別の棒グラフ
        bar_chart = create_monthly_bar_chart(filtered_df)
        st.plotly_chart(bar_chart, use_container_width=True)