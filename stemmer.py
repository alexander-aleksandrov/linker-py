import re

class Stemmer:
    def __init__(self):
        #Setup dictionaries for stemming words of different parts of speech of russian language
        self.noun = ['иями', 'ями', 'ами', 'ией', 'иям', 'ием', 'иях', 'ев', 'ов', 'ие', 'ье', 'еи', 'ии', 'ей', 'ой', 'ий', 'ям', 'ем', 'ам', 'ом', 'ах', 'ях', 'ию', 'ью', 'ия', 'ья', 'а', 'е', 'и', 'й', 'о', 'у', 'ы', 'ь', 'ю', 'я']
        self.verb_gr1 = ['ете', 'йте', 'ешь', 'нно', 'ла', 'на', 'ли', 'ем', 'ло', 'но', 'ет', 'ют', 'ны', 'ть', 'й', 'л', 'н']
        self.verb_gr2 = ['ейте', 'уйте', 'ила', 'ыла', 'ена', 'ите', 'или', 'ыли', 'ило', 'ыло', 'ено', 'ует', 'уют', 'ены', 'ить', 'ыть', 'ишь', 'ей', 'уй', 'ил', 'ыл', 'им', 'ым', 'ен', 'ят', 'ит', 'ыт', 'ую', 'ю']
        self.perfective_gerund_gr1 = ['вшись', 'вши', 'в']
        self.perfective_gerund_gr2 = ['ившись', 'ывшись', 'ивши', 'ывши', 'ив', 'ыв']
        self.adjective = ['ими', 'ыми', 'его', 'ого', 'еых', 'ее', 'ие', 'ые', 'ое', 'ей', 'ий', 'ый', 'ой', 'ем', 'им', 'ым', 'ом', 'ых', 'ую', 'юю', 'ая', 'яя', 'ою', 'ею']
        self.participle_gr1 = ['ем', 'нн', 'вш', 'ющ', 'щ']
        self.participle_gr2 = ['ивш', 'ывш', 'ующ']
        self.reflexive = ['ся','сь']
        self.superlative = ['ейше', 'ейш']
        self.derivational = ['ость', 'ост']
        self.group_ending = ['а','я']
        self.noun_suffixes = ['иант', 'ионн', 'еньк', 'оньк', 'тел', 'енк', 'ечк', 'очк', 'ушк', 'юшк', 'ичк', 'ишк', 'ышк', 'щик', 'щиц', 'ник', 'ион', 'иат', 'иут', 'ищ', 'иш', 'иц', 'ок', 'от', 'нк', 'ск', 'ик', 'иц', 'к',]
        self.adj_suffixes = ['оват', 'еват', 'альн', 'ельн', 'ильн', 'ольн', 'юльн', 'ульн', 'чив', 'лив', 'ист', 'ьн', 'ск', 'ущ', 'ин']
    
def main():
    print(stemm("машина"))
    

def stemm(word):
    if not is_valid(word):
        return word
    for i in range(len(word)):
        if word[i] == "ё":
            word = word[:i] + "е" + word[i+1:]
        word = word.lower().strip()
    if is_exclution(word):
        return word
    prefix = ""
    rv = ""
    for i in range(len(word)):
        if word[i] == "ь":
            prefix = word[:i+2]
            rv = word[i+2:]
            break
        elif is_vowel(word[i]):
            rv = word[i+1:]
            prefix = word[:i+1]
            break
    if not rv:
        return prefix
    else:
        try:
            rv = step_1(rv)
        except Exception as e:
            try:
                with open("files/exclutions.txt", "a", encoding="utf-8") as f:
                    f.write(word+"\n")
            except Exception as e:
                print("Error writing to file")                  
            return word
    return prefix+rv

    
def step_1(word):
    for ending in Stemmer().perfective_gerund_gr1:
        if word.endswith(ending) and word[-len(ending)-1] in Stemmer().group_ending:
            return step_2(word[:-len(ending)])
    for ending in Stemmer().perfective_gerund_gr2:
        if word.endswith(ending):
            return step_2(word[:-len(ending)])
    for ending in Stemmer().reflexive:
        if word.endswith(ending):
            return step_2(word[:-len(ending)])
    for ending in Stemmer().adjective:
        if word.endswith(ending):
            word_adj = word[:-len(ending)]
            for ending in Stemmer().adj_suffixes:
                if word_adj.endswith(ending):
                    return step_2(word_adj[:-len(ending)])
            return step_2(word_adj)
    for ending in Stemmer().verb_gr1:
        if word.endswith(ending) and word[-len(ending)-1] in Stemmer().group_ending:
            return step_2(word[:-len(ending)-1])
    for ending in Stemmer().verb_gr2:
        if word.endswith(ending):
            return step_2(word[:-len(ending)])
    for ending in Stemmer().noun:
        if word.endswith(ending):
            word_noun = word[:-len(ending)]
            for ending in Stemmer().noun_suffixes:
                if word_noun.endswith(ending):
                    return step_2(word_noun[:-len(ending)])
            else:
                return step_2(word_noun)    
    else: 
        word_noun = word
        for ending in Stemmer().noun_suffixes:
            if word_noun.endswith(ending):
                return step_2(word_noun[:-len(ending)])
        else:
            return step_2(word_noun)   

def step_2(word):
    if word.endswith("и"):
        return step_3(word[:-1])
    else:
        return step_3(word)

def step_3(word):
    for ending in Stemmer().participle_gr1:
        if word.endswith(ending) and word[-len(ending)-1] in Stemmer().group_ending:
            return step_4(word[:-len(ending)-1])
    for ending in Stemmer().participle_gr2:
        if word.endswith(ending):
            return step_4(word[:-len(ending)])
    
    for ending in Stemmer().derivational:
        if word.endswith(ending):
            return step_4(word[:-len(ending)])
    else:
        return step_4(word)
    
def step_4(word):
    if word.endswith("нн"):
        return word[:-1]
    for ending in Stemmer().superlative:
        if word.endswith(ending):
            word = word[:-len(ending)]
            if word.endswith("нн"):
                return word[:-1]
            else:
                return word
    if word.endswith("ь"):
        return word[:-1]
    else:
        return word


def is_exclution(word):
    with open("files/exclutions.txt", "r", encoding="utf-8") as f:
        for line in f:
            if word == line.strip():
                return True
    return False

# checks if word is cirillic    
def is_valid(word):
    if not re.fullmatch(r"[а-я]+", word.strip().lower()):
        return False
    elif len(word) <= 2:
        return False
    else:
        return True   

def is_vowel(ch):
    consonants = "бвгджзйклмнпрстфхцчшщъь"
    return True if ch not in consonants else False

if __name__ == "__main__":
    main()