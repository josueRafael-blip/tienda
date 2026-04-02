import streamlit as st

st.set_page_config(page_title="Tienda Online", layout="wide")

# -------- CARRITO --------
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# -------- MENÚ PRINCIPAL --------
st.sidebar.title("🛍️ Menú")
menu = ["Inicio", "Hombres", "Mujeres", "Ofertas", "Carrito", "Contacto"]
seccion = st.sidebar.radio("Ir a:", menu)

# -------- FUNCION PRODUCTO --------
def producto(nombre, precio, img):
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.image(img, use_container_width=True)
    
    with col2:
        st.subheader(nombre)
        st.write(f"💲{precio}")
        if st.button(f"Agregar {nombre}"):
            st.session_state.carrito.append((nombre, precio))
            st.success("Agregado al carrito")

# -------- INICIO --------
if seccion == "Inicio":
    st.title("👕 Tienda Online de Ropa")
    st.write("Explora nuestras categorías:")
    st.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8", use_container_width=True)

# -------- HOMBRES --------
elif seccion == "Hombres":
    st.title("👔 Hombres")
    
    sub = st.selectbox("Categoría", ["Polos", "Camisas", "Zapatillas"])
    
    if sub == "Polos":
        producto("Polo básico", 35, "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab")
        producto("Polo deportivo", 45, "https://images.unsplash.com/photo-1512436991641-6745cdb1723f")

    elif sub == "Camisas":
        producto("Camisa formal", 80, "https://http2.mlstatic.com/D_NQ_NP_977591-MPE105977808212_022026-O-camisa-formal-a-rayas-de-hombre.webp")
        producto("Camisa casual", 60, "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf")

    elif sub == "Zapatillas":
        producto("Zapatillas urbanas", 120, "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77")
        producto("Zapatillas deportivas", 140, "https://images.unsplash.com/photo-1519741497674-611481863552")

# -------- MUJERES --------
elif seccion == "Mujeres":
    st.title("👗 Mujeres")
    
    sub = st.selectbox("Categoría", ["Blusas", "Vestidos", "Tacones"])
    
    if sub == "Blusas":
        producto("Blusa elegante", 50, "https://images.unsplash.com/photo-1520975916090-3105956dac38")
    
    elif sub == "Vestidos":
        producto("Vestido rojo", 90, "https://images.unsplash.com/photo-1490481651871-ab68de25d43d")
    
    elif sub == "Tacones":
        producto("Tacones negros", 110, "https://images.unsplash.com/photo-1519741497674-611481863552")

# -------- OFERTAS --------
elif seccion == "Ofertas":
    st.title("🔥 Ofertas")
    
    sub = st.selectbox("Tipo", ["Descuentos", "Liquidación"])
    
    if sub == "Descuentos":
        producto("Polo en descuento", 20, "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab")
    
    elif sub == "Liquidación":
        producto("Camisa liquidación", 30, "https://images.unsplash.com/photo-1520975922284-8b456906c813")

# -------- CARRITO --------
elif seccion == "Carrito":
    st.title("🛒 Carrito de compras")
    
    total = 0
    for item in st.session_state.carrito:
        st.write(f"{item[0]} - S/ {item[1]}")
        total += item[1]
    
    st.subheader(f"Total: S/ {total}")

# -------- CONTACTO --------
elif seccion == "Contacto":
    st.title("📞 Contacto")
    st.write("WhatsApp: 999 999 999")
    st.write("Correo: tienda@email.com")
    st.write("Ubicación: Lima, Perú")
