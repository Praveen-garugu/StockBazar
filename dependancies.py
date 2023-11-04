import streamlit as st
import streamlit_authenticator as stauth
import datetime
import re
from deta import Deta
DATA_KEY='d0j6euzkhxu_zPjEC6kYCvndvoDsV6bGaFGmQp7gyVgk'
deta=Deta(DATA_KEY)

db=deta.Base('signin')

def insert_user(email,username,password):
    date_joined=str(datetime.datetime.now())

    return db.put({'key':email,'username':username,'password':password,'date_joined':date_joined})

def fetch_users():

    users=db.fetch()

    return users.items
#insert_user('a123@gmail.com','abc123','1234567')
#print(fetch_users())
def get_user_email():
    users=db.fetch()
    emails=[]
    for user in users.items:
        emails.append(user['key'])
    return emails

def get_user_email():
    users=db.fetch()
    emails=[]
    for user in users.items:
        emails.append(user['key'])
    return emails
def get_username():
    users=db.fetch()
    username=[]
    for user in users.items:
        username.append(user['key'])
    return username
def validate_email(email):
    pattern="^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(pattern,email):
        return True
    return False

def validate_username(username):
    pattern="^[a-zA-Z0-9]*$"
    if re.match(pattern,username):
        return True
    return False

def signup():
    st.title(':blue[What Is the Stock Market, What Does It Do, and How Does It Work?]')
    st.header('')
    st.subheader('What Is the Stock Market?')
    st.write('''
    The term stock market refers to several exchanges in which shares of publicly held companies are bought and sold. Such financial activities are conducted through formal exchanges and via over-the-counter (OTC) marketplaces that operate under a defined set of regulations. 
    Both “stock market” and “stock exchange” are often used interchangeably. Traders in the stock market buy or sell shares on one or more of the stock exchanges that are part of the overall stock market.
            ''')

    st.subheader('Understanding the Stock Market')
    st.write('''
    The first stock market was the London Stock Exchange which began in a coffeehouse, where traders met to exchange shares, in 1773.
    The first stock exchange in the United States began in Philadelphia in 1790.
    The Buttonwood Agreement, so named because it was signed under a buttonwood tree, marked the beginning of New York’s Wall Street in 1792. The agreement was signed by 24 traders and was the first American organization of its kind to trade in securities. The traders renamed their venture the New York Stock and Exchange Board in 1817

    ''')

    st.subheader('How the Stock Market Works?')
    st.write('''
    Stock markets provide a secure and regulated environment where market participants can transact in shares and other eligible financial instruments with confidence, with zero to low operational risk. Operating under the defined rules as stated by the regulator, the stock markets act as primary markets and secondary markets.
            
    As a primary market, the stock market allows companies to issue and sell their shares to the public for the first time through the process of an initial public offering (IPO). This activity helps companies raise necessary capital from investors.


    ''')

    st.subheader('Who Helps an Investor Trade on the Stock Market?')
    st.write('''
    Stock Brokers act as intermediaries between the stock exchanges and the investors by buying and selling stocks and portfolio managers are professionals who invest portfolios, or collections of securities, for clients. Investment bankers represent companies in various capacities, such as private companies that want to go public via an IPO
    ''')
    with st.form(key='signup',clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email=st.text_input(':blue[Email]',placeholder='Enter your email')
        username=st.text_input(':blue:[username]',placeholder='Enter your username')
        password=st.text_input(':blue[Password]',type='password',placeholder='Enter your password')
        cpassword=st.text_input(':blue[Confrim Password]',placeholder='Confirm your password')
        st.form_submit_button('Sign Up')

        if email:
            if validate_email(email):
                if email not in get_user_email():
                    if validate_username(username):
                        if username not in get_username():
                            if len(username)>2:
                                if len(password)>=6:
                                    if password==cpassword:
                                        pass
                                        hashed_password=stauth.Hasher([password]).generate()
                                        insert_user(email,username,hashed_password[0])
                                        st.success("Account Created Successully")
                                        st.snow()
                                    else:
                                        st.warning('Password didnt match')
                                else:
                                    st.warning('Password is short')
                            else:
                                st.warning('Username is too short')
                        else:
                            st.warning('Username Exist')    
                else:
                    st.warning('Email Already exist')
            else:
                st.warning('Invalid Email')
#sign_up()