from App import logic as lg

def print_menu(lenguage):
    print(f'\n{lenguage[0]}\n   {lenguage[1]}\n   {lenguage[2]}\n{lenguage[3]}\n{lenguage[21]}')

def lenguage_option():
    print('1) Español\n2) English\n3) Deutsch')
    option = input('--> ')
    try:
        return lg.lenguage(option)
    except:
        print('\n!!!\n')
        menu()
        
def account_searcher(lenguage, loader):
    print(f'\n{lenguage[4]}\n{lenguage[5]}')
    user = input('--> ')
    print(f'\n{lenguage[18]}...\n')
    profile = lg.bot_searcher(user)
    if profile:
        print(f'{lenguage[7]}: {profile.username}\n{lenguage[8]}: {profile.full_name}\n{lenguage[9]}: {profile.userid}\n{lenguage[10]}: {profile.followers}\n{lenguage[11]}: {profile.followees}\n{lenguage[12]}: {profile.mediacount}\n{lenguage[13]}: {profile.external_url}\n{lenguage[14]}: {profile.is_verified}\n{lenguage[15]}: {profile.is_business_account}\n{lenguage[16]}: {profile.is_private}\n{lenguage[17]}:\n{profile.biography}\n')
    else:
        print(f'{lenguage[6]}')

def user_login(lenguage):
    """Handles the user login flow. Returns the user's Profile object on success, None otherwise."""
    user = input(f"{lenguage[7]}: ")
    password = input(f"{lenguage[24]}: ")
    print(f'\n{lenguage[18]}...\n')
    status = lg.user_login(user, password)
    
    if status == '2FA':
        code = input(f"{lenguage[25]} 2FA: ")
        if not lg.user_login_2fa(code):
            print(f"{lenguage[26]}\n{lenguage[27]}")
            return None
    elif not status:
        print(f"{lenguage[26]}\n{lenguage[28]}")
        return None
    
    print(f"{lenguage[29]}!")
    # On successful login, get the profile object for the logged-in user
    return lg.bot_searcher(user)

def follow(profile, lenguage):
    print(f'{lenguage[22]}\n{lenguage[23]}')
    option = input('--> ')
    if option == '1':
        print(f'\n{lenguage[18]}...\n')
        followers, followees = lg.follow(profile)
        if followers is not None and followees is not None:
            print(f'{lenguage[10]}: {len(followers)}\n')
            for follower in followers:
                print(f'{lenguage[7]}: {follower.username}\n{lenguage[8]}: {follower.full_name}\n{lenguage[10]}: {follower.followers}\n{lenguage[16]}: {follower.is_private}\n')
            print(f'{lenguage[11]}: {len(followees)}\n')
            for followee in followees:
                print(f'{lenguage[7]}: {followee.username}\n{lenguage[8]}: {followee.full_name}\n{lenguage[10]}: {followee.followers}\n{lenguage[16]}: {followee.is_private}\n')
            
def logged_in_menu(profile, lenguage, loader):
    working = True
    while working:
        print(f'\n{lenguage[30]}')
        option = input('--> ')
        if option == '1':
            account_searcher(lenguage, loader)
        elif option == '2':
            follow(profile, lenguage)
        elif option == 'exit':
            working = False
        else:
            print(f'\n{lenguage[20]}\n')
            
def menu():
    lenguage = lenguage_option()
    loader = lg.loader
    working = True
    while working:
        if len(lenguage) == 0:
            print('\n!!!\n')
            menu()
        print_menu(lenguage)
        option = input('--> ')
        if option == '1':
            account_searcher(lenguage, loader)
        elif option == '2':
            profile = user_login(lenguage)
            if profile:
                logged_in_menu(profile, lenguage, loader)
        elif option == 'exit':
            print(f'{lenguage[19]}.')
            working = False
        elif option == 'leng':
            menu()
        else:
            print(f'\n{lenguage[20]}\n')
        
def main():
    menu()