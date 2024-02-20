import together 
import json 


SYSTEM_PROMPT = "You are an intelligent programming assistant. You are an expert in SQL."
OUTPUT_FILENAME = 'processed_data.jsonl'

def process_data(filename: str, mode: str) -> None: 
    f_input = open(filename, 'r')
    data = json.loads(f_input.read())

    f_output = open(OUTPUT_FILENAME, mode)

    for value in data:  
        question = value['question']
        if "\"" in question: question = question.replace("\"", "'")
        if "\t" in question: question = question.replace("\t", " ")

        query = value['query'] if 'query' in value else value['SQL']
        if "\"" in query: query = query.replace("\"", "'")
        if "\t" in query: query = query.replace("\t", " ")

        conversion = """{}"text":"<s>[INST] <<SYS>>\\n{} \\n<</SYS>>\\n\\n{} [/INST] {}</s>"{}\n""".format("{", SYSTEM_PROMPT, question, query, "}")
        f_output.write(conversion)

    f_input.close()
    f_output.close()

def check_file(): 
    resp = together.Files.check(OUTPUT_FILENAME)
    return resp

def upload_file(): 
    resp = together.Files.upload(OUTPUT_FILENAME)
    return resp['id']

if __name__ == '__main__':
    # process_data('spider/train_spider.json', 'w')
    # process_data('spider/dev.json', 'a')
    # process_data('spider/dev2.json', 'a')

    print(check_file())
    print(upload_file())
    # print(together.Files.list()['data'])
    
    


