# Customer Segmentation & Marketing Intelligence System

An end-to-end Machine Learning and Business Analytics project that segments retail customers into behavioral personas using unsupervised learning, accompanied by an interactive Streamlit targeting dashboard.

## 📌 Project Architecture & Workflow
1. **Data Ingestion & Cleaning:** Loaded raw customer transaction and demographic records, resolved delimiter issues, handled missing attributes (`Income`), and filtered demographic outliers.
2. **Feature Engineering:** Derived consolidated behavioural indicators:
   - `Age` calculated from birth year.
   - `total_Spent` aggregated across all six merchandise lines (Wine, Fruits, Meat, Fish, Sweets, Gold).
   - `Children` consolidated from household dependent counts (`Kidhome` + `Teenhome`).
3. **Feature Scaling & Clustering:** Normalized features with `StandardScaler` to handle multi-scale variances. Optimized clusters using the **Elbow Method (WCSS Inertia)** at $k = 4$.
4. **Model Deployment:** Built an interactive web application with **Streamlit** to classify prospective or existing customers in real time and display tailored business strategies.

## 👥 Segment Personas & Strategy
| Cluster | Persona Title | Avg Income | Avg Spending | Household | Target Marketing Strategy |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | Affluent / High-Value | ~$77.1k | ~$1,430 | Few kids | High-margin items, fine wines, VIP concierge |
| **1** | Budget-Conscious Family | ~$43.6k | ~$209 | High kids (2+) | Family bundles, multi-buy discounts, essentials |
| **2** | Frugal / Value Seekers | ~$32.8k | ~$155 | 0–1 kids | Flash promotions, clearance sales, entry tier |
| **3** | Mature / Moderate-High | ~$62.4k | ~$821 | Empty-nesters | Direct catalog mailing, premium produce |

## 🛠️ Tech Stack
- **Language:** Python
- **Analytics & ML:** Scikit-Learn (`KMeans`, `StandardScaler`), Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit
- **Persistence:** Joblib

## 🚀 How to Run Locally

1. **Clone the repository and set up environment:**
   ```powershell
   git clone [https://github.com/Sameer-56/customer-segmentation-intelligence.git](https://github.com/Sameer-56/customer-segmentation-intelligence.git)
   cd customer_segmentation_project
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1# Customer Segmentation & Marketing Intelligence System

An end-to-end Machine Learning and Business Analytics project that segments retail customers into behavioral personas using unsupervised learning, accompanied by an interactive Streamlit targeting dashboard.

## 📌 Project Architecture & Workflow
1. **Data Ingestion & Cleaning:** Loaded raw customer transaction and demographic records, resolved delimiter issues, handled missing attributes (`Income`), and filtered demographic outliers.
2. **Feature Engineering:** Derived consolidated behavioural indicators:
   - `Age` calculated from birth year.
   - `total_Spent` aggregated across all six merchandise lines (Wine, Fruits, Meat, Fish, Sweets, Gold).
   - `Children` consolidated from household dependent counts (`Kidhome` + `Teenhome`).
3. **Feature Scaling & Clustering:** Normalized features with `StandardScaler` to handle multi-scale variances. Optimized clusters using the **Elbow Method (WCSS Inertia)** at $k = 4$.
4. **Model Deployment:** Built an interactive web application with **Streamlit** to classify prospective or existing customers in real time and display tailored business strategies.

## 👥 Segment Personas & Strategy
| Cluster | Persona Title | Avg Income | Avg Spending | Household | Target Marketing Strategy |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | Affluent / High-Value | ~$77.1k | ~$1,430 | Few kids | High-margin items, fine wines, VIP concierge |
| **1** | Budget-Conscious Family | ~$43.6k | ~$209 | High kids (2+) | Family bundles, multi-buy discounts, essentials |
| **2** | Frugal / Value Seekers | ~$32.8k | ~$155 | 0–1 kids | Flash promotions, clearance sales, entry tier |
| **3** | Mature / Moderate-High | ~$62.4k | ~$821 | Empty-nesters | Direct catalog mailing, premium produce |

## 🛠️ Tech Stack
- **Language:** Python
- **Analytics & ML:** Scikit-Learn (`KMeans`, `StandardScaler`), Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit
- **Persistence:** Joblib

## 🚀 How to Run Locally

1. **Clone the repository and set up environment:**
   ```powershell
   git clone https://github.com/Sameer-56/customer-segmentation-intelligence.git
   cd customer_segmentation_project
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1