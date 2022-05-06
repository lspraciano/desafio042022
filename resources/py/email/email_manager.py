# Native Imports
from flask_mail import Mail, Message

# Created Imports
from configuration.configuration import Configuration
# from controllers.user_controller import save_mail_token
from resources.py.token.token_manager import mail_token_generate

mail = Mail()


def send_cod_confirmation_register(email: str) -> dict:
    """
    Esta função envia um email com um token de 6 números gerados aleatoriamente e ao mesmo tempo salva no banco SQL
    este token no registro referente a ao email informado.

    :param email: email
    :return: {'success': 'mail sent'} para sucesso ao enviar ou {'error': 'send mail failed to send'} em caso de error
    """

    try:
        random_cod = mail_token_generate()
        body = f'''
        
        Aqui está o código solicitado:
    
       <<<  {random_cod}  >>> 
    
        '''

        msg = Message(
            subject='Sua senha de acesso.',
            sender=Configuration.MAIL_USERNAME,
            recipients=email.split(),
            body=body
        )

        mail.send(msg)
        # save_mail_token(email, random_cod)

        return {'success': 'mail sent'}

    except:
        return {'error': 'send mail failed to send'}
