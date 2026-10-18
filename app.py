import streamlit as st

st.set_page_config(page_title="Pregunta seria ❤️", page_icon="💌")

st.title("Un pequeño test sorpresa ✨")
st.write("Responde con total sinceridad...")

nivel_amor = st.slider("Del 1 al 100, ¿cuánto me amas?", min_value=0, max_value=100, value=0)

cita_favorita = st.radio(
    "¿Cuál es el mejor plan para un fin de semana juntos?",
    ["Ver películas y pedir comida", "Ver películas y cocinar juntos", "Salir a pasear y conocer", "Un dia en casa y un dia afuera", "Todas las anteriores"]
)
lo_que_le_gusta = st.text_area("¿Qué es lo que más te gusta de mí?")

mensaje = st.text_input("¿Qué es lo que más te gusta de nosotros?")

mensaje_final = st.text_input("Un último mensaje para mí:")

if st.button("Enviar respuestas"):
    st.divider()

    if nivel_amor < 80:
        st.warning(f"¿Solo {nivel_amor}%? ¿Tan poquito? :( Para eso di que no me amas...")
    else:
        st.balloons()
        st.success(f"¡Muy bien! Un {nivel_amor}% es aceptable. 🥰")

    if lo_que_le_gusta.strip():
        st.markdown(f"**Lo que más te gusta de mí:**\n> *\"{lo_que_le_gusta}\"*")
    else:
        st.error("Epa, ¡dejaste vacía la parte de qué te gusta de mí! 🤨")

    st.write(f"**Plan elegido:** {cita_favorita}")

    if mensaje_final.strip():
        st.info(f"Mensaje final registrado: *\"{mensaje_final}\"*")
    else:
        st.caption("No dejaste ningún mensaje escrito, sospechoso...")