import streamlit as st
import pandas as pd
from supabase import create_client


SUPABASE_URL="https://wxcpfeabmqgtlpuibxin.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind4Y3BmZWFibXFndGxwdWlieGluIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDExNTksImV4cCI6MjA4MTYxNzE1OX0.fgCZDnmDi5E2aPT2LufMIKhi6lcy31Fsrg4zRduT01Q"


supabase = create_client(SUPABASE_URL,SUPABASE_KEY)
st.title("HDFC BANK(supabase)")
menu=("REGISTRATION","VIEW")
choice = st.sidebar.selectbox("menu",menu)

if choice == "REGISTRATION":
    name=st.text_input("ENTER NAME")
    age=st.number_input("age",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("save"):
        supabase.table("users").insert({
            "name":name,
            "age" :age,
            "account":account,
            "balance" :bal}).execute()
        st.success("user added successfully")


if choice =="VIEW":
    st.subheader("view user")
    data = supabase.table("users").select("*").execute()
    df = pd.DataFrame(data.data)

    st.dataframe(df)
