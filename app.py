import streamlit as st

st.set_page_config(page_title="Tienda Online de Ropa", layout="wide")

st.sidebar.title("🛍️ Menú")
menu = ["Inicio", "Hombres", "Mujeres", "Ofertas", "Carrito de compras", "Contacto"]
opcion = st.sidebar.radio("Ir a:", menu)

# INICIO
if opcion == "Inicio":
    st.title("👕 Tienda Online de Ropa")
    st.write("Bienvenido a nuestra tienda virtual.")
    st.image("https://images.unsplash.com/photo-1521334884684-d80222895322", use_container_width=True)

# HOMBRES
elif opcion == "Hombres":
    st.title("👔 Ropa para Hombres")
    st.write("Productos disponibles:")
    st.write("• Polos")
    st.write("• Camisas")
    st.write("• Zapatillas")

# MUJERES
elif opcion == "Mujeres":
    st.title("👗 Ropa para Mujeres")
    st.write("Productos disponibles:")
    st.write("• Blusas")
    st.write("• Vestidos")
    st.write("• Tacones")

# OFERTAS
elif opcion == "Ofertas":
    st.title("🔥 Ofertas")
    st.write("• Descuentos")
    st.write("• Liquidación")

# CARRITO
elif opcion == "Carrito de compras":
    st.title("🛒 Carrito de compras")
    st.write("Aquí aparecerán tus productos.")

# CONTACTO
elif opcion == "Contacto":
    st.title("📞 Contacto")
    st.write("WhatsApp: 999 999 999")
    st.write("Correo: tienda@email.com")
    st.write("Ubicación: Lima, Perú")
