import streamlit as st
import magic
import io

# -----------------------------
# Utility
# -----------------------------
def is_valid_image(file_content: bytes) -> bool:
    """Check if uploaded file content is a valid image."""
    try:
        mime = magic.Magic(mime=True)
        file_type = mime.from_buffer(file_content)
        return file_type.startswith("image/")
    except Exception:
        return False


# -----------------------------
# Uploader Component
# -----------------------------
def render_uploader():
    """Render the image uploader with validation and preview."""
    
    st.markdown("## 📤 Upload Product Image")
    
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg"],
        help="Upload a product image to enhance, edit, or generate variations."
    )

    if uploaded_file is None:
        st.info("ℹ️ You can skip this step if you only want AI-generated images.")
        return None

    # Read file content
    file_content = uploaded_file.getvalue()

    # Validate image type
    if not is_valid_image(file_content):
        st.error("🚫 Invalid file type. Please upload a valid PNG, JPG, or JPEG image.")
        return None

    # Preview uploaded image
    st.image(
        file_content,
        caption=f"✅ Uploaded: {uploaded_file.name}",
        use_container_width=True
    )

    # Extra feedback
    st.success("Image uploaded successfully! 🎉")

    return uploaded_file
