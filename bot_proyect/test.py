import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()
# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'mrcrpro')


print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio:\n", profile.biography,profile.external_url)
print('Full Name: ', profile.full_name)
print('Verified: ', profile.is_verified)
print('Business: ', profile.is_business_account)
print('Private: ', profile.is_private)

# for i in profile.get_followers():
#    print(f'Username: {i.username}\nFull Name: {i.full_name}\nNumber of Posts: {i.mediacount}\nFollowers: {i.followers}\nPrivate: {i.is_private}')