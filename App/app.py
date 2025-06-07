import streamlit as st
from ifcFunctions import lista_de_materiais, abrir_ifc, renomear_paredes, ifc_file_to_bytes

def main():
    st.title("Projeto IFC Streamlit")

    file = st.file_uploader(
        "Carregar arquivo IFC",
        type=["ifc"],
        key="ifc_file_uploader"
    )

    if file:
        ifcFile = abrir_ifc(file)

        materiais = lista_de_materiais(ifcFile)
        st.dataframe(materiais, use_container_width=True)

        st.write(renomear_paredes(ifcFile))

        st.download_button(
            label="Baixar arquivo IFC modificado",
            data=ifc_file_to_bytes(ifcFile),
            file_name="ifc_modificado.ifc",
            mime="application/octet-stream"
        )




if __name__ == "__main__":
    main()