# ✈️ Airline Financial Risk Analyzer  

🔗 **Live Demo** → [https://airline-financial-risk-analyzer.streamlit.app/]
---

## 📖 Overview  

Airline delays are not just an operational inconvenience — they also carry a **significant financial burden**.  
Flight delays can lead to compensation claims, higher operational costs, and reputational risks that directly impact an airline’s financial performance.  

This project introduces the **Airline Financial Risk Analyzer**, an **interactive Streamlit web application** designed to:  
- Analyze flight delays, passenger impacts, and financial risks.  
- Provide real-time insights with visual dashboards.  
- Demonstrate how data analytics can guide better decision-making in aviation risk management.  

By combining **Python, Pandas, and Streamlit**, this project showcases how raw airline delay data can be transformed into **actionable business insights**.  

---

## 📊 Features  

- 📈 **Delay Analysis** → Total delay, average delay, passenger impact.  
- 💸 **Financial Risk Insights** → Compensation loss, operational costs, insurance risks.  
- 🎨 **Interactive Dashboard** → Clean and modern Streamlit UI with cards and metrics.  
- 📂 **CSV Upload** → Easily replace or extend the dataset with your own airline delay data.  
- ☁️ **Deployment Ready** → Optimized for GitHub + Streamlit Cloud deployment.  

---

## 🖼️ Screenshots  

### Dashboard Overview  
 
  
<img width="1522" height="644" alt="image" src="https://github.com/user-attachments/assets/6ff78768-3062-4489-886c-7214b409647f" />

---

## 🏗️ Project Structure  

```
Airline-Financial-Risk-Analyzer/
│── app.py               # Main Streamlit app
│── utils.py             # Helper functions (data loading, metrics, calculations)
│── data/
│   └── sample_dataset.csv  # Sample airline delay dataset
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/Kulkarni-ui/Airline-Financial-Risk-Analyzer.git
cd Airline-Financial-Risk-Analyzer
```

### 2️⃣ Create a virtual environment (recommended)  
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app  
```bash
streamlit run app.py
```

---

## 🚀 Deployment  

### 🌐 Live App  
🔗 [Click here to try the app](https://airline-financial-risk-analyzer.streamlit.app/)  

### 🌐 Deploy on **Streamlit Cloud**  
1. Push your code to GitHub.  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).  
3. Connect your GitHub repo.  
4. Deploy → Done 🎉  

---

## 📊 Sample Dataset  

A sample dataset is provided in `data/sample_dataset.csv` with the following columns:  

| Airline   | FlightNumber | DepartureAirport | ArrivalAirport | DelayMinutes | Passengers | Date       |
|-----------|--------------|------------------|----------------|--------------|------------|------------|
| Vistara   | 8777         | BLR              | HYD            | 30           | 90         | 01-01-2023 |
| GoAir     | 1197         | CCU              | MAA            | 8            | 153        | 02-01-2023 |
| SpiceJet  | 8125         | MAA              | BOM            | 2            | 183        | 03-01-2023 |

You can replace it with **real-world datasets** for more insights.  

---

## 🛠️ Built With  

- [Python](https://www.python.org/) – Core programming language  
- [Pandas](https://pandas.pydata.org/) – Data analysis & manipulation  
- [Streamlit](https://streamlit.io/) – Interactive dashboard & deployment  

---

## 🤝 Contributing  

Contributions, issues, and feature requests are welcome!  
Feel free to open a PR or raise an issue.  

---

## 📜 License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  

---

## 👨‍💻 Author  

**Atharv Kulkarni**  
🔗 [GitHub](https://github.com/Kulkarni-ui) | 🌐 linkdin (https://www.linkedin.com/in/atharv-kulkarni-910785250/) | ✉️ Contact : 8850848258  

---
✨ _If you like this project, give it a ⭐ on GitHub!_
