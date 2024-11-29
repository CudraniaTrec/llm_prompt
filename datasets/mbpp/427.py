#Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)