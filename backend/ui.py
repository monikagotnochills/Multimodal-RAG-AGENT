import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Brand Guardian AI", page_icon="🛡️", layout="centered")

st.title("🛡️ Compliance Audit Agent")
st.markdown("Enter a YouTube URL to check for regulatory and compliance violations.")

# 2. User Input
video_url = st.text_input("YouTube Video URL", placeholder="https://youtube.com/watch?v=...")

# 3. Action Logic
if st.button("Run Compliance Audit"):
    if not video_url:
        st.warning("Please enter a URL first.")
    else:
        with st.spinner("Analyzing video... (this may take a few minutes)"):
            try:
                # Replace with your actual Azure App Service URL
                backend_url = "https://your-azure-backend-name.azurewebsites.net/audit"
                
                # Call your backend API
                response = requests.post(backend_url, json={"video_url": video_url})
                result = response.json()
                
                # 4. Display Results
                if response.status_code == 200:
                    st.success("Audit Complete!")
                    st.subheader("Summary")
                    st.write(result.get("summary", "No summary provided."))
                    
                    violations = result.get("violations", [])
                    if violations:
                        st.error("⚠️ Violations Detected:")
                        for v in violations:
                            st.write(f"- {v}")
                    else:
                        st.balloons()
                        st.info("✅ No violations found.")
                else:
                    st.error(f"Audit Failed: {result.get('error', 'Unknown error')}")
            except Exception as e:
                st.error(f"Could not connect to backend: {e}")