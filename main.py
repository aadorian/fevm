
import os
import time
import json
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import streamlit as st
import subprocess
import sys
import requests
from pathlib import Path
# from
from pandas import json_normalize
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.mention import mention
from st_aggrid import AgGrid


st.set_page_config(
    page_title="FEVM with Truffle",
    page_icon="🧊",

    layout="wide",  # center, wide
    initial_sidebar_state="collapsed",  # "expanded, auto"
    menu_items={

        'About': "# This is a header. This is an proof of FEVM !"
    }
)

CDN = """<link rel="stylesheet" href="https://unpkg.com/flowbite@1.5.3/dist/flowbite.min.css" />
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
<link rel="stylesheet" href="https://unpkg.com/flowbite@1.5.3/dist/flowbite.min.css" />
<script src="https://unpkg.com/flowbite@1.5.3/dist/flowbite.js"></script>"""

# Beryx Token
BEARER_TOKEN = st.secrets["token"]

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)
def construct_HTML(data):
    source = CDN
    return f"{source}{data} "

def labelResults(text):
    html_string_ = f'''
<!doctype html>
<html>
<head>
   <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
<div class="flex -space-x-2 overflow-hidden">
  <img class="inline-block h-10 w-10 rounded-full ring-2 ring-white" src="https://i.imgur.com/NrQRoYS.png" alt="compile">
</div>
    <div class="border-t border-gray-200 pt-1">
          <dt class="font-medium text-gray-900">{text}</dt>
          <dd class="mt-2 text-sm text-gray-500"> Results</dd>
</body>
</html>
'''
    return html_string_

# Example of dataframe loading
DATE_COLUMN = "Field"
DATA_URL = "data.csv"
df = pd.read_csv(DATA_URL)

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

def card(title, data):

    return f"""<a href="#" class="block p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hover:bg-gray-100 dark:bg-gray-800 
    dark:border-gray-700 dark:hover:bg-gray-700">
    <svg xmlns="http://www.w3.org/2000/svg" height="48" width="48"><path d="m16 35.9-12-12 12.1-12.1 2.15 2.15L8.3 23.9l9.85 9.85Zm15.9.1-2.15-2.15 9.95-9.95-9.85-9.85L32 11.9l12 12Z"/></svg>
   <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{title}</h5><p class="font-normal text-gray-500 dark:text-gray-400">{data}</p></a>"""


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

def save_uploadedfile(uploadedfile):
     uploadedfile.name = "Storage.sol"
     with open(os.path.join("contracts",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

# headers to call  API
headers = {
    'Accept': 'application/json',
    'Authorization': BEARER_TOKEN,
}
params = {
    'page': '1',
} 

#https://fonts.google.com/icons?icon.query=developer
st.write(construct_HTML(card("FEVM", "with Truffle")), unsafe_allow_html=True)
compiled = False
migrated = False
deployed = False
tab1, tab2, tab3, tab4 = st.tabs(["Compile | Deploy | Migrate", "Beryx Filecoin API", "Local Node", "Resources"])

with tab1:
    st.caption("Compile | Deploy | Migrate")
   
    col1, col2, col3 = st.columns(3,gap='small')

    with col1:
        if st.button('Compile'):
            subprocess.run([f"{sys.executable}", "compile.py"])
            st.snow()
            st.caption('Compilation Done')
            st.caption('ABI')   
            compiled = 'True'
        else:
            st.caption('Local Compile')
    with col2:
        if st.button('Deploy '):
            subprocess.run([f"{sys.executable}", "deploy.py"])
            st.snow()
            st.caption('Done Deploy')
            deployed = 'True'
        else:
            st.caption('Deploy to Local Node')

    with col3:
        if st.button('Migrate'):
            st.caption('Done Migrate')
            subprocess.run([f"{sys.executable}", "migrate.py"])
            st.snow()
            migrated = 'True'

        else:
            st.caption('Migrate to Wallaby Failed')

    st.markdown("<hr/>", unsafe_allow_html=True)
    if compiled: 
        filename = './build/contracts/Storage.json'     
        with open(filename) as f:
            data = json.load(f)
        st.code(data['abi'])
    if migrated: 
        st.markdown('[GLIF Explorer](https://explorer.glif.io/?network=wallaby)') 
    components.html(labelResults('Compile | Deploy | Migrate'), height=200)

   

 


with tab2:

    
   
    st.header("Beryx Filecoin API")
    code = '''f17uoq6tp427uzv7fztkbsnn64iwotfrristwpryy'''
    st.code(code)

    expander = st.expander("Beryx OpenAPI Tools")
   
    with st.expander("balance of {address} calculated at the tip"):
        try:
            form = st.form(key='my_form')
            name = form.text_input(label='Enter some address: ', value='f1bkgyshmwpji4sltshvtyzf6yb7uraxr2pkwlamq')
            st.caption(f"""Returns the balance of {name} calculated at the tip""")
           
            if st.session_state.disabled:
                df = pd.read_csv("balance_headers.csv")  
                st.table(df) 
            submit_button = form.form_submit_button(label='Submit')
            if submit_button:
                data = 'https://api.zondax.ch/fil/data/v1/wallaby/account/balance/'
                send = f'{data}{name}'
                response = requests.get(send, params=params, headers=headers)
                data = response.json()
                norm = pd.json_normalize(data,record_path=['balances'])
                st.metric('Balance', norm.iloc[0].value, 'FIL')
                st.write(norm)
                st.caption(response.json())
                AgGrid(norm)
        except ValueError:
            st.write('Error')
    with st.expander('Returns the transactions where the address {address} participated'):
        try:
            form = st.form(key='my_form_transactions')
            name = form.text_input(label='Enter some address: ', value='f1bkgyshmwpji4sltshvtyzf6yb7uraxr2pkwlamq')
            st.caption(f"""Returns the transactions where the address {name} participated""")
            
            st.checkbox("Display Schema", key="disabled")
            if st.session_state.disabled:
                df = pd.read_csv("transactions_headers.csv")  
                st.table(df) 
            submit_button = form.form_submit_button(label='Submit')
            if submit_button:
               # st.caption('https://api.zondax.ch/fil/data/v1/wallaby')
                page = '?page=1'
                data = 'https://api.zondax.ch/fil/data/v1/wallaby/transactions/address/'
                send = f'{data}{name}{page}'
                response = requests.get(send, params=params, headers=headers)
                data = response.json()
                norm = pd.json_normalize(data,record_path=['Transactions'])
               
                AgGrid(norm)
        except ValueError:
            st.write('Error')
    components.html(labelResults('Beryx API'), height=200)
with tab3:
    col1, col2 = st.columns([0.5, 1])
    with col1:
        st.caption("Upload a Solidity File to Compile, Deploy and Migrate")
    with col2:
        # To convert to a string based IO:

   
    
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
                bytes_data = uploaded_file.read()
                st.write("filename:", uploaded_file.name)
                st.write(bytes_data)
                save_uploadedfile(uploaded_file)  
        st.caption('Upload a solidity file.')
    components.html(labelResults('Local Node '), height=200)
    
        #st.warning('This is a warning', icon="⚠️")
        #st.info('This is a purely informational message', icon="ℹ️")
        #st.snow()
        #st.success('This is a success message!', icon="✅")
        #my_bar = st.progress(0)

        #for percent_complete in range(100):
        #   time.sleep(0.1)
        #   my_bar.progress(percent_complete + 1)
        #my_bar.empty()

with tab4:
    st.markdown('### Evidence of deployed contracts')
    st.code('0x0AD82D84073CC34B689CB74CEB6759A61D4E58FE')
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown('## NOTE: filecoinMockAPIs are deployed locally')
    st.markdown('[Explorer](https://explorer.glif.io/?network=wallaby)   | [Faucet](https://wallaby.network/#faucet)| [Docs ](https://fevm.ethglobal.com/#docs)| [Github](https://github.com/aadorian/fevm.git) | [Transactions](https://explorer.glif.io/address/t410fq5bq6eh23g44xbafni37qnwyvaccaqydncmf2ea/?network=wallaby ) | [Remix](https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js)') 

   
    components.html(labelResults('Resources '), height=200)
    mention(
        label="githubrepo",
        icon="github", 
        url="https://github.com/aadorian/fevm.git",
    )