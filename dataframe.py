from feedback import fetch_users,feedbackform
import pandas as pd
import streamlit as st

feedbackform()
users=fetch_users()
cols=list(users[0].keys())
f=[]
k=[]
n=[]
ra=[]
re=[]
u=[]

for user in users:
    f.append(user[cols[1]])
    k.append(user[cols[2]])
    n.append(user[cols[3]])
    ra.append(user[cols[4]])
    re.append(user[cols[5]])
    u.append(user[cols[6]])

d={
    'email':k,
    'Name':n,
    'Username':u,
    'Feedback':f,
    'Rating':ra,
    'Review':re
}

df=pd.DataFrame(d)
print(df)
        