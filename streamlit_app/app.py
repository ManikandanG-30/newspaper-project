import os
import django
import streamlit as st

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from articles.models import Article

st.title("My Newspaper Dashboard")
st.write("Listing all articles:")

for article in Article.objects.all():
    st.write(article.title)
