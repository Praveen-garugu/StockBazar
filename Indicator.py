import streamlit as st
def indicate():
    st.subheader(':blue[Moving Average]')
    st.write('''
    It is widely used technical indicators used to identify the trends or patterns in data mostly used in time series data.The most common applications of moving averages are to identify trend direction and to determine support and resistance levels.When asset prices cross over their moving averages, it may generate a trading signal for technical traders.Choose the window size (period) for the moving average. 
    In this case, we're using a 5-dsay window.
    1)Start at the beginning of the dataset.
    2)Take the sum of the closing prices for the first 5 days.
    3)Divide the sum by the window size (5) to calculate the average.
    4)Move the window one day forward (slide it by one data point) and repeat steps 3 and 4.
    5)Continue moving the window and calculating the average until you've covered all the data points.
    ''')
    st.subheader(':blue[Simple Moving Average]')
    st.write('''
    A simple moving average (SMA) calculates the average of a selected range of prices, usually closing prices, by the number of periods in that range.
    it is a technical indicator that can aid in determining if an asset price will continue or if it will reverse a bull or bear trend.
    SMA=(a1+a2+a3.....an)/n
    An=the price of an asset at period n
    n=the number of total periods.
    ''')
    st.subheader(':blue[Exponential Moving Average]')
    st.write('''
    An exponential moving average (EMA) is a type of moving average (MA) that places a greater weight and significance on the most recent data points. The exponential moving average is also referred to as the exponentially weighted moving average. An exponentially weighted moving average reacts more significantly to recent price changes than a simple moving average,which applies an equal weight to all observations in the period.
    Like all moving averages, this technical indicator is used to produce buy and sell signals based on crossovers and divergences from the historical average.
    Traders often use several different EMA lengths, such as 10-day, 50-day, and 200-day moving averages.
    EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier).
    ''')
    st.subheader(':blue[Moving Average Convergence Divergence (MACD)]')
    st.write('''
    Moving average convergence/divergence (MACD, or MAC-D) is a trend-following momentum indicator that shows the relationship between two exponential moving averages (EMAs) of a security’s price. The MACD line is calculated by subtracting the 26-period EMA from the 12-period EMA.
    The result of that calculation is the MACD line. A nine-day EMA of the MACD line is called the signal line, which is then plotted on top of the MACD line, which can function as a trigger for buy or sell signals. Traders may buy the security when the MACD line crosses above the signal line and sell—or short—the security when the MACD line crosses below the signal line.
    The moving average convergence/divergence (MACD, or MAC-D) line is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA. The signal line is a nine-period EMA of the MACD line.
    MACD is best used with daily periods, where the traditional settings of 26/12/9 days is the default.
    MACD triggers technical signals when the MACD line crosses above the signal line (to buy) or falls below it (to sell).
    MACD can help gauge whether a security is overbought or oversold, alerting traders to the strength of a directional move, and warning of a potential price reversal.
    MACD=12-Period EMA(-)26-Period EMA.
    ''')
    st.subheader(':blue[Relative Strength Index]')
    st.write('''
    The relative strength index (RSI) is a momentum indicator used in technical analysis. RSI measures the speed and magnitude of a security's recent price changes to evaluate overvalued or undervalued conditions in the price of that security.
    The RSI is displayed as an oscillator (a line graph) on a scale of zero to 100.
    The RSI can do more than point to overbought and oversold securities. It can also indicate securities that may be primed for a trend reversal or corrective pullback in price. It can signal when to buy and sell. Traditionally, an RSI reading of 70 or above indicates an overbought situation. A reading of 30 or below indicates an oversold condition.
    On the other hand, RSI readings that cross below 50 show negative and downtrend momentum. If RSI is below 30, though, it indicates oversold conditions.
    ''')
    st.subheader(':blue[Average Directional Index]')
    st.write('''
    The Average Directional Index (ADX) created by Welles Wilder established the Directional Movement System, which consists of the ADX, the Minus Directional Indicator (-DI), and the Plus Directional Indicator (+DI).
    These indicators as a group are used to help measure both the momentum and the direction of price movements.
    Traders should note that the ADX values of 20 or higher indicate that the market is trending, and for any reading less than 20, the market is viewed as “directionless” or consolidated.
    ''')
    st.subheader(':blue[On-Balance indicator]')
    st.write('''
    it is the volume indicator that calculates the buying and selling pressure as a cumulative indicator which sums up the volume on up days and subtracts volume on down days.
    When the stock closes higher than the previous close, all of the day’s volume is considered up-volume. Similarly, when the stock closes lower than the previous close, then all of the day's volume is considered down-volume.
    When both prices, as well as OBV, are making higher peaks and higher troughs, then the upward trend
    When both prices, as well as OBV, are making lower peaks and lower troughs, then the downward trend.
    ''')
    st.subheader(':blue[Money flow index]')
    st.write('''
    Money Flow Index (MFI) is a movement and volume indicator which analyses both time and the price for measuring the trading pressure – buying or selling.
    It is also known as the volume-weighted Relative Strength Index (RSI), as it includes volume, unlike RSI, which only incorporates price.
    The Money Flow Index (MFI) can be interpreted similarly to RSI. Trading signals are generated by this indicator when the stock signals bullish or bearish divergence, crossovers and when the stock is in the overbought or oversold zone.
    Money Flow Index(MFI)=100-100/(1+money flow ratio).
    ''')
    st.subheader(':blue[Bollinger Bands]')
    st.write('''
    Bollinger Bands consist of 3 bands: the upper, lower and middle bands. The middle band is the 20 days or bars moving average, the upper band is +2 Standard Deviation, and the lower band is the -2 Standard Deviation of the middle band.
    When the Volatility in the market increases, these bands expand, and when the Volatility decreases, these bands contract. Traders can trade with the Bollinger bands when the prices break out from either side of the upper or lower bands after the low Volatility or consolidation phase.
    Many technical indicators work best in conjunction with other ones. Bollinger Bands® are often used along with the relative strength indicator (RSI) as well as the BandWidth indicator, which is the measure of the width of the bands relative to the middle band. Traders use BandWidth to find Bollinger Squeezes.
    Bollinger Bands® typically use a 20-day moving average.
    ''')
    st.subheader(':blue[Average True Range(ATR)]')
    st.write('''
    The ATR measures the true range of a particular number of price bars.
    ATR is a pure volatility measure that does not necessarily indicate a trend. Volatile price movement can occur inside a choppy market during an important news event.
    The best way of using the ATR is to indicate the change in the market’s nature. A rise in ATR indicates higher trading ranges and, thus, an increase in Volatility. In contrast, low readings from the ATR indicate periods of quiet or uneventful trading.
    Traders use the indicator to enter and exit trades and also to put a stop loss in order to reduce the loss if the prices move in the opposite direction.
    ''')
    st.subheader(':blue[Commodity Channel Index (CCI)]')
    st.write('''
    The Commodity Channel Index (CCI) is a momentum-based oscillator used to help determine when an investment vehicle is reaching a condition of being overbought or oversold.
    This technical indicator assesses price trend direction and strength, allowing traders to determine if they want to enter or exit a trade, refrain from taking a trade, or add to an existing position.
    When the CCI is above zero, it indicates the price is above the historic average. Conversely, when the CCI is below zero, the price is below the historic average.
    The CCI is an unbounded oscillator, meaning it can go higher or lower indefinitely. For this reason, overbought and oversold levels are typically determined for each individual asset by looking at historical extreme CCI levels where the price reversed from.
    CCI=(Typical price-MA)/(0.015*Mean Deviation)
    ''')
    st.subheader(':blue[Elliott Wave Theory]')
    st.write('''
    The Elliott Wave Theory in technical analysis describes price movements in the financial market.
    It is a technical analysis of price patterns related to changes in investor sentiment and psychology.
    The theory identifies impulse waves that establish a pattern and corrective waves that oppose the larger trend.
    Each set of waves is within another set of waves that adhere to the same impulse or corrective pattern, described as a fractal approach to investing.
    The theory assumes that stock price movements can be predicted because they move in repeating up-and-down patterns called waves created by investor psychology or sentiment.
    ''')
    st.subheader(':blue[Candlestick Patterns]')
    st.write('''
    Candlestick charts are a technical tool that packs data for multiple time frames into single price bars. This makes them more useful than traditional open, high, low, and close (OHLC) bars or simple lines that connect the dots of closing prices.
    Traditionally, candlesticks are best used on a daily basis, the idea being that each candle captures a full day’s worth of news, data, and price action. This suggests that candles are more useful to longer-term or swing traders.
    Traders supplement candlestick patterns with additional technical indicators to refine their trading strategy (e.g., entry, exit).
    Candlesticks are based on current and past price movements and are not future indicators.
    ''')
    st.subheader(':blue[Volume-Weighted Average Price (VWAP)]')
    st.write('''
    The volume-weighted average price (VWAP) is a technical analysis indicator used on intraday charts that resets at the start of every new trading session.
    It's a trading benchmark that represents the average price a security has traded at throughout the day, based on both volume and price.
    VWAP is important because it provides traders with pricing insight into both the trend and value of a security.
    VWAP = Cumulative Typical Price x Volume/Cumulative Volume, Where Typical Price = High price + Low price + Closing Price/3 , Cumulative = total since the trading session opened.
    ''')
    st.subheader(':blue[Chaikin Money Flow]')
    st.write('''
    Chaikin Money Flow is the nearer the closing price is to the high, the more accumulation has taken place.
    A CMF value above the zero line is a sign of strength in the market, and a value below the zero line is a sign of weakness in the market.
    The breakout direction of price action through trend lines or through support and resistance lines. For example, if a price breaks upward through resistance, wait for the CMF to have a positive value to confirm the breakout direction.
    A CMF sell signal occurs when price action develops a higher high into overbought zones, with the CMF diverging with a lower high and beginning to fall.
    A CMF buy signal occurs when price action develops a lower low into oversold zones, with the CMF diverging with a higher low and beginning to rise.
    ''')
    st.subheader(':blue[Stochastic Oscillator]')
    st.write('''
    A stochastic oscillator is a momentum indicator comparing a particular closing price of a security to a range of its prices over a certain period of time.
    The sensitivity of the oscillator to market movements is reducible by adjusting that time period or by taking a moving average of the result. It is used to generate overbought and oversold trading signals, utilizing a 0–100 bounded range of values.
    Stochastic oscillators tend to vary around some mean price level since they rely on an asset's price history.
    Stochastic oscillators measure recent prices on a scale of 0 to 100, with measurements above 80 indicating that an asset is overbought and measurements below 20 indicating that it is oversold.
    ''')
    st.subheader(':blue[Ichimoku Cloud]')
    st.write('''
    The Ichimoku Cloud is a collection of technical indicators that show support and resistance levels, as well as momentum and trend direction. 
    It does this by taking multiple averages and plotting them on a chart. It also uses these figures to compute a “cloud” that attempts to forecast where the price may find support or resistance in the future.
    It provides more data points than the standard candlestick chart. While it seems complicated at first glance, those familiar with how to read the charts often find it easy to understand with well-defined trading signals.
    The above trend signals are strengthened if the cloud is moving in the same direction as the price. For example, during an uptrend, the top of the cloud is moving up, or during a downtrend, the bottom of the cloud is moving down.
    ''')
    st.subheader(':blue[Rate of Change]')
    st.write('''
    The Price Rate of Change (ROC) is a momentum-based technical indicator that measures the percentage change in price between the current price and the price a certain number of periods ago.
    The ROC indicator is plotted against zero, with the indicator moving upwards into positive territory if price changes are to the upside, and moving into negative territory if price changes are to the downside.
    The indicator can be used to spot divergences, overbought and oversold conditions, and centerline crossovers.
    ROC=(closing price(p)/closing price(p-n))*100, where closing price(p)=closing price of most recent period, closing price(p-n)=closing price n periods before.      
    ''')
