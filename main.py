import streamlit as st
import pandas as pd
import yfinance as yf  # For fetching stock data
import plotly.express as px  # For creating charts

# Page configuration
st.set_page_config(
    page_title="Stock Analysis Tool",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS (inline instead of external file)
def load_custom_css():
    """Load custom CSS for styling."""
    custom_css = """
    <style>
    .stock-header {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .plot-container {
        margin-top: 1rem;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

load_custom_css()

# Sidebar
def render_sidebar():
    """Render the sidebar for stock search and options."""
    st.sidebar.title('Stock Analysis Tool')

    # Initialize session state for search and real-time updates
    if 'search_text' not in st.session_state:
        st.session_state.search_text = ''
    if 'auto_refresh' not in st.session_state:
        st.session_state.auto_refresh = False

    # Search input that updates session state
    search_text = st.sidebar.text_input(
        'Type to search stocks:',
        key='search_input',
        placeholder='Example: AAPL, Microsoft, NVDA',
        value=st.session_state.search_text
    )

    # Update session state
    st.session_state.search_text = search_text

    # Hardcoded popular stocks (replace with your own data)
    POPULAR_STOCKS = {
        'AAPL': 'Apple Inc.',
        'GOOGL': 'Alphabet Inc.',
        'MSFT': 'Microsoft Corporation',
        'AMZN': 'Amazon.com Inc.',
        'TSLA': 'Tesla Inc.',
        'NVDA': 'NVIDIA Corporation',
    }

    # Filter stock options based on search text
    filtered_options = [
        f"{symbol} - {name}" for symbol, name in POPULAR_STOCKS.items()
        if search_text.lower() in symbol.lower() or search_text.lower() in name.lower()
    ]

    # If no matches, show all options
    if not filtered_options and not search_text:
        filtered_options = [f"{symbol} - {name}" for symbol, name in POPULAR_STOCKS.items()]

    # Stock selection
    selected = st.sidebar.selectbox(
        'Select a stock:',
        options=filtered_options,
        index=0 if filtered_options else None,
        key='stock_selector'
    )

    # Extract symbol from selection
    symbol = selected.split(' - ')[0] if selected else ''

    # Time period selection
    period = st.sidebar.selectbox(
        'Select Time Period:',
        ['1mo', '3mo', '6mo', '1y', '2y', '5y'],
        index=3
    )

    # Real-time updates toggle (placeholder, no real-time functionality yet)
    st.sidebar.checkbox(
        'Enable real-time updates',
        key='auto_refresh',
        help='Updates price data every 5 seconds'
    )

    return symbol, period

# Fetch stock data using yfinance
def get_stock_data(symbol, period):
    """Fetch historical stock data and info using yfinance."""
    try:
        stock = yf.Ticker(symbol)
        hist_data = stock.history(period=period)
        stock_info = stock.info
        return hist_data, stock_info
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {str(e)}")
        return None, None

# Format large numbers (e.g., market cap)
def format_large_number(value):
    """Format large numbers into a readable format."""
    if isinstance(value, (int, float)):
        if value >= 1e12:
            return f"{value / 1e12:.2f}T"
        elif value >= 1e9:
            return f"{value / 1e9:.2f}B"
        elif value >= 1e6:
            return f"{value / 1e6:.2f}M"
        elif value >= 1e3:
            return f"{value / 1e3:.2f}K"
        else:
            return f"{value:.2f}"
    return value

# Get key metrics from stock info
def get_key_metrics(stock_info):
    """Extract key metrics from stock info."""
    metrics = {
        'Market Cap': stock_info.get('marketCap', 'N/A'),
        'P/E Ratio': stock_info.get('trailingPE', 'N/A'),
        'Dividend Yield': stock_info.get('dividendYield', 'N/A'),
        '52 Week High': stock_info.get('fiftyTwoWeekHigh', 'N/A'),
        '52 Week Low': stock_info.get('fiftyTwoWeekLow', 'N/A'),
    }
    return metrics

# Create a price chart using Plotly
def create_price_chart(hist_data):
    """Create a price chart using Plotly."""
    fig = px.line(hist_data, x=hist_data.index, y='Close', title='Stock Price Over Time')
    return fig

# Create a metrics chart (placeholder)
def create_metrics_chart(hist_data):
    """Create a metrics chart (e.g., moving averages)."""
    fig = px.line(hist_data, x=hist_data.index, y='Close', title='Moving Averages')
    return fig

# Main content
def render_main_content(symbol, period):
    """Render the main content based on the selected stock and period."""
    if symbol:
        with st.spinner(f'Loading data for {symbol}...'):
            try:
                # Fetch stock data
                hist_data, stock_info = get_stock_data(symbol, period)

                if hist_data is not None and stock_info is not None and len(hist_data) > 0:
                    # Stock Header
                    st.markdown('<div class="stock-header">', unsafe_allow_html=True)
                    col1, col2 = st.columns([2, 1])

                    with col1:
                        st.title(f"{stock_info.get('longName', symbol)}")
                        st.subheader(f"{stock_info.get('symbol', symbol)} - {stock_info.get('exchange', '')}")

                    with col2:
                        # Display current price and change
                        if len(hist_data) >= 2:
                            current_price = hist_data['Close'].iloc[-1]
                            price_change = current_price - hist_data['Close'].iloc[-2]
                            price_change_pct = (price_change / hist_data['Close'].iloc[-2]) * 100
                            st.metric(
                                "Current Price",
                                f"${current_price:.2f}",
                                f"{price_change:+.2f} ({price_change_pct:+.2f}%)"
                            )
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Key Metrics
                    st.subheader('Key Metrics')
                    metrics = get_key_metrics(stock_info)
                    cols = st.columns(3)
                    for i, (metric, value) in enumerate(metrics.items()):
                        with cols[i % 3]:
                            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                            st.metric(
                                metric,
                                format_large_number(value) if isinstance(value, (int, float)) else value
                            )
                            st.markdown('</div>', unsafe_allow_html=True)

                    # Charts
                    st.subheader('Price Chart')
                    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
                    price_chart = create_price_chart(hist_data)
                    st.plotly_chart(price_chart, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.subheader('Moving Averages')
                    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
                    metrics_chart = create_metrics_chart(hist_data)
                    st.plotly_chart(metrics_chart, use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                else:
                    st.error(f"Unable to fetch data for {symbol}. Please try another stock symbol.")
            except Exception as e:
                st.error(f"An error occurred while fetching data for {symbol}: {str(e)}")
    else:
        st.info("Start typing to search for stocks")

# Main execution
def main():
    """Main function to render the app."""
    symbol, period = render_sidebar()
    render_main_content(symbol, period)

if __name__ == "__main__":
    main()