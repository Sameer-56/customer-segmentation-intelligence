import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Page configuration
st.set_page_config(
    page_title="Customer Segmentation Intelligence",
    page_icon="🎯",
    layout="wide"
)

# Load saved artifacts
scaler = joblib.load('scaler.pkl')
kmeans = joblib.load('kmeans_model.pkl')

# Persona definitions matching model training
CLUSTER_DETAILS = {
    0: {
        "title": "Affluent / High-Value Spender",
        "color": "green",
        "description": "High disposable income and top-tier spending across categories with minimal household dependents.",
        "strategy": "Promote premium reserve wines, exclusive gold/luxury bundles, loyalty concierge, and VIP event access."
    },
    1: {
        "title": "Budget-Conscious Family",
        "color": "orange",
        "description": "Moderate earnings with multiple children and conservative discretionary basket sizes.",
        "strategy": "Deploy family bundle discounts, back-to-school offers, bulk deal promotions, and coupon incentives."
    },
    2: {
        "title": "Frugal / Entry-Level Shopper",
        "color": "red",
        "description": "Lowest household income and lowest cumulative spending; primarily value-seeking.",
        "strategy": "Target with flash sales, clearanced-item alerts, seasonal promotional drives, and essential goods."
    },
    3: {
        "title": "Established / Mature Moderate Spender",
        "color": "blue",
        "description": "Older demographic with solid income and consistent mid-to-high spending.",
        "strategy": "Direct catalog marketing, emphasis on customer service quality, and fine dining/produce recommendations."
    }
}

st.title("🎯 Customer Segmentation & Targeting App")
st.markdown("Enter customer attributes to classify their segment, inspect persona positioning, and generate marketing recommendations.")

st.divider()

# Input layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Customer Age", min_value=18, max_value=90, value=45)
    income = st.number_input("Annual Household Income ($)", min_value=1000.0, max_value=200000.0, value=50000.0, step=1000.0)

with col2:
    total_spent = st.number_input("Total Spending Across Products ($)", min_value=0.0, max_value=3000.0, value=500.0, step=25.0)
    children = st.selectbox("Total Children at Home (Kids + Teens)", options=[0, 1, 2, 3, 4], index=1)

st.divider()

if st.button("Predict Customer Segment", type="primary"):
    # Create input DataFrame with exact training column names: ['Age', 'Income', 'total_Spent', 'Children']
    input_df = pd.DataFrame([[age, income, total_spent, children]], 
                            columns=['Age', 'Income', 'total_Spent', 'Children'])
    
    scaled_data = scaler.transform(input_df)
    cluster_id = int(kmeans.predict(scaled_data)[0])
    details = CLUSTER_DETAILS[cluster_id]

    st.subheader(f"Assigned Segment: :{details['color']}[{details['title']}] (Cluster {cluster_id})")

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.info(f"**Persona Profile:**\n\n{details['description']}")
    with res_col2:
        st.success(f"**Recommended Strategy:**\n\n{details['strategy']}")

    st.divider()
    st.subheader("📊 Customer Position in Segmentation Space")

    # Load baseline dataset to plot background cluster landscape
    try:
        df_raw = pd.read_csv('Customer_Segmentation.csv', sep='\t')
        df_bg = df_raw.dropna(subset=['Income']).copy()
        df_bg['total_Spent'] = (
            df_bg['MntWines'] + df_bg['MntFruits'] + df_bg['MntMeatProducts'] +
            df_bg['MntFishProducts'] + df_bg['MntSweetProducts'] + df_bg['MntGoldProds']
        )
        df_bg['Age'] = 2026 - df_bg['Year_Birth']
        df_bg['Children'] = df_bg['Kidhome'] + df_bg['Teenhome']
        df_bg = df_bg[(df_bg['Age'] < 90) & (df_bg['Income'] < 200000)]

        # Apply model to background data using exact training feature names
        features = ['Age', 'Income', 'total_Spent', 'Children']
        X_bg = scaler.transform(df_bg[features])
        df_bg['Cluster'] = kmeans.predict(X_bg)

        # Plot cluster scatter
        fig, ax = plt.subplots(figsize=(9, 4.5))
        sns.scatterplot(
            data=df_bg,
            x='Income',
            y='total_Spent',
            hue='Cluster',
            palette=['#2ca02c', '#ff7f0e', '#d62728', '#1f77b4'],
            alpha=0.35,
            s=25,
            ax=ax
        )

        # Plot current customer
        ax.scatter(
            [income],
            [total_spent],
            color='black',
            s=180,
            marker='X',
            label='Current Customer',
            edgecolor='white',
            linewidth=1.5
        )

        ax.set_title("Income vs. Total Spending Segmentation Distribution", fontsize=12)
        ax.set_xlabel("Annual Income ($)")
        ax.set_ylabel("Total Spending ($)")
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')

        st.pyplot(fig)
    except Exception as e:
        st.caption(f"Cluster visualization optional: {e}")
