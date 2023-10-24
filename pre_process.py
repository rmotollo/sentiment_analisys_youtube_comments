from bs4 import BeautifulSoup
import re 

def clean_text(text):
    """
    Função para limpar o texto de entrada, removendo tags HTML e caracteres indesejados.
    """
    
    # Remova tags HTML usando BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()
    
    # Remova caracteres indesejados usando regular expressions
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remova espaços em branco duplos usando regular expressions
    text = re.sub(r'\s+', ' ', text)
    
   
    # Remove emoticons usando regular expressions
    emoticon_pattern = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    text = emoticon_pattern.sub(r'', text)
    
    
    # Remova outros caracteres indesejados aqui, se necessário
    
    return text