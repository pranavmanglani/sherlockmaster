import streamlit as st
import pandas as pd
import sherlock 
from sherlock import *
from sherlock_project.sherlock import sherlock
from sherlock_project.sites import SitesInformation
from sherlock_project.notify import QueryNotifyPrint
from sherlock_project.result import QueryStatus
import time

st.set_page_config(
    page_title="Sherlock Web App",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Sherlock Username Search")
st.markdown("""
This web application helps you find usernames across social networks using Sherlock.
Simply enter a username below and click 'Search' to find where that username exists.
""")

# Initialize session state for results
if 'results' not in st.session_state:
    st.session_state.results = None
if 'searching' not in st.session_state:
    st.session_state.searching = False

# Create the search form
with st.form("search_form"):
    username = st.text_input("Enter username to search:", placeholder="johndoe")
    timeout = st.slider("Request timeout (seconds):", min_value=10, max_value=120, value=60)
    submitted = st.form_submit_button("Search")

if submitted and username:
    st.session_state.searching = True
    st.session_state.results = None
    
    # Create a progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Initialize Sherlock components
    site_data = SitesInformation()
    query_notify = QueryNotifyPrint()
    
    # Create a placeholder for results
    results_placeholder = st.empty()
    
    # Run the search
    try:
        results = sherlock(
            username=username,
            site_data=site_data,
            query_notify=query_notify,
            timeout=timeout
        )
        
        # Process results
        found_sites = []
        for site_name, result in results.items():
            if result.status == QueryStatus.CLAIMED:
                found_sites.append({
                    'Site': site_name,
                    'URL': result.url,
                    'Status': 'Found'
                })
        
        if found_sites:
            st.session_state.results = pd.DataFrame(found_sites)
        else:
            st.session_state.results = pd.DataFrame(columns=['Site', 'URL', 'Status'])
            st.session_state.results.loc[0] = ['No sites found', '', 'Not Found']
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
    
    st.session_state.searching = False

# Display results
if st.session_state.results is not None:
    st.subheader("Search Results")
    st.dataframe(
        st.session_state.results,
        use_container_width=True,
        hide_index=True
    )
    
    # Add download button for results
    csv = st.session_state.results.to_csv(index=False)
    st.download_button(
        label="Download Results as CSV",
        data=csv,
        file_name=f"sherlock_results_{username}.csv",
        mime="text/csv"
    )

# Add footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ using Sherlock and Streamlit</p>
    <p>Original Sherlock project: <a href="https://github.com/sherlock-project/sherlock">GitHub</a></p>
</div>
""", unsafe_allow_html=True)
