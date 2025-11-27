import streamlit as st

st.sidebar.title("Menú")

opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["Página principal", "Registrar datos", "Consultar / Modificar", "Filtros", "Estadísticas"]
)

if opcion == "Página principal":
    st.title("Bienvenido a la App de Desempleo")
    st.write("Selecciona una opción en el menú lateral.")

elif opcion == "Registrar datos":
    st.title("Registrar datos")
    # (Aquí agregas tus inputs)

elif opcion == "Consultar / Modificar":
    st.title("Consultar / Modificar datos")
    # (Aquí agregas la lógica de búsqueda)

elif opcion == "Filtros":
    st.title("Filtros interactivos")
    # (Aquí agregas filtros + tabla + botón graficar)

elif opcion == "Estadísticas":
    st.title("Gráficos de estadísticas")
    # (Aquí agregas el módulo de visualización)