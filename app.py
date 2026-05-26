import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyA0WMXWReh3HnfhDpphyj1m1l4u0tx850g"))
