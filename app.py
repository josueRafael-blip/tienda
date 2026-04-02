import streamlit as st

st.set_page_config(page_title="Tienda Online", layout="wide", page_icon="🛍️")

# -------- DISEÑO Y ESTILOS (CSS) --------
st.markdown("""
    <style>
    /* Fondo de la aplicación */
    .stApp {
        background-color: #f4f7f6;
    }
    
    /* Estilo para los botones de compra */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #1E1E1E;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #FF4B4B;
        color: white;
        transform: scale(1.02);
    }
    
    /* Tarjetas de productos (Contenedores) */
    [data-testid="stVerticalBlock"] > div:has(div.stImage) {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #efefef;
    }
    
    /* Títulos y textos */
    h1 {
        font-family: 'Inter', sans-serif;
        color: #1E1E1E;
        border-bottom: 2px solid #FF4B4B;
        padding-bottom: 10px;
    }
    
    .price-tag {
        color: #FF4B4B;
        font-size: 24px;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# -------- CARRITO --------
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# -------- MENÚ PRINCIPAL --------
with st.sidebar:
    st.markdown("# 🚀 Style Store")
    st.markdown("---")
    menu = ["Inicio", "Hombres", "Mujeres", "Ofertas", "Carrito", "Contacto"]
    seccion = st.sidebar.radio("Categorías principales:", menu)
    st.markdown("---")
    st.metric(label="Artículos en Carrito", value=len(st.session_state.carrito))

# -------- FUNCION PRODUCTO --------
def producto(nombre, precio, img):
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.image(img, use_container_width=True)
    
    with col2:
        st.subheader(nombre)
        st.markdown(f'<p class="price-tag">S/ {precio}</p>', unsafe_allow_html=True)
        # Botón con key única para evitar errores de Streamlit
        if st.button(f"🛒 Añadir {nombre}", key=f"btn_{nombre}_{precio}"):
            st.session_state.carrito.append((nombre, precio))
            st.toast(f"¡{nombre} agregado!") # Notificación flotante

# -------- INICIO --------
if seccion == "Inicio":
    st.title("👕 Nueva Temporada 2026")
    st.write("### La mejor moda a un click de distancia.")
    st.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8", use_container_width=True)
    st.info("💡 Tip: Revisa la sección de **Ofertas** para descuentos exclusivos.")

# -------- HOMBRES --------
elif seccion == "Hombres":
    st.title("👔 Moda Masculina")
    
    sub = st.selectbox("Selecciona un estilo:", ["Polos", "Camisas", "Zapatillas"])
    st.divider()
    
    if sub == "Polos":
        producto("Polo básico", 35, "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab")
        producto("Polo deportivo", 45, "https://images.unsplash.com/photo-1512436991641-6745cdb1723f")

    elif sub == "Camisas":
        producto("Camisa formal", 80, "https://mbo.com.pe/cdn/shop/files/CAMISAS_FORMALES_270x360@2x.webp?v=1774274537")
        producto("Camisa casual", 60, "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf")

    elif sub == "Zapatillas":
        producto("Zapatillas urbanas", 120, "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77")
        producto("Zapatillas deportivas", 140, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgyYVFQhJR9umcl67vAaKiUR9p8fDLFSb81g&s")

# -------- MUJERES --------
elif seccion == "Mujeres":
    st.title("👗 Moda Femenina")
    
    sub = st.selectbox("Categoría", ["Blusas", "Vestidos", "Tacones"])
    st.divider()
    
    if sub == "Blusas":
        producto("Blusa elegante", 50, "https://img.kwcdn.com/product/fancy/b59ffcc2-46b5-4b74-a97f-885552a1e6fe.jpg?imageMogr2/auto-orient%7CimageView2/2/w/800/q/70/format/webp")
    
    elif sub == "Vestidos":
        producto("Vestidos hermosos", 90, "https://images.unsplash.com/photo-1490481651871-ab68de25d43d")
    
    elif sub == "Tacones":
        producto("Tacones negros", 110, "https://m.media-amazon.com/images/I/61W5S3xfayL._AC_UF894,1000_QL80_.jpg")

# -------- OFERTAS --------
elif seccion == "Ofertas":
    st.title("🔥 Hot Sale")
    
    sub = st.selectbox("Ver ofertas de:", ["Descuentos", "Liquidación"])
    st.divider()
    
    if sub == "Descuentos":
        producto("Polo en descuento", 20, "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab")
    
    elif sub == "Liquidación":
        producto("Camisa liquidación", 30, "https://images.unsplash.com/photo-1520975922284-8b456906c813")

# -------- CARRITO --------
elif seccion == "Carrito":
    st.title("🛒 Tu Carrito")
    
    total = 0
    if not st.session_state.carrito:
        st.warning("Aún no has agregado productos.")
    else:
        for item in st.session_state.carrito:
            with st.expander(f"📦 {item[0]}"):
                st.write(f"Precio unitario: S/ {item[1]}")
            total += item[1]
        
        st.markdown("---")
        st.markdown(f"## Total: **S/ {total}**")
        if st.button("Confirmar Pedido y Pagar"):
            st.balloons()
            st.success("¡Pedido procesado con éxito!")
            st.session_state.carrito = []

# -------- CONTACTO --------
elif seccion == "Contacto":
    st.title("📞 Canal de Atención")
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("📱 WhatsApp: 999 999 999")
        st.info("✉️ Correo: tienda@email.com")
    with col_b:
        st.warning("📍 Ubicación: Lima, Perú")
        st.write("Horario: 9am - 8pm")
