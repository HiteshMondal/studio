import streamlit as st
import requests
from PIL import Image
import io

# -----------------------------
# Utility
# -----------------------------
def download_image(url: str) -> bytes | None:
    """Download image from a given URL and return raw bytes, or None if failed."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content
    except Exception as e:
        st.warning(f"⚠️ Could not download image: {e}")
        return None

# -----------------------------
# Main Renderer
# -----------------------------
def render_image_preview(result: dict) -> None:
    """Render the generated images in a grid layout with download options."""

    if not result or "images" not in result or not result["images"]:
        st.error("🚫 No images available to display.")
        return

    st.markdown("## 🖼️ Generated Images")

    # Arrange in columns (max 3 per row for better readability)
    images = result["images"]
    num_cols = min(3, len(images))
    
    rows = [images[i:i+num_cols] for i in range(0, len(images), num_cols)]

    for row in rows:
        cols = st.columns(len(row))
        for idx, (col, image_data) in enumerate(zip(cols, row), start=1):
            with col:
                # Ensure image data has a URL
                if "url" not in image_data:
                    st.error("❌ Invalid image data.")
                    continue

                image_bytes = download_image(image_data["url"])
                if not image_bytes:
                    st.error("❌ Failed to load image.")
                    continue

                # Display image
                st.image(image_bytes, caption=f"✨ Image {idx}", use_container_width=True)

                # Prepare PIL image for download
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format=image.format or "PNG")
                    img_byte_arr = img_byte_arr.getvalue()

                    # Download button
                    st.download_button(
                        label="💾 Download",
                        data=img_byte_arr,
                        file_name=f"adsnap_generated_{idx}.png",
                        mime="image/png",
                        use_container_width=True
                    )
                except Exception as e:
                    st.warning(f"⚠️ Error preparing image for download: {e}")

    # Show extra API details (excluding image blobs)
    with st.expander("🔍 Image Generation Metadata"):
        st.json({k: v for k, v in result.items() if k != "images"})
