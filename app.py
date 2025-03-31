import streamlit as st
from src.style import apply_style
from src.example_function import random_time_process
from src.about_it import about_it_text
import concurrent.futures
from random import randrange

apply_style()

st.header(":rainbow[Zac Milioli] (Apr/2025)")
st.title(":orange[Multiprocessing] in :red[Streamlit]")

with st.expander(label="About it", icon=":material/lightbulb:"):
    st.markdown(about_it_text)

st.markdown('---')
st.title("Try it yourself")
with st.container(border=True):
    st.markdown("In this simulation, you can select the number of workers, max seconds of sleep and instances you wish to execute with multithreading.\n\nAfter clicking the button, just watch as they execute an example function with random sleep times.")

cols = st.columns(3)
cols[0].number_input("Workers", min_value=1, max_value=50, value=5, key="workers")
cols[1].number_input("Instances", min_value=1, max_value=500, value=15,key="instances")
cols[2].number_input("Max seconds of sleep", min_value=1, max_value=500, value=8, key="max_seconds")

if st.button("Play simulation :material/play_circle:", use_container_width=True):
    num_workers = st.session_state['workers']
    instances = st.session_state['instances']
    max_seconds = st.session_state['max_seconds']
    results = []
    threads = []
    progress_num = 0
    progress = st.progress(progress_num, "Starting threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        for _ in range(0,instances):
            random_number = randrange(1, max_seconds)
            threads.append(executor.submit(random_time_process, random_number))
            st.toast(f"Thread of {random_number} seconds queued", icon=":material/play_arrow:")
        for future in concurrent.futures.as_completed(threads):
            result = future.result()
            if result:
                st.toast(result, icon=":material/check:")
                results.append(result)
                progress_num += 1
                progress.progress(progress_num/instances, f"Threads done: {progress_num}/{instances}")
            else:
                st.toast("An error has occurred", icon=":material/error:")
    st.session_state['results'] = results
    progress.empty()

if "results" in st.session_state:
    st.title("Results summary")
    with st.container(border=True):
        for i in st.session_state['results']:
            st.markdown(f"- {i}")
