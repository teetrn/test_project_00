# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XEOv1QdaENhVi2P2C4wyhkD-RNvnpReK
"""

import streamlit as st
import random

st.title('Test Streamlit')
st.write('Hello World!')

if st.button('Generate Random Number'):
    random_number = random.randint(1, 100)
    st.write(f'Random Number: {random_number}')