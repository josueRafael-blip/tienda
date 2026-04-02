import streamlit as st

# Configuración de página
st.set_page_config(page_title="Moda Premium | Tienda Online", layout="wide", page_icon="🛍️")

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    /* Fondo y tipografía general */
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1f1f1f;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff4b4b;
        color: white;
    }
    /* Contenedor de producto */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# -------- ESTADO DEL CARRITO --------
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# -------- NAVEGACIÓN LATERAL --------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3159/3159614.png", width=100)
    st.title("StyleHub")
    st.markdown("---")
    menu = ["Inicio", "Hombres", "Mujeres", "Ofertas", "Carrito", "Contacto"]
    seccion = st.radio("Explorar categorías:", menu)
    st.markdown("---")
    st.info(f"Tienes {len(st.session_state.carrito)} artículos en el carrito.")

# -------- LÓGICA DE PRODUCTO OPTIMIZADA --------
def mostrar_producto(nombre, precio, img):
    with st.container():
        st.markdown(f"""
            <div class="product-card">
                <img src="{img}" style="width:100%; border-radius:8px; height:250px; object-fit:cover;">
                <h3 style="margin-top:15px;">{nombre}</h3>
                <p style="color: #ff4b4b; font-weight: bold; font-size: 20px;">S/ {precio}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Añadir al Carrito", key=nombre):
            st.session_state.carrito.append({"nombre": nombre, "precio": precio})
            st.toast(f"✅ {nombre} añadido")

# -------- SECCIONES --------
if seccion == "Inicio":
    st.markdown("<h1 style='text-align: center;'>✨ Nueva Colección 2026</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8", use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Envío Gratis", "Desde S/ 200")
    with col2:
        st.metric("Devoluciones", "Hasta 30 días")
    with col3:
        st.metric("Soporte", "24/7")

elif seccion in ["Hombres", "Mujeres"]:
    st.title(f"Sección de {seccion}")
    
    # Filtros visuales
    cats = ["Polos", "Camisas", "Calzado"] if seccion == "Hombres" else ["Blusas", "Vestidos", "Tacones"]
    sub = st.tabs(cats)

    # Ejemplo dinámico en la primera pestaña
    with sub[0]:
        col1, col2 = st.columns(2)
        with col1:
            mostrar_producto("Premium Cotton Tee", 45, "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab")
        with col2:
            mostrar_producto("Executive Shirt", 85, "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf")

elif seccion == "Carrito":
    st.title("🛒 Tu Selección")
    if not st.session_state.carrito:
        st.warning("Tu carrito está vacío. ¡Ve a buscar algo increíble!")
    else:
        total = sum(item['precio'] for item in st.session_state.carrito)
        for i, item in enumerate(st.session_state.carrito):
            c1, c2 = st.columns([4, 1])
            c1.write(f"🛍️ **{item['nombre']}**")
            c2.write(f"S/ {item['precio']}")
        
        st.divider()
        st.header(f"Total a pagar: S/ {total}")
        if st.button("Finalizar Compra"):
            st.balloons()
            st.success("¡Pedido realizado con éxito!")
            st.session_state.carrito = []

elif seccion == "Contacto":
    st.title("📩 Ponte en contacto")
    with st.form("contact_form"):
        st.text_input("Nombre")
        st.text_input("Correo electrónico")
        st.text_area("¿En qué podemos ayudarte?")
        st.form_submit_button("Enviar Mensaje")
    st.write("Correo: tienda@email.com")
    st.write("Ubicación: Lima, Perú")
