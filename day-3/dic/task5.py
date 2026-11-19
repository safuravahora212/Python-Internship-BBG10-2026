default_settings = {"theme": "light", "language": "english", "notifications": True}
user_settings = {"theme": "dark", "language": "gujarati"}

final_settings = {**default_settings, **user_settings}

print(final_settings)