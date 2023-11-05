import streamlit as st
def c():
    # Title and description
    st.title("Stock Market Course")
    

    # Sidebar menu
    option = st.sidebar.selectbox("Select an Option", ["Introduction to stock market"
                                                    , "Triangles"
                                                    , "Technical Indicators",
                                                        "Investments  and tradings",
                                                        "Risk Management and portfolio optimization",
                                                        "Terminologies",
                                                        "Futures and Options",
                                                        "Stock Exchangers"])

    if option == "Introduction to stock market":
        st.header("Introduction to stock market")
        st.subheader("Stock")
        st.write('Shares of ownership in a company.')
        st.write('There are 2 types of stocks Common stocks and preferred stocks.')
        st.subheader('Common Stocks')
        st.write(':blue[Ownership]: Holders of common stock are partial owners of the company, granting them voting rights at shareholders meetings.')
        st.write(':blue[Dividends]: Eligible to receive dividends, although not guaranteed. Dividends are a portion of the companys profits distributed to shareholders.')
        st.write(':blue[Capital Appreciation]: Potential for capital gains as the stocks value increases.')
        st.write(':blue[Limited Liability]: Limited liability in the companys losses, meaning shareholders are not personally responsible for the companys debts.')

        st.subheader('Preferred Stocks:')
        st.write(''':blue[Fixed Dividends]: Preferred shareholders receive fixed dividends that are paid before common shareholders.\n
    :blue[Preference in Dividends]: In the event of company liquidation or dividend payments, preferred shareholders are entitled to receive payments before common shareholders.\n
    :blue[No Voting Rights]: Typically, preferred stockholders do not have voting rights in company decisions.\n
    :blue[Less Volatility]: Compared to common stocks, preferred stocks generally experience less price volatility.\n
    ''')
        st.subheader('Stock Markets Work:')
        st.write(''':blue[Primary Markets]:The stock market, or equity market, is a vital financial system where individuals and institutions trade ownership shares in publicly traded companies. These shares, called stocks, represent partial ownership and carry associated rights and responsibilities. Stocks are bought and sold on stock exchanges, such as the NYSE and NASDAQ. Companies go public through Initial Public Offerings (IPOs), allowing their shares to be traded.
    Stock prices are influenced by supply and demand dynamics. When more people want to buy, prices rise; when more people want to sell, prices fall. Market indices like the S&P 500 offer insights into market performance.
    Investors range from individuals to institutions with diverse objectives. Stocks offer opportunities for capital growth and dividends but come with market risks.
    Successful stock investing requires research, with methods like fundamental and technical analysis. Various strategies exist, from long-term investing to index funds.
    Regulation by bodies like the SEC maintains market integrity and investor protection.''')
        st.write(''':blue[Secondary Markets]:The secondary market is a fundamental component of the financial system where existing securities, such as stocks and bonds, are actively bought and sold by investors. Unlike the primary market, which deals with initial issuances, the secondary market provides liquidity and a platform for investors to trade previously issued securities, allowing for flexibility and the adjustment of investment portfolios. This market operates through stock exchanges like the NYSE and NASDAQ, where supply and demand dynamics determine security prices, offering opportunities for various market participants, including individual investors, institutions, and traders. While the secondary market doesn't directly raise capital for issuing entities, it plays a critical role in providing an exit strategy for investors and contributes to price discovery, making it an essential element of the financial ecosystem.
    ''')
        st.subheader('Market Participants:')
        st.write(''':blue[Buyers]:Individuals, institutional investors, or entities seeking to acquire securities (like stocks, bonds, etc.) in the stock market.''')
        st.write(''':blue[Sellers]:Individuals, institutional investors, or entities looking to sell their securities in the stock market.''')
        st.write(''':blue[Function]:Facilitate trades between buyers and sellers in the stock market by executing orders on their behalf.''')
        st.write(''':blue[Services]:Provide investment advice, execute trades, manage portfolios, and offer research and analysis.''')
        st.write(''':blue[Commissions]:Earn commissions or fees for their services, often based on the volume or value of transactions.
                ''')
    elif option=="Triangles":
        st.header('Chat Patterns')
        st.subheader('Head and shoulders pattern:')
        st.write(''':blue[Formation]:Consists of three peaks a higher peak (head) between two lower peaks (shoulders) on a price chart.
    The central peak (head) is higher than the two surrounding peaks (shoulders), which are approximately at the same level.
    The two troughs between the peaks form the neckline\n:blue[Reversal Signal]:Suggests a bullish trend is losing momentum and a bearish trend might be imminent.When the price breaks below the neckline after the right shoulder, it's often seen as a confirmation of the pattern.\n
    :blue[Volume]:Volume tends to decrease as the pattern is formed, with a surge in volume when the price breaks the neckline, confirming the pattern.\n
    :blue[Projected Price Movement]:The projected price decline after the pattern is usually estimated by measuring the distance from the head to the neckline. This length is often used to predict the potential downward movement after the breakout.\n
    :blue[Inverted Head and Shoulders]:This is a mirror image of the regular head and shoulders, indicating a potential reversal from a downtrend to an uptrend.''')
        st.subheader('Double Tops:')
        st.write(''':blue[Formation]:Occurs when the price reaches a high, retraces, rallies to a similar level, and then declines.The two peaks are separated by a trough, forming a resistance level that the price fails to surpass''')
        st.write(''':blue[Reversal Signal]:Indicates that a bullish trend might be losing momentum and a potential shift to a bearish trend could be imminent.The breakout below the support level formed by the trough confirms the pattern''')
        st.subheader('Double Bottoms')
        st.write(''':blue[Formation]:Forms after a downtrend, with the price reaching a low, rebounding, declining again to the same level as the first trough, and then rising.The two troughs are separated by a peak, forming a support level that the price fails to breach.''')
        st.write(''':blue[Reversal Signal]:Suggests that a bearish trend might be losing strength, indicating a potential shift to a bullish trend.The breakout above the resistance level formed by the peak confirms the pattern\n''')
        st.subheader('Symmetrical Triangle:')
        st.write(''':blue[Description]: Created by two trend lines that converge, forming a symmetrical triangle.''')
        st.write(''':blue[Trend Lines]: The upper trend line connects the lower highs, while the lower trend line joins the higher lows.''')
        st.write('''):blue[Interpretation]: Signals a period of indecision and market consolidation, often seen as a continuation pattern.''')
        st.subheader('Ascending Triangle')
        st.write(''':blue[Description]: Comprises a horizontal resistance line and a rising trend line.\n
    :blue[Trend Lines]: The horizontal resistance line connects multiple peaks, while the rising trend line connects higher lows.
    :blue[Interpretation]: Suggests a bullish bias, with the price likely to break upwards.''')
        st.subheader('Descending Triangle:')
        st.write(''':blue[Description]: Formed by a horizontal support line and a declining trend line.\n
    :blue[Trend Lines]: The horizontal support line connects multiple lows, while the descending trend line connects lower highs.\n
    :blue[Interpretation]: Implies a bearish bias, with the price likely to break downwards.''')
        
    elif option == "Technical Indicators":
        st.header("Technical Indicators")
        st.subheader('Simple Moving Average (SMA)')
        st.write(''':blue[Calculation]: Derived by averaging the closing prices of an asset over a defined period and recalculating it as new data becomes available.''')
        st.write(''':blue[Characteristics]: Offers a smooth representation of the price trend over the selected time frame.''')
        st.write(''':blue[Usage]: Used to identify the overall trend direction and potential support/resistance levels.''')
        st.subheader('Exponential Moving Average (EMA)')
        st.write(''':blue[Calculation]: Provides more weight to recent prices, making it more responsive to current price changes compared to the SMA.''')

        st.write(''':blue[Characteristics]: Reacts faster to price changes, allowing traders to catch new trends earlier.''')
        st.write(''':blue[Usage]: Employed to track short-term price movements and identify trend changes more promptly.''')
        st.subheader('Relative Strength Index')
        st.write(''':blue[Calculation]: RSI is calculated using a formula that measures the magnitude of recent price changes over a specified period, often 14 days. It oscillates between 0 and 100.''')
        st.write(''':blue[Overbought and Oversold Levels]:Values above 70 are typically considered overbought, indicating a potential sell signal.Values below 30 are generally considered oversold, signaling a potential buy opportunity.''')
        st.subheader('Moving Average Convergence Divergence (MACD):')
        st.write('''The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of an asset's price. It is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA.''')
        st.write(''':blue[MACD Line (12-day EMA - 26-day EMA)]:The difference between the 12-day and 26-day exponential moving averages.Provides insight into short-term price momentum relative to the longer-term momentum.''')
        st.write(''':blue[Signal Line (9-day EMA of MACD Line)]:A 9-day Exponential Moving Average of the MACD Line.Serves as a signal line, generating buy or sell signals.''')
        st.write(''':blue[MACD Histogram (Difference between MACD Line and Signal Line)]:Displays the difference between the MACD Line and the Signal Line.Offers a visual representation of the difference between the MACD and its signal line.''')
        st.subheader('Bollinger Bands')
        st.write('''Bollinger Bands are a technical analysis tool developed by John Bollinger that consists of three bands: a middle band representing the simple moving average (SMA), and an upper and lower band calculated by adding and subtracting a specified standard deviation from the SMA.''')
        st.write(''':blue[Middle Band (SMA)]:Typically a 20-period SMA that serves as the centerline.Reflects the average price over the chosen period.''')
        st.write(''':blue[Upper Band]:Calculated by adding a specified number (usually 2) of standard deviations to the SMA.Represents the upper volatility boundary.''')
        st.write(''':blue[Lower Band]:Calculated by subtracting the same number of standard deviations from the SMA.
    ''')

    elif option == "Investments  and tradings":
        st.header('''Investments  and tradings''')
        st.subheader('Long term investment:')
        st.write('''Long-term investment refers to the practice of purchasing and holding financial assets, such as stocks, bonds, real estate, or other investment vehicles, for an extended period of time with the expectation of achieving capital appreciation and/or income over the long run. The primary goal of long-term investing is to accumulate wealth and achieve financial objectives over a time horizon that typically extends beyond several years, often ranging from years to decades.
        Here are some key characteristics and concepts associated with long-term investment:''')
        st.write(''':blue[Time Horizon]:Long-term investors are willing to hold their investments for an extended period, allowing their assets to potentially grow in value over time. This approach is in contrast to short-term traders who seek to profit from short-term price fluctuations.\n :blue[Capital Appreciation]: Long-term investors primarily aim to benefit from the appreciation of their investments' value over time. This appreciation can result from factors like economic growth, corporate profitability, and market trends.\n :blue[Income Generation]: Some long-term investments, such as bonds or dividend-yielding stocks, provide regular income in the form of interest or dividends. This income can supplement an investor's cash flow or be reinvested to further enhance returns.\n''')
        st.subheader('Short term investment:')
        st.write('''Short-term investments refer to the practice of acquiring financial assets with the intention of holding them for a relatively brief period, typically ranging from a few days to a few years. These investments are designed to provide liquidity and relatively quick access to capital while still generating some return on investment. Short-term investments serve various purposes, including preserving capital, generating income, and taking advantage of immediate opportunities. Here are some key characteristics and examples of short-term investments:''')
        st.write(''':blue[Short Time Horizon]: Short-term investors have a shorter investment horizon compared to long-term investors. They may have a specific financial goal in the near future or anticipate the need for funds within a short time frame.\n :blue[Liquidity]: Short-term investments are chosen for their relatively high liquidity. This means that the investor can easily convert the investment into cash or another asset with minimal loss of value.\n :blue[Preservation of Capital]: While generating a return is important, the primary focus of short-term investments is often on preserving the capital invested, rather than taking on excessive risk.''')
        st.subheader('Intraday trading')
        st.write('''Intraday trading, often referred to as day trading, is a style of trading in financial markets where traders buy and sell financial assets (e.g., stocks, currencies, commodities, or derivatives) within the same trading day. Intraday traders aim to profit from short-term price movements and take advantage of market volatility. Key characteristics and aspects of intraday trading include:\n :blue[Quick Trades]: Day traders make multiple trades throughout the trading session, looking to capitalize on small price fluctuations. Each trade is usually executed with a specific entry and exit point.\n:blue[Leverage]: Intraday traders often use leverage to amplify the potential returns from their trades. However, leverage also increases risk, and traders can face significant losses if the market moves against them.\n:blue[Technical Analysis]: Intraday traders primarily rely on technical analysis and use various technical indicators, chart patterns, and analysis tools to make trading decisions. They examine price charts and other technical data to predict short-term price movements.\n:blue[Volatility]: Intraday traders seek assets with sufficient volatility to create opportunities for short-term profits. High volatility can result from news events, economic releases, or market sentiment''')
        st.subheader('Short Selling:')
        st.write('''Short selling, also known as "shorting," is a trading strategy that involves selling an asset (such as a stock, bond, or commodity) that the seller does not own at the time of the sale. In a short sale, the seller anticipates that the price of the asset will decline, and they aim to profit from this anticipated price decrease. Short selling involves several key steps and mechanics:\n:blue[Borrowing the Asset]: Before initiating a short sale, the trader or investor must borrow the asset from a broker or another source. This borrowed asset is typically sold immediately in the market. The lender of the asset may charge a fee for borrowing.\n:blue[Selling the Asset]: After obtaining the borrowed asset, the seller sells it in the market, effectively creating a short position. They receive the proceeds from the sale, which are held in their trading account.\n:blue[Waiting for a Price Decline]: The seller's profit in a short sale comes from the difference between the price at which they initially sold the asset (the short sale price) and the price at which they will repurchase the asset (the cover or buy-to-cover price) later. The seller expects the asset's price to decrease.\n:blue[Buying Back the Asset]: At a later time, the seller must repurchase the same quantity of the asset they initially borrowed and sold. This is known as "covering" or "buying to cover" the short position.\n:blue[Returning the Borrowed Asset]: The repurchased asset is returned to the lender. The cost of repurchasing the asset is deducted from the proceeds received from the initial short sale, and any price difference represents the profit or loss on the short sale.''')
    elif option == "Risk Management and portfolio optimization":
        st.header('''Risk Management and portfolio optimization''')
        st.write('''Risk management is the process of identifying, assessing, and prioritizing risks and taking measures to minimize or mitigate their potential negative impact on an organization, project, or investment. Effective risk management aims to enhance decision-making, protect assets, and optimize opportunities while ensuring that potential adverse events are considered and planned for. It is a fundamental component of good governance, whether in business, finance, project management, or everyday life.Key components of risk management include: ''')
        st.subheader('Risk Identification')
        st.write('''This involves identifying and recognizing potential risks that could affect a specific goal, project, or operation. Risks can be internal or external, and they may be related to various factors, including financial, operational, strategic, or regulatory issues.''')
        st.subheader('Risk Assessment:')
        st.write('''Once risks are identified, they are assessed to determine their potential impact and likelihood. This process often involves assigning risk ratings or scores to prioritize risks and focus resources on the most significant threats.''')
        st.subheader('Risk Avoidance:')
        st.write('''In certain situations, it may be prudent to avoid a particular risk altogether by refraining from engaging in a specific activity or making a particular investmen''')
        st.subheader('Risk Acceptance:')
        st.write('''Some risks are considered acceptable, and organizations or individuals may choose to accept them without taking specific actions to mitigate or transfer them. This approach is often based on a cost-benefit analysis.''')
        st.subheader('Portfolio:')
        st.write('''A portfolio refers to a collection or combination of financial assets, such as stocks, bonds, real estate, and other investments, held by an individual or entity. Portfolios are structured to achieve specific financial goals, manage risk, and potentially maximize returns. By diversifying investments across different asset classes or securities, a portfolio aims to spread risk and minimize the impact of poor performance from any single asset.
        ''')
        st.subheader('Optimization of portfolio:')
        st.write('''Portfolio optimization is a systematic process of constructing an investment portfolio that aims to achieve the highest possible return for a given level of risk or the lowest possible risk for a given level of return. It combines various assets or securities in a way that maximizes the portfolio's expected return while minimizing its risk. Portfolio optimization is based on the principles of diversification and the concept that not all assets move in the same direction at the same time.''')
        st.write(''':blue[Set Investment Goals]:Define your financial objectives, risk tolerance, and time horizon. Are you investing for long-term growth, income, or capital preservation? Understanding your goals is fundamental to portfolio optimization.''')
        st.write(''':blue[Select Asset Classes]:Determine which asset classes you want to include in your portfolio. Common asset classes include stocks, bonds, cash or equivalents, and alternative investments like real estate or commodities.''')
        st.write(''':blue[Analyze Correlations]:Analyze the correlations between the assets in your portfolio. Consider how they tend to move in relation to each other. Diversification benefits are greater when assets have low or negative correlations.''')
        st.write(''':blue[Rebalance Regularly]:Periodically review your portfolio to ensure it remains aligned with your target allocation. Market movements may cause deviations from the desired mix, so rebalancing helps maintain portfolio integrity.''')
        st.write(''':blue[Consider Constraints]:Take into account any specific constraints, such as liquidity needs, regulatory restrictions, tax considerations, or ethical investing preferences. These factors may influence the asset allocation and investment choices.''')
    elif option=="Terminologies":
        st.header('''Stock Market Terminologies''')
        st.subheader('Stock')
        st.write('''A share of ownership in a company.''')
        st.subheader('Market Capitalization')
        st.write('''The total value of a company's outstanding shares, calculated by multiplying the stock price by the number of shares.''')
        st.subheader('Dividend')
        st.write('''A portion of a company's earnings distributed to shareholders as a cash payment or additional shares.
        ''')
        st.subheader('Bull Market')
        st.write('''A market characterized by rising stock prices and optimism among investors.''')
        st.subheader('Bear Market')
        st.write('''A market characterized by falling stock prices and pessimism among investors.''')
        st.subheader('Index')
        st.write('''A benchmark that tracks the performance of a group of stocks, such as the S&P 500 or Dow Jones Industrial Average.
        ''')
        st.subheader('Volatility')
        st.write('''The degree of variation in the price of a stock or the overall market.''')
        st.subheader('Blue-Chip Stock')
        st.write('''Shares of well-established, financially stable, and reputable companies.
        ''')
        st.subheader('IPO(initial public offering)')
        st.write('''The first sale of a company's stock to the public.
        ''')
        st.subheader('Limit Order')
        st.write('''An order to buy or sell a stock at a specific price or better.''')
        st.subheader('Stock Exchange')
        st.write('''A marketplace where stocks are bought and sold, such as the New York Stock Exchange (NYSE) or NASDAQ.
        ''')
        st.subheader('Ticker Symbol')
        st.write('''A unique abbreviation or combination of letters representing a publicly traded company's stock.
        ''')
        st.subheader('Portfolio')
        st.write('''A collection of investments held by an individual or institution.
        ''')
        st.subheader('Asset Allocation')
        st.write('''The distribution of investments among different asset classes, such as stocks, bonds, and cash.''')
        st.subheader('Brokerage Account')
        st.write('''An account with a brokerage firm that allows individuals to buy and sell stocks and other securities.''')
        st.subheader('Diversification')
        st.write('''Spreading investments across various assets or asset classes to reduce risk.''')
        st.subheader('Market Order')
        st.write('''An order to buy or sell a stock at the current market price.''')
        st.subheader('Stock Split')
        st.write('''An action by a company to increase the number of its outstanding shares, typically to lower the stock's price per share.''')
        st.subheader('Short Selling')
        st.write('''The practice of selling borrowed shares with the expectation that the price will fall, allowing for a profitable buyback.''')
        st.subheader('Day Trading')
        st.write('''The practice of buying and selling stocks within the same trading day to profit from short-term price fluctuations.''')
        st.subheader('P/E Ratio')
        st.write('''A valuation ratio that measures the price of a stock relative to its earnings per share.''')
        st.subheader('Yield')
        st.write('''The income generated from an investment, often expressed as a percentage.''')
        st.subheader('Liquidity')
        st.write('''The ease with which an asset can be bought or sold without affecting its price.''')
        st.subheader('Stockbroker')
        st.write('''A licensed professional who buys and sells stocks on behalf of clients.''')
        st.subheader('Earning report')
        st.write('''A company's financial report that discloses its earnings, revenue, and other financial information.''')
    elif option=="Futures and Options":
        st.header('''Futures and Options''')
        st.subheader('Futures:-')
        st.write('''these are financial derivatives contracts that obligate the parties involved to buy or sell a specific quantity of a particular financial asset (such as stocks, stock indices, commodities, or currencies) at a predetermined price on a specified future date. These contracts are standardized in terms of the underlying asset, quantity, price, and expiration date, and they are traded on organized futures exchanges.''')
        st.write(''':blue[Commodity Futures]:\n:blue[Agriculture Futures]: Trading in agricultural commodities like wheat, corn, soybeans, and coffee.''')
        st.write(''':blue[Energy Futures]: Focusing on commodities like crude oil, natural gas, and heating oil.''')
        st.write(''':blue[Metal Futures]: Trading in metals such as gold, silver, copper, and aluminum.''')
        st.write(''':blue[Soft Commodities]: Includes futures on items like sugar, cotton, and cocoa.''')
        
        st.write(''':blue[Stock Index Futures]: Contracts based on the performance of stock market indices like the S&P 500 or NASDAQ.''')
        st.write(''':blue[Interest Rate Futures]: Involves trading on interest rate products such as Treasury bonds and Eurodollar futures.''')
        st.write(''':blue[Currency Futures]: Trading in foreign exchange currencies (forex) for speculative or hedging purposes.''')
        
        st.write(''':blue[Single Stock Futures]: Contracts based on the performance of individual stocks.''')
        st.write(''':blue[Index Futures]: Focusing on futures contracts tied to stock market indices, which allow for broad market exposure.Key points to understand about futures in the stock market:''')
        st.write(''':blue[Obligations]:Both parties are legally obligated to fulfill the contract. This means the buyer must purchase, and the seller must sell, the asset at the agreed-upon price and date.''')
        st.write(''':blue[Leverage]:Futures contracts often require a relatively small initial margin, allowing traders to control a larger position size. This leverage can amplify both gains and losses.''')
        st.write(''':blue[Risk Management]:Futures are used for hedging and speculation. Investors use them to manage risk or to profit from anticipated price movements.''')
        st.subheader('Options:')
        st.write('''An options contract provides the holder (buyer) the right, but not the obligation, to buy (call option) or sell (put option) the underlying asset at a specific price (strike price) on or before a predetermined expiration date.In options, there are two parties: the option holder (buyer) and the option writer (seller). The writer receives a premium from the buyer for granting the option.''')
        st.write(''':blue[Call Option]:-A call option is a financial contract that gives the owner the right, but not the obligation, to buy a specific quantity of an underlying asset (such as a stock, commodity, or index) at a predetermined price (the strike price) on or before a specified expiration date. The buyer of a call option pays a premium to the seller of the option for this right. Call options are commonly used for various purposes, including speculating on price increases, hedging, and generating income.''')
        st.write(''':blue[Put Option]:-A put-options is a financial contract that gives the owner the right, but not the obligation, to sell a specific quantity of an underlying asset (such as a stock, commodity, or index) at a predetermined price (the strike price) on or before a specified expiration date. The buyer of a put option pays a premium to the seller of the option for this right. Put options are commonly used for various purposes, including speculating on price declines, hedging, and generating income.''')
        st.write(''':blue[Flexibility]:Options provide flexibility as the holder can choose whether or not to exercise the contract. The writer, however, is obligated to fulfill the contract if the holder chooses to exercise''')
        st.write(''':blue[Leverage]:Options also offer leverage, as the initial investment (the premium) is much smaller than the value of the underlying asset.''')
        st.write(''':blue[Risk Management]:Options are used for various purposes, including hedging against adverse price movements and generating income through option writing.'''
        )
    elif option=="Stock Exchangers":
        st.header('''Stock Exchangers''')
        st.write('''Stock exchanges are organized financial marketplaces where securities, such as stocks, bonds, commodities, and derivatives, are bought and sold. They provide a centralized platform for investors to trade these securities. Key functions of stock exchanges include facilitating the trading process, ensuring transparency, setting rules and regulations for market participants, and providing a marketplace for price discovery. Prominent examples of stock exchanges include the New York Stock Exchange (NYSE), NASDAQ, London Stock Exchange, and Tokyo Stock Exchange. Stock exchanges play a pivotal role in the global financial system, enabling companies to raise capital through the issuance of stocks and providing investors with opportunities to buy and sell securities. They are subject to strict regulatory oversight to maintain market integrity and protect investors.\n
        Types:-''')
        st.subheader('Primary Exchangers')
        st.write('''These are the major, well-established stock exchanges in major financial centers like the New York Stock Exchange (NYSE) and NASDAQ in the United States, London Stock Exchange in the UK, and Tokyo Stock Exchange in Japan. They are known for their large and highly liquid markets.''')
        st.subheader('Secondary Exchangers')
        st.write('''Secondary exchanges are usually smaller and less liquid than primary exchanges. They often list smaller companies or those not meeting the stringent requirements of primary exchanges. Examples include the NYSE American and the Tokyo Stock Exchange's TSE Mothers.''')
        st.subheader('Stock Exchanges in india and their indexes:-')
        st.write('''1):blue[The Bombay Stock Exchange (BSE)]: is one of India's oldest and largest stock exchanges, situated in Mumbai. Established in 1875, it plays a pivotal role in the Indian financial market, providing a platform for trading equities, commodities, and various other financial instruments. BSE is known for its benchmark index, the Sensex, which tracks the performance of 30 of the country's largest and most actively traded stocks. It has a rich history of facilitating economic growth and investment opportunities in India, serving as a crucial barometer for the nation's economic health and financial stability.''')
        st.write(''':blue[Index]:The Sensex is a collection of the top 30 companies listed on the Bombay Stock Exchange (BSE), representing a diverse range of sectors in the Indian economy. These companies are referred to as "blue-chip" stocks and are among the largest and most influential companies in India.''')
        st.write('''2):blue[The National Stock Exchange (NSE)]: is one of India's leading stock exchanges, headquartered in Mumbai. Established in 1992, it has grown to become the largest stock exchange in India by market capitalization and is known for its technologically advanced trading platform and robust regulatory framework. The NSE facilitates trading in various financial instruments, including equities, derivatives, debt securities, and exchange-traded funds. It operates key benchmark indices like the Nifty 50, which tracks the performance of 50 of India's largest and most actively traded companies, making it a significant player in the Indian financial landscape, providing investors with a vital barometer of the nation's economic health and financial stability.''')
        st.write(''':blue[Index]:-The National Stock Exchange of India (NSE) also has its own benchmark index known as the Nifty 50, or simply the Nifty, which comprises the top 50 companies listed on the NSE. Together with the Sensex, the Nifty is a key indicator of the Indian stock market's performance.''')
