def remove_uppercase(s):
    return ''.join(char for char in s if not char.isupper())
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'