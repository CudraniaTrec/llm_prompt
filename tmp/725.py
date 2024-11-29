def extract_quotation(s):
    result = []
    in_quote = False
    current = ""
    
    for char in s:
        if char == '"':
            if in_quote:
                result.append(current)
                current = ""
            in_quote = not in_quote
        elif in_quote:
            current += char
            
    return result
def extract_quotation(s):
    result = []
    in_quote = False
    current = ""
    
    for char in s:
        if char == '"':
            if in_quote:
                result.append(current)
                current = ""
            in_quote = not in_quote
        elif in_quote:
            current += char
            
    return result
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
assert extract_quotation("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []