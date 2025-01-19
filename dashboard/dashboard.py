import streamlit as st  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
  
# Load data  
@st.cache_data  
def load_data():  
    # Load the all_data.csv file  
    data = pd.read_csv("dashboard/all_data.csv")  
    return data  
  
data = load_data()  
  
# Sidebar for navigation  
st.sidebar.title("Navigation")  
options = st.sidebar.radio(  
    "Go to",  
    ["Home", "Review Scores", "Top Product Categories", "Payment Methods", "Insights"]  
)  
  
# Home Section  
if options == "Home":  
    st.title("E-Commerce Dashboard")  
    st.markdown("""  
    Selamat datang di dashboard E-Commerce Data Analysis!   
    Navigasikan melalui sidebar untuk eksplorasi data.  
    """)  
  
# Review Scores Section  
elif options == "Review Scores":  
    st.header("Distribution of Review Scores")  
    if "review_score" in data.columns:  
        review_scores = data["review_score"].value_counts().sort_index()  
        fig1, ax1 = plt.subplots()  
        sns.barplot(x=review_scores.index, y=review_scores.values, palette="viridis", ax=ax1)  
        ax1.set_title("Distribution of Review Scores")  
        ax1.set_xlabel("Review Score")  
        ax1.set_ylabel("Count")  
        st.pyplot(fig1)  
    else:  
        st.error("Column 'review_score' not found in the dataset.")  
  
# Top Product Categories Section  
elif options == "Top Product Categories":  
    st.header("Top 10 Product Categories by Sales")  
    if "product_category_name_english" in data.columns:  
        top_categories = data["product_category_name_english"].value_counts().head(10)  
  
        fig2, ax2 = plt.subplots()  
        top_categories.plot(kind="bar", color="skyblue", ax=ax2)  
        ax2.set_title("Top 10 Product Categories by Sales")  
        ax2.set_xlabel("Product Category")  
        ax2.set_ylabel("Number of Sales")  
        st.pyplot(fig2)  
    else:  
        st.error("Column 'product_category_name_english' not found in the dataset.")  
  
# Payment Methods Section  
elif options == "Payment Methods":  
    st.header("Distribution of Payment Methods")  
    if "payment_type" in data.columns:  
        payment_methods = data["payment_type"].value_counts(normalize=True) * 100  
        fig3, ax3 = plt.subplots()  
        payment_methods.plot(kind="pie", autopct="%.1f%%",   
                             colors=["#87CEFA", "#FFA07A", "#90EE90", "#FFB6C1"],   
                             ax=ax3)  
        ax3.set_title("Payment Method Distribution")  
        ax3.set_ylabel("")  # Remove y-label for pie chart  
        st.pyplot(fig3)  
    else:  
        st.error("Column 'payment_type' not found in the dataset.")  
  
# Insights Section  
elif options == "Insights":  
    st.header("Insights")  
    st.markdown("""  
    **1. Review Scores:**  
    - Mayoritas ulasan pelanggan memberikan skor 5 (sangat puas).  
  
    **2. Top Product Categories:**  
    - Kategori terlaris adalah "Cama, Mesa, Banho", diikuti oleh "Beleza, Saúde".  
    - Produk terkait rumah tangga dan kecantikan mendominasi penjualan.  
  
    **3. Payment Methods:**  
    - Kartu kredit digunakan dalam 73.3% transaksi.  
    - Metode "boleto" menjadi pilihan kedua dengan 19.3% dari transaksi.  
    """)  
  
# Footer  
st.sidebar.markdown("**Created with Streamlit by Rayhan Gunaningrat**")  