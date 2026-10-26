"""Fonctions d'envoi de messages."""


def send_mass_messages(message, user_list):
    """Envoie un message personnalisé à chaque utilisateur."""
    for user in user_list:
        mail_merge = {"name": user.name, "contact_info": user.contact_method}
        customised_message = message.format(**mail_merge)
        user.send(customised_message)
