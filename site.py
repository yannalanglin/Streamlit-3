import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()
if st.session_state["authentication_status"] is None:
    st.info("Username : root / Password : rootMDP")


#def accueil():
     # st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")

if st.session_state["authentication_status"]:
   
  
    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options = ["Accueil","📷Photos"]
        )
    # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
    # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Mon album photo")

        col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne : 
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")

# Contenu de la deuxième colonne :
        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

# Contenu de la troisième colonne : 
        with col3:
            st.header("An owl")
            st.image("https://static.streamlit.io/examples/owl.jpg")


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')



