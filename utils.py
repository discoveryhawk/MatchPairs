async def get_formatted_time(seconds):
    return f'{seconds // 3600:02}:{seconds // 60:02}:{seconds % 60:02}'
