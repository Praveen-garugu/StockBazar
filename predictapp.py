import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, SimpleRNN, Dense
from sklearn.metrics import mean_squared_error
import plotly.express as px
from sklearn.metrics import r2_score
import plotly.graph_objects as go
def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    short_ema = data['Close'].ewm(span=short_period, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_period, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram
def macd(stock_data,stock_symbol):
    stock_data['MACD'], stock_data['Signal Line'], stock_data['Histogram'] = calculate_macd(stock_data)

    # Create the candlestick trace
    candlestick_trace = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name='Candlesticks'
    )

    # Create the MACD and Signal Line traces
    macd_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['MACD'],
        mode='lines',
        name='MACD'
    )

    signal_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['Signal Line'],
        mode='lines',
        name='Signal Line'
    )

    # Create the figure
    fig = go.Figure(data=[candlestick_trace, macd_trace, signal_trace])
    fig.update_layout(
        title=f'Candlestick Chart with MACD for {stock_symbol}',
        yaxis_title='Price / MACD',
        xaxis_rangeslider_visible=False
    )

# Show the plot
    st.plotly_chart(fig)

def rsiindex(stock_data,stock_symbol):
    stock_data['RSI'] = calculate_rsi(stock_data)

    # Create the candlestick trace
    candlestick_trace = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name='Candlesticks'
    )

    # Create the RSI trace
    rsi_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['RSI'],
        mode='lines',
        name='RSI'
    )

    # Create the figure
    fig = go.Figure(data=[candlestick_trace, rsi_trace])
    fig.update_layout(
        title=f'Candlestick Chart with RSI for {stock_symbol}',
        yaxis_title='Price / RSI',
        xaxis_rangeslider_visible=False
    )

    # Show the plot
    st.plotly_chart(fig)

def smaema(stock_data,stock_symbol):
    stock_data['SMA20'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['SMA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['EMA20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()
    stock_data['EMA50'] = stock_data['Close'].ewm(span=50, adjust=False).mean()

    # Create the candlestick trace
    candlestick_trace = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name='Candlesticks'
    )

    # Create the moving averages traces
    sma20_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['SMA20'],
        mode='lines',
        name='SMA20'
    )

    sma50_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['SMA50'],
        mode='lines',
        name='SMA50'
    )

    ema20_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['EMA20'],
        mode='lines',
        name='EMA20'
    )

    ema50_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['EMA50'],
        mode='lines',
        name='EMA50'
    )

    # Create the figure
    fig = go.Figure(data=[candlestick_trace, sma20_trace,ema20_trace])
    fig.update_layout(
        title=f'Candlestick Chart with Moving Averages and Exponential Averages for {stock_symbol}',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )

    # Show the plot
    st.plotly_chart(fig)
def obv(stock_data,stock_symbol):
    stock_data['OBV'] = ((stock_data['Close'] - stock_data['Open']) / stock_data['Open']) * stock_data['Volume']
    stock_data['OBV'] = stock_data['OBV'].cumsum()

    # Create the candlestick trace
    candlestick_trace = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name='Candlesticks'
    )

    # Create the OBV trace
    obv_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['OBV'],
        mode='lines',
        name='OBV'
    )

    # Create the figure
    fig = go.Figure(data=[candlestick_trace, obv_trace])
    fig.update_layout(
        title=f'Candlestick Chart with On-Balance Volume (OBV) for {stock_symbol}',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )

    # Show the plot
    st.plotly_chart(fig)
def rsithreshold(stock_data,stock_symbol):
    stock_data['RSI'] = calculate_rsi(stock_data, period=14)

    # Set RSI overbought and oversold thresholds
    overbought_threshold = 70
    oversold_threshold = 30

    # Create the candlestick trace
    candlestick_trace = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        name='Candlesticks'
    )

    # Create the RSI trace
    rsi_trace = go.Scatter(
        x=stock_data.index,
        y=stock_data['RSI'],
        mode='lines',
        name='RSI'
    )

    # Create horizontal lines for overbought and oversold thresholds
    overbought_line = go.Scatter(
        x=stock_data.index,
        y=[overbought_threshold] * len(stock_data),
        mode='lines',
        line=dict(color='red', width=1, dash='dash'),
        name='Overbought Threshold'
    )

    oversold_line = go.Scatter(
        x=stock_data.index,
        y=[oversold_threshold] * len(stock_data),
        mode='lines',
        line=dict(color='green', width=1, dash='dash'),
        name='Oversold Threshold'
    )

    # Create the figure
    fig = go.Figure(data=[candlestick_trace, rsi_trace, overbought_line, oversold_line])
    fig.update_layout(
        title=f'Candlestick Chart with Relative Strength Index (RSI) for {stock_symbol}',
        yaxis_title='Price / RSI',
        xaxis_rangeslider_visible=False
    )

    # Show the plot
    st.plotly_chart(fig)
def stockPredict():
    st.title('Stock Price Prediction')

    # Sidebar
    stock_symbol = st.sidebar.text_input('Enter Stock Symbol (e.g., AAPL)', value='AAPL', max_chars=5)
    look_back = st.sidebar.slider('Number of Previous Days to Consider', min_value=1, max_value=30, value=10)
    period=st.sidebar.selectbox('Select a period',options=['1y','2y','3y','4y','5y','10y'])
    algorithm = st.sidebar.selectbox('Select Algorithm', ['LSTM', 'GRU', 'RNN'])
    # Load data using yfinance

    def load_data(symbol,period):
        data = yf.download(symbol, period=period)
        return data

    stock_data = load_data(stock_symbol,period)
    st.write(f"Displaying data for: {stock_symbol}")
    st.table(stock_data[::-1].head())
    st.subheader(':blue[Different Technical Indicators for the prediction]')
    leftgraph,rightgraph=st.columns(2)
    with leftgraph:
        # Calculate moving averages and exponential moving average
        stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
        stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()
        stock_data['EMA_20'] = stock_data['Close'].ewm(span=20, adjust=False).mean()

        # Create the candlestick trace
        candlestick_trace = go.Candlestick(
            x=stock_data.index,
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close'],
            name='Candlesticks'
        )

        # Create moving average traces
        sma_50_trace = go.Scatter(
            x=stock_data.index,
            y=stock_data['SMA_50'],
            mode='lines',
            name='SMA 50'
        )

        sma_200_trace = go.Scatter(
            x=stock_data.index,
            y=stock_data['SMA_200'],
            mode='lines',
            name='SMA 200'
        )

        ema_20_trace = go.Scatter(
            x=stock_data.index,
            y=stock_data['EMA_20'],
            mode='lines',
            name='EMA 20'
        )

        # Create the figure
        fig = go.Figure(data=[candlestick_trace, sma_50_trace, sma_200_trace, ema_20_trace])
        fig.update_layout(
            title=f'Candlestick Chart with Moving Averages for {stock_symbol}',
            yaxis_title='Price',
            xaxis_rangeslider_visible=False
        )

        # Show the plot
        st.plotly_chart(fig)
        rsiindex(stock_data,stock_symbol)
        obv(stock_data,stock_symbol)
    with rightgraph:
        smaema(stock_data,stock_symbol)
        macd(stock_data,stock_symbol)
        rsithreshold(stock_data,stock_symbol)
    # Data preprocessing
    closing_prices = stock_data['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(closing_prices)

    # Create sequences for prediction
    X = []
    y = []
    for i in range(len(scaled_prices) - look_back):
        X.append(scaled_prices[i:i+look_back])
        y.append(scaled_prices[i+look_back])
    X = np.array(X)
    y = np.array(y)

    # Split stock_data into training and testing sets
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    if algorithm=='LSTM':
    # LSTM model
        lstm_model = Sequential()
        lstm_model.add(LSTM(50, activation='relu', input_shape=(look_back, 1)))
        lstm_model.add(Dense(1))
        lstm_model.compile(optimizer='adam', loss='mse')
        lstm_model.fit(X_train, y_train, epochs=10)
        model = lstm_model
    # GRU model
    if algorithm=='GRU':
        gru_model = Sequential()
        gru_model.add(GRU(50, activation='relu', input_shape=(look_back, 1)))
        gru_model.add(Dense(1))
        gru_model.compile(optimizer='adam', loss='mse')
        gru_model.fit(X_train, y_train, epochs=10)
        model = gru_model
    # Simple RNN model
    if algorithm=='RNN':
        rnn_model = Sequential()
        rnn_model.add(SimpleRNN(50, activation='relu', input_shape=(look_back, 1)))
        rnn_model.add(Dense(1))
        rnn_model.compile(optimizer='adam', loss='mse')
        rnn_model.fit(X_train, y_train, epochs=10)
        model = rnn_model
    # Streamlit App
    if st.button('Predict'):
        pred=model.predict(X_test)
        pred=scaler.inverse_transform(pred)
        df=pd.DataFrame(scaler.inverse_transform(y[train_size:]),columns=['Actual'],index=stock_data.index[-y_test.shape[0]-1:-1:])
        df['Predicted']=pred
        st.header(f'The predicted vs Actual values by {algorithm}')
        st.table(df.tail())
        st.subheader(f'Graphical representation of the tested and trained results by {algorithm}')
        st.plotly_chart(px.line(df,title='Actual vs Predicted'))
        last_sequence = scaled_prices[-look_back:].reshape(1, look_back, 1)
        prediction = model.predict(last_sequence)
        predicted_price = scaler.inverse_transform(prediction)[0][0]
        st.subheader(f'Predicted Next Day\'s Closing Price using {algorithm}: :blue[{predicted_price:.2f}]')
        
#stockPredict()