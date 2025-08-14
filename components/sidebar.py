import streamlit as st

def get_config():
    """Render and return user configuration from sidebar settings."""

    # Default config values
    config = {
        "create_packshot": False,
        "add_shadow": False,
        "lifestyle_shot": False,
        "background_color": "#FFFFFF",
        "shadow_type": "natural",
        "scene_description": "",
        "num_results": 1,
        "aspect_ratio": "1:1",
        "sync": True,
    }

    # -------------------------------
    # Sidebar Layout
    # -------------------------------
    st.sidebar.title("⚙️ Configuration Panel")

    # 📸 Image Generation
    with st.sidebar.expander("🖼️ Image Generation", expanded=True):
        config["num_results"] = st.slider("Number of Results", 1, 4, 1)
        config["aspect_ratio"] = st.selectbox(
            "Aspect Ratio",
            ["1:1", "16:9", "9:16", "4:3", "3:4"],
            index=0,
        )
        config["sync"] = st.checkbox("⏳ Wait for Results", True)

    # 📦 Packshot
    with st.sidebar.expander("📦 Packshot Settings"):
        config["create_packshot"] = st.checkbox(
            "Enable Packshot",
            help="Generate a clean, professional product packshot"
        )
        if config["create_packshot"]:
            config["background_color"] = st.color_picker(
                "Background Color",
                "#FFFFFF",
                help="Choose the background color for your packshot"
            )

    # 🌑 Shadow
    with st.sidebar.expander("🌑 Shadow Options"):
        config["add_shadow"] = st.checkbox(
            "Enable Shadow",
            help="Add shadow to the product image for realism"
        )
        if config["add_shadow"]:
            config["shadow_type"] = st.radio(
                "Shadow Type",
                ["Natural", "Drop"],
                horizontal=True
            ).lower()

    # 🏞️ Lifestyle Shot
    with st.sidebar.expander("🏞️ Lifestyle Shot"):
        config["lifestyle_shot"] = st.checkbox(
            "Generate Lifestyle Shot",
            help="Place product in a real-world environment"
        )
        if config["lifestyle_shot"]:
            config["scene_description"] = st.text_area(
                "Scene Description",
                placeholder="E.g., modern kitchen countertop with natural light",
                help="Describe the environment for the lifestyle shot"
            )

    return config
