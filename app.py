import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import io

# ----------------- APP CONFIG -----------------
st.set_page_config(page_title="Airline Financial Risk Analyzer", layout="wide")

# ----------------- CUSTOM CSS -----------------
st.markdown(
    """
    <style>
        body {background-color: #f4f6f9;}
        .title-card {
            padding: 20px;
            border-radius: 15px;
            background: linear-gradient(135deg, #1a73e8, #0d47a1);
            color: white;
            text-align: center;
            margin-bottom: 25px;
        }
        .title-card h1 {font-size: 38px; margin-bottom: 10px;}
        .title-card p {font-size: 16px; opacity: 0.9;}
        .stButton>button {
            background-color: #1a73e8;
            color:white; border-radius:10px; font-size:16px; padding:10px 20px;
        }
        .stButton>button:hover {background-color:#0d47a1; color:white;}
        
        /* Metric Cards */
        .metric-card {
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
            text-align: center;
            margin-bottom: 15px;
        }
        .metric-card h3 {margin-bottom:10px; font-size:20px;}
        .metric-card p {font-size:18px; font-weight:bold; margin:0;}
        
        /* Different colors for different metrics */
        .blue-card { background: #e3f2fd; }
        .green-card { background: #e8f5e9; }
        .yellow-card { background: #fffde7; }
        .orange-card { background: #fff3e0; }
        .red-card { background: #ffebee; }
        .purple-card { background: #f3e5f5; }
        
        .highlight-card {
            padding: 25px;
            border-radius: 15px;
            background: linear-gradient(135deg, #ff6b6b, #d32f2f);
            color: white;
            text-align: center;
            margin-top: 20px;
            font-size: 28px;
            font-weight: bold;
        }
        .section-divider {
            border-top: 2px solid #ddd;
            margin: 20px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- HEADER -----------------
st.markdown(
    """
    <div class="title-card">
        <h1> Airline Financial Risk Analyzer</h1>
        <p>💹 AI-powered Financial Risk Modeling for Airlines due to Flight Delays</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------- FILE UPLOAD -----------------
uploaded_file = st.file_uploader("📂 Upload your dataset (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Support both CSV and Excel
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Dataset uploaded successfully!")
        st.write("### Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)

        # ----------------- VALIDATION -----------------
        col_names = [c.lower() for c in df.columns]
        aviation_keywords = ["airline", "flight", "carrier", "delay", "dep", "arr", "minutes"]
        if not any(word in "".join(col_names) for word in aviation_keywords):
            st.error("This dataset does not look like an aviation dataset. Please upload aviation data.")
            st.stop()

        categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        if not categorical_cols or not numeric_cols:
            st.error("No valid columns found. Please check dataset.")
            st.stop()

        # ----------------- USER INPUTS -----------------
        st.markdown("### Select Columns for Analysis")
        airline_col = st.selectbox("Airline/Flight Column", categorical_cols)
        delay_col = st.selectbox("⏱Delay Column (minutes)", numeric_cols)
        passenger_col = st.selectbox("Passenger Column (optional)", ["None"] + numeric_cols)

        airline_choice = st.selectbox("Select Airline/Flight", df[airline_col].unique())

        st.markdown("### Financial Parameters")
        col1, col2, col3 = st.columns(3)
        with col1:
            COMPENSATION_RATE = st.number_input("Compensation Rate ($/passenger/hr)", 10, 200, 50)
        with col2:
            OPERATIONAL_COST_RATE = st.number_input("Operational Cost Rate ($/delay min)", 10, 500, 100)
        with col3:
            INSURANCE_MULTIPLIER = st.slider("Insurance Risk (% of operational cost)", 0.0, 0.2, 0.02)

        # ----------------- AI RISK PREDICTION -----------------
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
        st.subheader("AI Risk Prediction")

        if st.button(" Run AI Analysis"):
            try:
                X = pd.concat([df[[delay_col]], pd.get_dummies(df[airline_col], drop_first=True)], axis=1)
                y = ((df[delay_col] / 60) * 100 * COMPENSATION_RATE) + \
                    (df[delay_col] * OPERATIONAL_COST_RATE) + \
                    ((df[delay_col] * OPERATIONAL_COST_RATE) * INSURANCE_MULTIPLIER)

                model = LinearRegression()
                model.fit(X, y)

                avg_delay_selected = df[df[airline_col] == airline_choice][delay_col].mean()
                selected_X = pd.DataFrame([[avg_delay_selected]], columns=[delay_col])
                for col in X.columns:
                    if col not in selected_X.columns:
                        selected_X[col] = 0
                selected_X = selected_X.reindex(columns=X.columns, fill_value=0)

                predicted_risk = model.predict(selected_X).item()
                st.success(f"Predicted Financial Risk for {airline_choice}: **${round(predicted_risk,2)}**")
            except Exception as e:
                st.error(f"AI Analysis Error: {e}")

        # ----------------- FINANCIAL CALCULATIONS -----------------
        selected_data = df[df[airline_col] == airline_choice]
        total_delay = selected_data[delay_col].sum()
        avg_delay = selected_data[delay_col].mean()

        if passenger_col != "None":
            passengers = selected_data[passenger_col].sum()
            compensation = (total_delay / 60) * passengers * COMPENSATION_RATE
        else:
            flights = len(selected_data)
            passengers = flights * 100
            compensation = (total_delay / 60) * passengers * COMPENSATION_RATE

        operational_cost = total_delay * OPERATIONAL_COST_RATE
        insurance_risk = operational_cost * INSURANCE_MULTIPLIER
        total_risk = compensation + operational_cost + insurance_risk

        # ----------------- METRICS -----------------
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
        st.subheader(" Financial Risk Analysis")

        m1, m2, m3 = st.columns(3)
        with m1: st.markdown(f"<div class='metric-card blue-card'><h3>Total Delay</h3><p>{round(total_delay,2)} min</p></div>", unsafe_allow_html=True)
        with m2: st.markdown(f"<div class='metric-card green-card'><h3>Average Delay</h3><p>{round(avg_delay,2)} min</p></div>", unsafe_allow_html=True)
        with m3: st.markdown(f"<div class='metric-card yellow-card'><h3>Passengers</h3><p>{int(passengers)}</p></div>", unsafe_allow_html=True)

        m4, m5, m6 = st.columns(3)
        with m4: st.markdown(f"<div class='metric-card orange-card'><h3>Compensation Loss</h3><p>${round(compensation,2)}</p></div>", unsafe_allow_html=True)
        with m5: st.markdown(f"<div class='metric-card red-card'><h3>Operational Cost</h3><p>${round(operational_cost,2)}</p></div>", unsafe_allow_html=True)
        with m6: st.markdown(f"<div class='metric-card purple-card'><h3>Insurance Risk</h3><p>${round(insurance_risk,2)}</p></div>", unsafe_allow_html=True)

        st.markdown(f"<div class='highlight-card'>Total Financial Risk for {airline_choice}: ${round(total_risk,2)}</div>", unsafe_allow_html=True)

        # ----------------- RISK TABLE -----------------
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
        st.subheader("Airline-wise Risk Comparison")

        comparison = []
        for airline in df[airline_col].unique():
            temp = df[df[airline_col] == airline]
            td = temp[delay_col].sum()
            if passenger_col != "None":
                p = temp[passenger_col].sum()
                comp = (td / 60) * p * COMPENSATION_RATE
            else:
                comp = (td / 60) * len(temp) * 100 * COMPENSATION_RATE
            op = td * OPERATIONAL_COST_RATE
            ins = op * INSURANCE_MULTIPLIER
            tr = comp + op + ins
            comparison.append([airline, td, comp, op, ins, tr])

        comp_df = pd.DataFrame(comparison, columns=["Airline", "Total Delay (min)", "Compensation ($)", "Operational ($)", "Insurance ($)", "Total Risk ($)"])
        st.dataframe(comp_df, use_container_width=True)

        # Download button
        csv_buffer = io.StringIO()
        comp_df.to_csv(csv_buffer, index=False)
        st.download_button("📥 Download Risk Report (CSV)", data=csv_buffer.getvalue(), file_name="airline_risk_report.csv", mime="text/csv")

        # ----------------- CHART -----------------
        st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
        st.subheader(" Visualization of Financial Risk")

        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(comp_df["Airline"], comp_df["Total Risk ($)"], color="#1a73e8", alpha=0.9)
        ax.set_ylabel("Total Risk ($)")
        ax.set_title("Airline-wise Financial Risk due to Delays")
        plt.xticks(rotation=30)

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 100, f"${int(yval)}", ha="center", va="bottom", fontsize=8)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error reading the dataset: {e}")

else:
    st.info("⬆️ Please upload a dataset to begin analysis.")
