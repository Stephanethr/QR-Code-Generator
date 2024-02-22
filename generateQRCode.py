# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:02:00 2023

@author: Stéphane Marchi
"""

# Importation des modules nécessaires
import qrcode
from flask import *

# Initialisation de l'application Flask
app = Flask(__name__)

def generer_qr_code(url, nom_fichier="qrcode.png"):
    """
    Génère un QR code à partir de l'URL fournie.

    Args:
    - url (str): L'URL à encoder dans le QR code.
    - nom_fichier (str): Le nom du fichier de sortie (par défaut, 'qrcode.png').

    Returns:
    - str: Chemin relatif du fichier généré.
    """
    # Création d'un objet QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Ajout de l'URL à l'objet QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Création d'une image QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Sauvegarde de l'image dans un fichier
    img.save(nom_fichier)

    return nom_fichier

# Route principale pour l'interface web
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupération de l'URL depuis le formulaire
        url = request.form['url']

        # Génération du QR code
        fichier_qr = generer_qr_code(url)

        # Retourne le fichier en téléchargement
        return send_file(fichier_qr, as_attachment=True)

    # Affiche la page d'accueil si la méthode est GET
    return render_template('index.html')

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(debug=True)

