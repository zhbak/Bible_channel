from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pandas import read_csv
from random import randrange

# Формирует промпт и делает запрос, возвращает ответ LLM
def bible_message(system, user_input, llm):

    # system - текст системного промпта
    # user_input - текст пользовательского промпта
    # llm - llm модель

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"{system}"),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({"input" : f"{user_input}"})

    return response

# Функция для экстракта части текста библии из подготовленного csv файла
def bible_text_extraction(csv_file, segment):
    table = read_csv(csv_file)
    length = len(table)
    start_index = randrange(length-segment)
    result = table[start_index:start_index+segment]
    text = result.to_string(header=False, index=False)
    return text