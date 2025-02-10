import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_category_pie_chart(df, start_date=None, end_date=None):
    """カテゴリ別の支出円グラフを作成"""
    if start_date and end_date:
        df = df[(df['日付'] >= start_date) & (df['日付'] <= end_date)]
    
    category_sum = df.groupby('カテゴリ')['金額'].sum().reset_index()
    
    fig = px.pie(
        category_sum,
        values='金額',
        names='カテゴリ',
        title='カテゴリ別支出割合',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def create_monthly_bar_chart(df):
    """月別支出の棒グラフを作成"""
    monthly_sum = df.set_index('日付').resample('M')['金額'].sum().reset_index()
    monthly_sum['月'] = monthly_sum['日付'].dt.strftime('%Y-%m')
    
    fig = px.bar(
        monthly_sum,
        x='月',
        y='金額',
        title='月別支出推移',
        color_discrete_sequence=['#FF4B4B']
    )
    fig.update_layout(
        xaxis_title='月',
        yaxis_title='支出額 (円)'
    )
    return fig
