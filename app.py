from autocorrect import spell
import random
from random import randint


def bin_alpha(alpha):
    bin_alpha = bin(ord(alpha))[2:]
    return  '0' * (8 - len(bin_alpha)) +  bin_alpha


def bin_secret(secret):
    bin_secret = ''
    for alpha in secret:
        bin_secret += bin_alpha(alpha)
    return bin_secret


def extract_secret(binary_secret):
    parsed = []
    part = ''
    step = 0
    for i in binary_secret:
        part += i
        step += 1
        if step == 8:
            if part != '00000000':
                parsed.append(part)
                part = ''
                step = 0

    secret = ''
    for part in parsed:
        secret += chr(int(part, 2))
    return secret


def make_a_dict():
    list='m q w e r t y i u o p a s d f g h j k l z x c v b n m q' #собл.цикличность
    list=list.split()
    d={}
    for i in range(1,len(list)-1):
        d[list[i]]=list[i+1]
    return(d) 
    

synonym={  #по версии онлайн-переводчика
    'studying' : 'education',
    'learning' : 'education',
    'teaching' : 'education',
    'training' : 'education',
    'doctrine' : 'education',
    'study' : 'educate',
    'learn' : 'educate',
    'train' : 'educate',
    'person': 'man' ,
    'man' : 'male', 
    'human' : 'male', 
    'husband' : 'male', 
    'guy' : 'male',
    'class' : 'lesson',
    'experience' :"lesson",
    'success' : 'luck', 
    'progress' : 'luck',
    'what' : 'which', 
    'who' : 'which',
    'pupils' : 'classmans', 
    'students' : 'learners',
    'schoolchilds' : 'students',
    'value' : 'meaning', 
    'role' : "meaning", 
    'importance' : 'meaning', 
    'existence' : 'living',
    'life' : 'living',
    'great' : 'grand',
    'world' : 'earth',
    'teacher' : 'tutor',
    'during' : 'in the process',
    'the' : 'a',
    'is' : 'be',
    'knowledge' : 'understanding',
    'experience' :'adventure',
    'of' : 'from',
    'grows' : 'develops',
    'passes' : 'goes',
    'significance' : 'relevancy',
    'to' : 'for',
    'in' : 'inside',
    'this' : 'that',
    'also' : 'too',
    'are' : 'is',
    'and': 'both',
    'become' : 'make',
    'emplloyees':'chief',
    'educated':'skilled' 
}


class Stego:
    def __init__(self, input_file, output_file, method, secret=None):
        self.input = input_file
        self.output = output_file
        self.method = method
        self.secret = secret

    def _registers_encode(self):
        secret = bin_secret(self.secret)
        with open(self.input, 'r') as file:
            data = file.read()
        data = data.lower()
        waste = [i for i in data]
        step = 0
        i = 0
        while i < len(secret):
            if waste[i + step].isalpha():
                if secret[i] == '1':
                    waste[i + step] = waste[i + step].upper()
                i += 1
            else:
                step += 1
        #return ''.join(waste)
        with open(self.output, 'w') as out:
            out.write(''.join(waste))

    def _registers_decode(self):
        secret = ''
        with open(self.input, 'r') as file:
            data = file.read()
        for i in data:
            if i.isalpha():
                if i.isupper():
                    secret += '1'
                else:
                    secret += '0'
        #return extract_secret(secret) #на выходе готовая строка
        with open(self.output, 'w') as out:
            out.write(extract_secret(secret))

    def _change_alphabet_encode(self):
        secret = bin_secret(self.secret)
        with open(self.input, 'r') as file:
            data = file.read()
        data = data.replace('е', 'e')

        waste = [i for i in data]
        step = 0
        i = 0
        while i < len(secret):
            if waste[i + step] == 'e': #english
                if secret[i] == '1':
                    waste[i + step] = 'е' #russian
                i += 1
            else:
                step += 1
        with open(self.output, 'w') as file:
            file.write(''.join(waste))

    def _change_alphabet_decode(self):
        secret = ''
        with open(self.input, 'r') as file:
            data = file.read()
        for i in data:
            if i == 'е':
                secret += '1'
            elif i == 'e':
                secret += '0'
        with open(self.out, 'w') as file:
            file.write(extract_secret(secret))

    def _spaces_in_the_end_encode(self):
        binary_secret = bin_secret(self.secret)
        result = list()
        with open(self.input, 'r') as file:
            for line_number, line in enumerate(file):
                if line_number < len(binary_secret):
                    space = int(binary_secret[line_number]) * " "
                    result.append(line.rstrip() + space + '\n')
                else:
                    result.append(line.rstrip() + '\n')
        with open(self.output, 'w') as file:
            for line in result:
                file.write(line)

    def _spaces_in_the_end_decode(self):
        binary_secret = ''
        with open(self.input, 'r') as file:
            for line in file:
                if len(line) > 1:
                    if line[-2] == ' ':
                        binary_secret += '1'
                    else:
                        binary_secret += '0'
                else:
                    binary_secret += '0'
        with open(self.output, 'w') as file:
            file.write(extract_secret(binary_secret))

    def _typos_encode(self):
        d = make_a_dict()
        message=bin_secret(self.secret)
        with open(self.input, 'r') as file:  
            text=file.read()
        newtext=''
        k=0
        j=0
        while k<len(text):
            if text[k-1]==' ' and text[k]!=' ' and j<len(message) or k==0:
                if message[j]=='1':
                    newtext+=text[k]+d[text[k].lower()]      
                else:
                    newtext+=text[k] 
                j+=1
            else:
                newtext+=text[k]
            k+=1
        with open(self.output, 'w') as file:
            file.write(newtext)

    def _typos_decode(self):
        k=0
        message=''
        with open(self.input, 'r') as file:
            text = file.read()
        while k<len(text):
            if text[k-1]==' ' and text[k]!=' ' or k==0 and  text[k].isalpha():
                word=''
                j=k
                while text[j]!=' ' and j<len(text)-1:
                    word+=text[j]
                    j+=1
                if word.lower()==spell(word).lower():
                    message+='0'
                else:
                    message+='1'
            else:
                pass
            k+=1
        #return extract_secret(message)
        with open(self.output, 'w') as file:
            file.write(extract_secret(message))

    def _punct_encode(self):
        possible_punct = ('!', ';')
        secret = bin_secret(self.secret)
        with open(self.input, 'r') as file:
            data = file.read().replace(';', '.').replace('!', '.')
        
        waste = [i for i in data]
        step = 0
        i = 0
        while i < len(secret):
            if waste[i + step] == '.': 
                if secret[i] == '1':
                    waste[i + step] = possible_punct[randint(0,1)] 
                i += 1
            else:
                step += 1
        #return ''.join(waste) #на выходе строка, которую нужно записать в файл
        with open(self.output, 'w') as file:
            file.write(''.join(waste))

    def _punct_decode(self):
        secret = ''
        with open(self.input, 'r') as file:
            data = file.read()
        for i in data:
            if i == '!' or i == ';':
                secret += '1'
            elif i == '.':
                secret += '0'
        #return extract_secret(secret) #на выходе готовый секрет
        with open(self.output, 'w') as file:
            file.write(extract_secret(secret))

    def _synonym_encode(self):
        message = bin_secret(self.secret)
        with open(self.input, 'r') as file:  
            text = file.read()
        newtext = ''
        symbols = 0
        symbolsofmes=0
        while symbols<len(text):
            word = ''
            if text[symbols-1]==' ' and text[symbols]!=' ' and symbolsofmes<len(message) or symbols==0:
                while text[symbols].isalpha():
                    word += text[symbols]
                    symbols += 1
                if message[symbolsofmes]=='1':
                    newtext += synonym[word.lower()]+text[symbols]
                else:
                    newtext+=word+text[symbols]
                symbolsofmes += 1
            else:
                newtext += text[symbols]
            symbols += 1
        with open(self.output, 'w') as file:
            file.write(newtext)

    def _synonym_decode(self):
        with open(self.input, 'r') as file:
            text = file.read()
        symbols = 0
        message = ''
        while symbols<len(text):
            word = ''
            if text[symbols-1]==' ' and text[symbols]!=' ' or symbols==0:
                while text[symbols].isalpha():
                    word += text[symbols]
                    symbols += 1
                if word.lower() in synonym.values():
                    message += '1'
                else:
                    message += '0'
            else:
                pass
            symbols += 1
        #return extract_secret(message)
        with open(self.output) as file:
            file.write(extract_secret(message))


if __name__ == "__main__":
    pass
    