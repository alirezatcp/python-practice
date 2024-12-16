import json

json_str = '{"A": 2, "B": 4}' # a json object

python_dict = json.loads(json_str) # convert json object to python dict

print(python_dict, type(python_dict), sep='\n') # {'A': 2, 'B': 4}\n<class 'dict'>

# read from json file
with open('jsfile.json', 'r') as js_file:
    python_code = json.load(js_file) # convert json file to python dict

print(python_code, type(python_code), sep='\n') # {'object': 'dict', 'array': ['list', 'tuple'], 'str': 'str', 'Number': ['int', 'float'], 'true': True, 'false': False, 'null': None}\n<class 'dict'>

python_dict = {'a': 1, 'b': 2}
json_object = json.dumps(python_dict) # convert python dict to json object
print(json_object, type(json_object), sep='\n') # {"a": 1, "b": 2}\n<class 'str'>


python_dict = {
'dict': 'object', 
'list': ["array",], 
'str': 'str', 
'int': 123, 
"true": True, 
"false": False, 
"null": None
}
# write python_dict in a file named convert_to_json.json as a json file
with open('convert_to_json.json', 'w') as jsfile:
    write_command = json.dump(python_dict, jsfile, indent=4, sort_keys=True, separators=('kama','colon')) # indent=4: number of spaces from left, sort_keys=True: sort as alphabet, separators=('kama','colon'): use 'kama' as ','  and 'colon' as ':' in json file
print(write_command)