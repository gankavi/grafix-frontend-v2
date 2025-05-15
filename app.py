import streamlit as st
import base64

# -------------------
# PAGE CONFIG
# -------------------
st.set_page_config(page_title="GraFix AI Studio - Prompt Builder", layout="wide")

# -------------------
# BANNER
# -------------------
st.markdown("""
    <div style="text-align:center;">
        <img src="https://raw.githubusercontent.com/gankavi/grafix-backend-v1/main/grafix-frontend-v1/grafix%20ai%20studio%20name.png" width="1300"/>
    </div>
""", unsafe_allow_html=True)

# -------------------
# STYLE WRITING FORMATS
# -------------------
story_styles = [
    "None", "Cinematic Descriptive", "Comic Panel Action", "Narrative Fantasy",
    "Photorealistic Description", "Surreal Dreamscape", "Sci-Fi Epic", "Mythical Tale",
    "Horror Vignette", "Cyberpunk Scene", "Steampunk World", "Oil Painting Description",
    "Portrait Art Detail", "Dark Gothic Style", "Vintage Aesthetic", "Nature Documentary Style"
]

styles = [
    "None", "Cinematic", "Portrait", "Fantasy Art", "Anime", "Expressive",
    "Digital Painting", "Comic", "Manga", "Pixel Art", "Cyberpunk",
    "Watercolor", "Line Art", "Ink Drawing", "Concept Art", "3D Render",
    "Low Poly", "Realistic", "Photorealistic", "Surrealism", "Dark Fantasy",
    "Dreamlike", "Noir", "Pop Art", "Graffiti", "stickers"
]

portrait_styles = [
    "None", "Classic Portrait", "Studio Portrait", "Environmental Portrait",
    "Cinematic Portrait", "Low Key", "High Key", "Character Portrait",
    "Glamour Portrait", "Artistic Portrait", "Realistic Portrait", "Hyper-realistic Portrait",
    "Anime-style Portrait", "Manga-style Portrait", "Vector-style Portrait",
    "Pixel Art Portrait", "Cyberpunk Portrait", "Sketch Portrait",
    "Minimalist Portrait", "Expressive Portrait", "Surreal Portrait", "Silhouette Portrait"
]

comic_styles = [
    "None", "Comic Panel", "Comic Page", "Manga Panel", "Speech Bubble",
    "Dynamic Lines", "Halftone Shadows", "Action Pose", "Superhero Comic",
    "Vintage Comic", "Modern Webtoon"
]

poses = ["None", "Standing", "Sitting", "Leaning", "Walking", "Running", "Jumping", "Dancing", "Flying", "Casting Magic", "Meditating", "Crouching", "Kneeling", "Lying Down", "Floating", "Stretching", "Fighting", "Posing"]

clothing = [
    "None", "Saree", "Lehenga", "Kurta", "Armor", "Kimono", "Hanbok", "Casual", "Cyberpunk",
    "Gothic", "Traditional", "Modern Suit", "Steampunk Outfit", "Robe", "Streetwear", "School Uniform", "Fantasy Armor"
]

backgrounds = ["None", "Palace", "Temple", "Forest", "Beach", "Studio", "Mountain", "Desert", "Cityscape", "Underwater", "Space", "Village", "Street", "Throne Room"]

countries = [
    "None", "South Indian", "North Indian", "Tamil", "Punjabi", "Japanese", "Korean", "Chinese",
    "African", "Arabian", "European", "Fantasy Kingdom", "Tribal", "Western", "Victorian", "Sci-Fi World"
]

objects = ["None", "Sword", "Shield", "Hoverbike", "Ancient Book", "Lamp", "Magic Staff", "Gun", "Camera", "Scroll", "Treasure Box"]

angles = ["None", "¾ View", "Profile", "Back View", "High Angle", "Low Angle", "Overhead", "Worm's Eye", "Eye Level"]

camera_setups = ["None", "Close-up", "Wide shot", "Drone shot", "Over-the-shoulder", "POV", "Tilt shot", "Tracking shot"]

lighting_setups = ["None", "Cinematic Lighting", "Backlight", "Soft Light", "Golden Hour", "Neon Lighting", "Rim Lighting"]

depth_of_field = ["None", "Shallow DOF", "Deep DOF", "Blurred Background", "Bokeh"]

lens_types = ["None", "Wide Angle", "Telephoto", "Macro", "Fisheye", "Tilt-shift"]

focus_distance = ["None", "Foreground Focus", "Midground Focus", "Background Focus"]

visual_tags = ["sharp focus", "high contrast", "soft lighting", "8k", "realistic", "vibrant colors", "moody atmosphere", "film grain"]

music_items = [
    "None", "Veena", "Mridangam", "Flute", "Tabla", "Guitar", "Sitar",
    "Violin", "Drums", "Tambourine", "Trumpet", "Piano", "Synthesizer",
    "Saxophone", "Harp", "Shehnai", "Dholak", "Bongo", "Microphone"
]

camera_models = [
    "None", "DSLR", "Mirrorless", "Canon EOS R5", "Nikon Z9",
    "Sony A7R IV", "Fujifilm X-T5", "RED Komodo", "ARRI Alexa Mini",
    "GoPro Hero", "iPhone 15 Pro", "Drone Cam", "Vintage Film Camera"
]

ad_types = [
    "None", "Magazine Ad", "TV Commercial", "Billboard", "Poster", "Web Banner", "Social Media Ad",
    "Flyer", "Brochure", "Packaging Design", "Product Mockup", "Movie Poster"
]

vehicles = [
    "None", "Bike", "Car", "Chariot", "Horse", "Spaceship", "Rickshaw", "Cart", "Boat", "Helicopter", "Drone", "Tank", "Hovercraft"
]

sea_creatures = [
    "None", "Fish", "Shark", "Dolphin", "Octopus", "Jellyfish", "Sea Turtle", "Mermaid", "Crab", "Sea Horse", "Whale", "Starfish"
]

ocean_elements = [
    "None", "Sea", "Thunderstorm", "River", "Waves", "Rain", "Stormy Sea", "Calm Lake"
]

# -------------------
# SIDEBAR UI
# -------------------
with st.sidebar:
    st.header("🎧 Prompt Settings")

    characters = st.text_area("Character(s)", "tiger")
    scene_action = st.text_area("Scene Narrative", "Walking in a forest with sunlight filtering")

    selected_style = st.selectbox("Art Style", styles)
    selected_portrait_style = st.selectbox("Portrait Style", portrait_styles)
    selected_comic_style = st.selectbox("Comic Style", comic_styles)

    selected_pose = st.selectbox("Pose", poses)
    selected_clothing = st.selectbox("Clothing", clothing)
    selected_background = st.selectbox("Background", backgrounds)
    selected_country = st.selectbox("Origin / Culture", countries)
    selected_object = st.selectbox("Object", objects)
    selected_angle = st.selectbox("Angle", angles)
    selected_camera = st.selectbox("Camera Setup", camera_setups)
    selected_lighting = st.selectbox("Lighting", lighting_setups)
    selected_dof = st.selectbox("Depth of Field", depth_of_field)
    selected_lens = st.selectbox("Lens Type", lens_types)
    selected_focus = st.selectbox("Focus Distance", focus_distance)
    selected_music_item = st.selectbox("🎶 Music Item", music_items)
    selected_camera_model = st.selectbox("📸 Camera Model", camera_models)
    selected_ad_type = st.selectbox("🗾 Ad Type", ad_types)
    selected_vehicle = st.selectbox("🚗 Vehicle", vehicles)
    selected_sea_creature = st.selectbox("🌊 Sea Creature", sea_creatures)
    selected_ocean_element = st.selectbox("🌧️ Water Element", ocean_elements)

# -------------------
# MAIN UI - RIGHT SIDE CONTROLS
# -------------------
col2, col3 = st.columns([2, 1])

with col3:
    st.markdown("### 📝 Story Prompt Style")
    selected_story_style = st.selectbox("", story_styles)

    st.markdown("### 🎨 Visual Enhancers")
    selected_tags = st.multiselect("", visual_tags, default=["sharp focus", "soft lighting"])

    st.markdown("### 🔬 LoRA Settings")
    lora_name = st.text_input("LoRA Name", "")
    lora_weight = st.slider("LoRA Weight", 0.5, 1.5, 1.0, 0.1)

    add_quality_tags = st.checkbox("Add quality boosters", value=True)

# -------------------
# STORY STYLE PROMPT GENERATOR
# -------------------
def generate_story_style_prompt(style, base):
    if style == "Cinematic Descriptive":
        return f"A visually stunning scene unfolds: {base}. The lighting is cinematic, the mood intense, and every detail hyper-focused."
    elif style == "Comic Panel Action":
        return f"A dynamic comic book panel explodes with action — {base}. The background pops with halftone ink, bold outlines, and motion lines."
    elif style == "Narrative Fantasy":
        return f"In a magical realm, {base} shine with enchanted glow. Each element feels lifted from an ancient tale."
    elif style == "Photorealistic Description":
        return f"A photorealistic rendering of {base}, detailed with crisp lighting, real textures, and lifelike depth."
    elif style == "Surreal Dreamscape":
        return f"Inside a surreal dream, {base} float in warped perspectives and painted illusions."
    elif style == "Sci-Fi Epic":
        return f"Among stars and steel, {base} radiate futuristic power and neon edge in a galactic battlefield."
    elif style == "Mythical Tale":
        return f"Forged in myth, {base} appear as ancient beings blessed with divine light and history."
    elif style == "Horror Vignette":
        return f"In chilling silence, {base} emerge through shadows, evoking fear and suspense in dim candlelight."
    elif style == "Cyberpunk Scene":
        return f"Neon pulses. Rain falls. {base} stand in a tech-drenched, cyberpunk dystopia glowing with data."
    elif style == "Steampunk World":
        return f"Driven by steam and clockwork, {base} rise among brass gears and mechanical marvels."
    elif style == "Oil Painting Description":
        return f"Rendered in rich oils, {base} take shape with expressive brushwork and dramatic contrast."
    elif style == "Portrait Art Detail":
        return f"A detailed portrait of {base}, painted with focus on expression, lighting, and composition."
    elif style == "Dark Gothic Style":
        return f"Gothic arches and cold stone walls frame {base}, draped in mystery and melancholy."
    elif style == "Vintage Aesthetic":
        return f"Through a vintage lens, {base} appear timeless, styled like a 1950s photograph."
    elif style == "Nature Documentary Style":
        return f"As if narrated by Attenborough, {base} move gracefully within untouched landscapes."
    else:
        return base

# -------------------
# GENERATE PROMPT
# -------------------

# Center-aligned button using column trick
center_col2, right_col3 = st.columns([2, 1])
with col2:
    if st.button("✨ Generate Prompt", use_container_width=True):
        st.session_state.generated_prompt = True

# Show info if button not clicked yet
with col2:
    if "generated_prompt" not in st.session_state:
        st.info("💡 Fill out the prompt settings and click ✨ Generate Prompt")

# Proceed if generated_prompt was triggered
with col2:
   if "generated_prompt" in st.session_state:
    prompt_parts = [
        characters,
        scene_action,
        f"({selected_pose})" if selected_pose != "None" else "",
        f"wearing ({selected_clothing})" if selected_clothing != "None" else "",
        f"from ({selected_country})" if selected_country != "None" else "",
        f"holding ({selected_object})" if selected_object != "None" else "",
        f"angle: ({selected_angle})" if selected_angle != "None" else "",
        f"camera: ({selected_camera})" if selected_camera != "None" else "",
        f"{selected_dof}" if selected_dof != "None" else "",
        f"lighting: ({selected_lighting})" if selected_lighting != "None" else "",
        f"lens: ({selected_lens})" if selected_lens != "None" else "",
        f"focus: ({selected_focus})" if selected_focus != "None" else "",
        f"in a ({selected_background})" if selected_background != "None" else "",
        f"({selected_style} style)" if selected_style != "None" else "",
        f"{selected_portrait_style}" if selected_portrait_style != "None" else "",
        f"{selected_comic_style}" if selected_comic_style != "None" else "",
        f"with ({selected_music_item})" if selected_music_item != "None" else "",
        f"shot on ({selected_camera_model})" if selected_camera_model != "None" else "",
        f"ad style: ({selected_ad_type})" if selected_ad_type != "None" else "",
        f"with ({selected_vehicle})" if selected_vehicle != "None" else "",
        f"featuring ({selected_sea_creature})" if selected_sea_creature != "None" else "",
        f"scene includes ({selected_ocean_element})" if selected_ocean_element != "None" else ""
    ]

    base_prompt = ", ".join([p for p in prompt_parts if p])

    if selected_tags:
        base_prompt = ", ".join([f"({tag})" for tag in selected_tags]) + ", " + base_prompt

    if add_quality_tags:
        base_prompt = "((masterpiece)), ((best quality)), ((highly detailed)), " + base_prompt

    if lora_name:
        base_prompt += f", <lora:{lora_name}:{lora_weight}>"

    final_prompt = generate_story_style_prompt(selected_story_style, base_prompt)
    negative_prompt = "low quality, blurry, bad anatomy, extra fingers, disfigured, watermark, text"

    st.subheader("✅ Positive Prompt")
    st.code(final_prompt, language="text")
    #st.download_button("⬇ Download Positive Prompt", final_prompt, file_name="positive_prompt.txt")

    st.subheader("❌ Negative Prompt")
    st.code(negative_prompt, language="text")
    #st.download_button("⬇ Download Negative Prompt", negative_prompt, file_name="negative_prompt.txt")


footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #111;
    color: white;
    text-align: center;
    padding: 8px;
    font-size: 14px;
    z-index: 999;
}
.footer img {
    height: 16px;
    vertical-align: middle;
    margin-right: 6px;
}
</style>
<div class="footer">
    <img src="https://raw.githubusercontent.com/gankavi/grafix-backend-v1/main/grafix-frontend-v1/images/G%20logo%20for%20favicon.jpg" alt="G Logo">
    GraFix AI Studio Advanced Prompt Engine V-1. Powered by: <strong>GraFix</strong>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
