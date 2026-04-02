import streamlit as st

st.set_page_config(page_title="Tienda Online", layout="wide")

# --- ESTILO CSS PARA DAR VIDA A LA TIENDA ---
st.markdown("""
    <style>
    /* Estilo para los botones de 'Agregar' */
    .stButton>button {
        background-color: #000000;
        color: white;
        border-radius: 20px;
        border: 1px solid #000000;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        border: 1px solid #ff4b4b;
        color: white;
    }
    /* Estilo para los títulos de sección */
    h1 {
        color: #1E1E1E;
        font-family: 'Helvetica', sans-serif;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    /* Contenedor de productos */
    [data-testid="stVerticalBlock"] > div:has(div.stImage) {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# -------- CARRITO --------
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# -------- MENÚ PRINCIPAL --------
st.sidebar.markdown("## 🛍️ **StyleHub**")
menu = ["Inicio", "Hombres", "Mujeres", "Ofertas", "Carrito", "Contacto"]
seccion = st.sidebar.radio("Navegar por la tienda:", menu)
st.sidebar.markdown("---")
st.sidebar.write(f"🛒 **Productos en carrito:** {len(st.session_state.carrito)}")

# -------- FUNCION PRODUCTO --------
def producto(nombre, precio, img):
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.image(img, use_container_width=True)
    
    with col2:
        st.subheader(nombre)
        st.markdown(f"<h3 style='color: #ff4b4b;'>S/ {precio}</h3>", unsafe_allow_html=True)
        if st.button(f"Agregar {nombre}"):
            st.session_state.carrito.append((nombre, precio))
            st.toast(f"✅ {nombre} añadido") # Feedback visual rápido

# -------- INICIO --------
if seccion == "Inicio":
    st.title("👕 Tienda Online de Ropa")
    st.markdown("### ¡Bienvenido! Explora nuestras categorías:")
    st.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8", use_container_width=True)
    st.divider()

# -------- HOMBRES --------
elif seccion == "Hombres":
    st.title("👔 Sección Hombres")
    
    sub = st.selectbox("¿Qué estás buscando hoy?", ["Polos", "Camisas", "Zapatillas"])
    st.markdown("---")
    
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
    st.title("👗 Sección Mujeres")
    
    sub = st.selectbox("Categoría", ["Blusas", "Vestidos", "Tacones"])
    st.markdown("---")
    
    if sub == "Blusas":
        producto("Blusa elegante", 50, "https://img.kwcdn.com/product/fancy/b59ffcc2-46b5-4b74-a97f-885552a1e6fe.jpg?imageMogr2/auto-orient%7CimageView2/2/w/800/q/70/format/webp")
    
    elif sub == "Vestidos":
        producto("Vestidos hermosos", 90, "https://images.unsplash.com/photo-1490481651871-ab68de25d43d")
    
    elif sub == "Tacones":
        producto("Tacones negros", 110, "https://m.media-amazon.com/images/I/61W5S3xfayL._AC_UF894,1000_QL80_.jpg")

# -------- OFERTAS --------
elif seccion == "Ofertas":
    st.title("🔥 Super Ofertas")
    
    sub = st.selectbox("Tipo", ["Descuentos", "Liquidación"])
    st.markdown("---")
    
    if sub == "Descuentos":
        producto("Polo en descuento", 20, "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab")
    
    elif sub == "Liquidación":
        producto("Camisa liquidación", 30, "https://images.unsplash.com/photo-1520975922284-8b456906c813")

# -------- CARRITO --------
elif seccion == "Carrito":
    st.title("🛒 Carrito de compras")
    
    total = 0
    if not st.session_state.carrito:
        st.info("Tu carrito está vacío.")
    else:
        for item in st.session_state.carrito:
            st.write(f"✅ {item[0]} - S/ {item[1]}")
            total += item[1]
        
        st.markdown("---")
        st.subheader(f"Total: S/ {total}")
        if st.button("Finalizar Pedido"):
            st.balloons()
            st.success("¡Gracias por tu compra!")

# -------- CONTACTO --------
elif seccion == "Contacto":
    st.title("📞 Información de Contacto")
    with st.container():
        st.info("Atendemos de Lunes a Sábado de 9:00 AM a 8:00 PM")
        st.write("💬 **WhatsApp:** 999 999 999")
        st.write("✉️ **Correo:** tienda@email.com")
        st.write("📍 **Ubicación:** Lima, Perú")
