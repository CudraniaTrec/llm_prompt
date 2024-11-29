def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_case_str = ''.join(x.capitalize() for x in components)
    return camel_case_str
assert snake_to_camel('android_tv') == 'AndroidTv'
assert snake_to_camel('google_pixel') == 'GooglePixel'
assert snake_to_camel('apple_watch') == 'AppleWatch'