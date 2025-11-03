import instaloader
import time
import random
loader = instaloader.Instaloader()


def lenguage(option):
    if option == '1':
        return [
            'Bienvenido', #0
            '1) Acceder con un bot', #1
            '2) Acceder con su cuenta propia', #2
            'Para salir digite "exit".', #3
            'Se va a comenzar la busqueda por bot.', #4
            'Por favor, digite correctamente el usuario', #5
            'No se han encontrado datos.', #6
            'Usuario', #7
            'Nombre', #8
            'ID de usuario', #9
            'Seguidores', #10
            'Seguidos', #11
            'Número de Publicaciones', #12
            'Links externos', #13
            'Cuenta Verificada', #14
            'Cuenta Empresarial', #15
            'Cuenta Privada', #16
            'Biografía', #17
            'Por favor, espere un momento', #18
            'Gracias por usar el programa', #19
            'Por favor, digite una opción válida', #20
            'Para cambiar el idioma digite "leng"', #21
            '¿Desea ver los seguidores/seguidos?', #22
            '1) Sí\n2) No', #23
            'Contraseña', #24
            'Código', #25
            'Error al iniciar sesión.', #26
            'Por favor, revise el código de autenticación.', #27
            'Por favor, revise las credenciales ingresadas.', #28
            'Inicio de sesión exitoso', #29
            '1) Buscar una cuenta\n2) Revisar seguidores/seguidos'
            ]
        
    elif option == '2':
        return [
    'Welcome',
    '1) Log in with a bot',
    '2) Log in with your own account',
    'To exit, type "exit".',
    'The search by bot will begin.',
    'Please type the username correctly',
    'No data found.',
    'Username',
    'Name',
    'User ID',
    'Followers',
    'Following',
    'Number of Posts',
    'External Links',
    'Verified Account',
    'Business Account',
    'Private Account',
    'Biography',
    'Please wait a moment',
    'Thank you for using the program',
    'Please type a valid option',
    'To change the language, type "leng"',
    'Would you like to see followers/following?',
    '1) Yes\n2) No']
        
    elif option == '3':
        return [
    'Willkommen',
    '1) Mit einem Bot anmelden',
    '2) Mit dem eigenen Konto anmelden',
    'Um das Programm zu beenden, geben Sie "exit" ein.',
    'Die Suche per Bot wird gestartet.',
    'Bitte geben Sie den Benutzernamen korrekt ein',
    'Keine Daten gefunden.',
    'Benutzername',
    'Name',
    'Benutzer-ID',
    'Follower',
    'Folgt',
    'Anzahl der Beiträge',
    'Externe Links',
    'Verifiziertes Konto',
    'Geschäftskonto',
    'Privates Konto',
    'Biografie',
    'Bitte warten Sie einen Augenblick',
    'Vielen Dank für die Nutzung des Programms',
    'Bitte geben Sie eine gültige Option ein',
    'Um die Sprache zu ändern, geben Sie "leng" ein',
    'Möchten Sie die Follower/gefolgten Personen sehen?',
    '1) Ja\n2) Nein']
        
    else:
        return []

def bot_searcher(user):
    try:
        return instaloader.Profile.from_username(loader.context, user)
    except instaloader.exceptions.ProfileNotExistException:
        return None


def user_login(user, password):
    try:
        loader.login(user, password)
        return True
    except instaloader.TwoFactorAuthRequiredException:
        return '2FA'
    except (instaloader.exceptions.BadCredentialsException, instaloader.exceptions.ConnectionException):
        return False

def user_login_2fa(code):
    """Returns True on success, False on failure."""
    try:
        loader.two_factor_login(code)
        return True
    except (instaloader.exceptions.BadCredentialsException, instaloader.exceptions.ConnectionException):
        return False
    
def follow(profile):
    """
    Fetches followers and followees with delays to avoid rate-limiting.
    Returns (followers, followees) on success, or (None, None) on a ConnectionException.
    """
    user_followers = []
    user_followees = []
    try:
        print("Fetching followers...")
        for follower in profile.get_followers():
            user_followers.append(follower)
            time.sleep(random.uniform(0.5, 1.5)) # Wait 0.5 to 1.5 seconds
        print("Fetching followees...")
        for followee in profile.get_followees():
            user_followees.append(followee)
            time.sleep(random.uniform(0.5, 1.5)) # Wait 0.5 to 1.5 seconds
        return user_followers, user_followees
    except instaloader.exceptions.ConnectionException as e:
        print(f"Error fetching data: {e}")
        return None, None

def username(profile):
    try:
        return profile.username
    except:
        return None

def user_id(profile):
    try:
        return profile.userid
    except:
        return None

def fullname(profile):
    try:
        return profile.full_name
    except:
        return None
    
def followers(profile):
    try:
        return profile.followers
    except:
        return None
    
def followees(profile):
    try:
        return profile.followees
    except:
        return None
    
def posts(profile):
    try:
        return profile.mediacount
    except:
        return None
    
def external_url(profile):
    try:
        return profile.external_url
    except:
        return None
    
def is_verified(profile):
    try:
        return profile.is_verified
    except:
        return None
    
def is_business(profile):
    try:
        return profile.is_business_account
    except:
        return None

def is_private(profile):
    try:
        return profile.is_private
    except:
        return None
    
def info_bio(profile):
    try:
        return profile.biography
    except:
        return None