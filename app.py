import streamlit as st
st.header(":blue[_Bhaskar Bhallamudi's_] streamlit demo")
st.caption("Learning to play with Data from Innomatics -- Batch_170")
st.subheader(":blue[About Me]")
st.markdown("Very curious and extremely obsessive guy." )
st.markdown("Knows Python, Data Analysis, ML and DL(still learning this part).")
st.markdown("Short-term Goals : Gain knowledge and land a decent job where I can learn")
st.markdown("Long-term Goals : Be happy:full_moon_with_face:")
st.subheader(":blue[Let's Connect:]")
st.markdown("LinkedIn:")
btn_click = st.button("LinkedIn Link")
if btn_click == True:
    st.balloons()
    st.markdown("https://www.linkedin.com/in/bhaskar-bhallamudi-6a7a511ba/")
st.markdown("GitHub profile:")
btn_git = st.button("GitHub Link")
if btn_git==True:
    st.markdown("https://github.com/Bhaskar-Bhallamudi")
    st.snow()