
# Stock Analysis Tool

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

The **Stock Analysis Tool** is a web application built with Streamlit that allows users to analyze stock data. It provides key metrics, historical price charts, and moving averages for selected stocks. The app fetches real-time stock data using the `yfinance` library and visualizes it using Plotly.

---

## Features

- **Search and Select Stocks**: Search for popular stocks by symbol or name.
- **Key Metrics**: View important financial metrics such as Market Cap, P/E Ratio, Dividend Yield, and more.
- **Historical Price Chart**: Visualize the stock's price movement over time.
- **Moving Averages**: Analyze trends using moving averages.
- **Real-Time Updates**: Toggle real-time price updates (placeholder functionality).
- **Responsive Design**: Built with Streamlit for a seamless user experience.

---

## Screenshots

![Stock Analysis Tool Screenshot](screenshots/screenshot.png)  
*Example: Analyzing Apple Inc. (AAPL) stock.*

---

## Installation

Follow these steps to set up and run the Stock Analysis Tool on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rebel47/Stock-Analysis-Tool.git
   cd stock-analysis-tool
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

5. **Access the App**:
   Open your browser and navigate to `http://localhost:8501`.

---

## Usage

1. **Search for a Stock**:
   - Type the stock symbol or name (e.g., `AAPL`, `Microsoft`) in the search bar.
   - Select a stock from the dropdown list.

2. **Select a Time Period**:
   - Choose a time period (e.g., `1mo`, `1y`, `5y`) to view historical data.

3. **View Key Metrics**:
   - The app displays key financial metrics for the selected stock.

4. **Explore Charts**:
   - View the historical price chart and moving averages.

5. **Enable Real-Time Updates** (placeholder):
   - Toggle the "Enable real-time updates" checkbox to simulate real-time price updates.

---

## Technologies Used

- **Streamlit**: For building the web application.
- **yfinance**: For fetching stock data.
- **Plotly**: For creating interactive charts.
- **Pandas**: For data manipulation and analysis.

---

## File Structure

```
stock-analysis-tool/
├── main.py                # Main application code
├── README.md              # Project documentation
├── requirements.txt       # List of dependencies
└── screenshots/           # Folder for screenshots
    └── screenshot.png     # Example screenshot
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework.
- [yfinance](https://pypi.org/project/yfinance/) for providing stock data.
- [Plotly](https://plotly.com/) for interactive charting.

---

## Contact

For questions or feedback, feel free to reach out:

