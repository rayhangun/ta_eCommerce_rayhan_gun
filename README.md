# E-Commerce Data Analysis and Visualization Dashboard

This project involves analyzing and visualizing data from an e-commerce platform using Python. The key objectives include answering specific research questions, creating visualizations, and building a Streamlit dashboard for interactive data exploration.

---

## **Features**
- **Exploratory Data Analysis (EDA):**
  - Analyze customer satisfaction based on delivery times.
  - Investigate the relationship between product categories and payment methods.
  
- **Interactive Dashboard:**
  - Built with Streamlit for seamless exploration of insights.
  - Visualizes distribution of review scores, product sales, and payment method usage.

---

## **Files and Directories**
- `dashboard.py`: Main Streamlit application for the dashboard.
- `requirements.txt`: List of Python libraries required to run the project.
- `data/`: Directory containing the datasets used in this project.
- `README.md`: Documentation for the project.

---

## **Datasets**
The analysis uses multiple datasets related to an e-commerce platform:
1. **Order Items Dataset**: Details about individual items in orders.
2. **Order Reviews Dataset**: Customer reviews and satisfaction scores.
3. **Orders Dataset**: Metadata about orders.
4. **Order Payments Dataset**: Payment information.
5. **Customers Dataset**: Customer demographics and locations.
6. **Products Dataset**: Information about products and categories.
7. **Sellers Dataset**: Seller location and details.
8. **Product Category Translation Dataset**: Maps product category names to English translations.

---

## **Installation**

### **Prerequisites**
- Python 3.7+

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run dashboard.py
   ```

---

## **How to Use the Dashboard**
1. Open the Streamlit application in your browser.
2. Use the sidebar to navigate between different visualizations and filter options.
3. Explore insights such as:
   - Distribution of review scores.
   - Top product categories by sales.
   - Distribution of payment methods.

---

## **Key Insights**
1. **Customer Satisfaction and Delivery Times:**
   - Orders delivered on time tend to have higher satisfaction scores.
2. **Product Categories and Payment Methods:**
   - Credit cards dominate as the most used payment method across all product categories.

---

## **Dependencies**
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `streamlit`

---

## **Future Improvements**
- Add more detailed insights and visualizations.
- Enable additional filtering options on the dashboard.
- Deploy the dashboard on a cloud platform for public access.

---

## **Contributors**
- Rayhan Gunaningrat(https://github.com/rayhangun)

Feel free to fork this repository, open issues, or submit pull requests for suggestions and improvements!
