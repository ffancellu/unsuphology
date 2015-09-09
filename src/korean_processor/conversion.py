#-*- coding: utf-8 -*-

table = {
            #initial ㅇ
            u'\u110b' : '',
            #empty tail
            u'\u11a7' : '',
            #white space
            u' ' : ' ',
            #consonants
            u'\u1100' : 'g',#lead ㄱ
            u'\u11a8' : 'k',#tail ㄱ
            u'\u1101' : 'kk',#lead ㄲ
            u'\u11a9' : 'k',#tail ㄲ
            u'\u11aa' : 'ks',
            u'\u1102' : 'n',#lead ㄴ
            u'\u11ab' : 'n',#tail ㄴ
            u'\u11ad' : 'nh',#tailㄴㅎ
            u'\u1103' : 'd',#lead ㄷ
            u'\u11ae' : 't',#tail ㄷ
            u'\u1104' : 'tt',#ㄸ
            u'\u1105' : 'r',#lead ㄹ
            u'\u11af' : 'r',#tail ㄹ
            u'\u11b0' : 'lk',
            u'\u11b1' : 'lm',
            u'\u11b2' : 'lp',
            u'\u11b3' : 'ls',
            u'\u11b4' : 'lt',
            u'\u11b5' : 'lp',
            u'\u11b6' : 'lh',
            u'\u1106' : 'm',#lead ㅁ
            u'\u11b7' : 'm',#tail ㅁ
            u'\u1107' : 'b',#lead ㅂ
            u'\u11b8' : 'p',#tail ㅂ
            u'\u1108' : 'pp',#ㅃ
            u'\u11b9' : 'ps',#tailㅂㅅ
            u'\u1109' : 's',#lead ㅅ
            u'\u11ba' : 's',#tail ㅅ
            u'\u110a' : 'ss',#lead ㅆ
            u'\u11bb' : 'ss',#tail ㅆ
            u'\u11bc' : 'ng',#tail ㅇ
            u'\u110c' : 'j',#lead ㅈ
            u'\u11bd' : 't',#tail ㅈ
            u'\u110d' : 'jj',#ㅉ
            u'\u110e' : 'ch',#lead ㅊ
            u'\u11be' : 't',#tail ㅊ
            u'\u110f' : 'k',#lead ㅋ
            u'\u11bf' : 'k',#tail ㅋ
            u'\u1110' : 't',#lead ㅌ
            u'\u11C0' : 't',#tail ㅌ
            u'\u1111' : 'p',#lead ㅍ
            u'\u11c1' : 'p',#tail ㅍ
            u'\u1112' : 'h',#lead ㅎ
            u'\u11c2' : 'h',#tail ㅎ
            #vowels
            u'\u1161' : 'a',
            u'\u1162' : 'ae',
            u'\u1163' : 'ya',
            u'\u1164' : 'yae',
            u'\u1165' : 'eo',
            u'\u1166' : 'e',
            u'\u1167' : 'yeo',
            u'\u1168' : 'ye',
            u'\u1169' : 'o',
            u'\u116a' : 'wa',
            u'\u116b' : 'wae',
            u'\u116c' : 'oe',
            u'\u116d' : 'yo',
            u'\u116e' : 'u',
            u'\u116f' : 'weo',
            u'\u1170' : 'we',
            u'\u1171' : 'wi',
            u'\u1172' : 'yu',
            u'\u1173' : 'eu',
            u'\u1174' : 'yi',
            u'\u1175' : 'i',
            #bugs
            u'\u1160' : 'i',
            u'\u115e' : 'eu',
            u'\u115f' : 'yi',
            # consonant clusters
            
            #TO DO:mapping this other range to the vowels

        }

lead_start = int(0x1100) - 1
vowel_start = int(0x1161) - 7 
tail_start = int(0x11a8) - 1

START = 44032

def break_const(word):

    array_ch = list()

    for block in word:
        if block != u' ':
            if block in map(lambda x: unicode(x),range(0,10)):
                array_ch.append(block)
            else: 
                tail = get_tail(block)
                vowel = get_vowel(block,ord(tail))
                lead = get_lead(block)
                if set(table.keys()).issuperset(set([tail,vowel,lead])):
                    # print lead
                    # print vowel
                    # print tail

                    array_ch.extend([lead,vowel,tail])

        elif block == u' ': array_ch.append(u' ')

    # print array_ch
    return array_ch

def get_tail(block):
    return unichr(tail_start + ((ord(block) - START) % 28))

def get_vowel(block,tail):
    #vowel = 1 + mod (Hangul codepoint − 44032 − tail, 588) / 28
    return unichr(vowel_start + (1 + (((ord(block) - 44032 - tail) % 588) / 28)))

def get_lead(block):
    #lead = 1 + int [ (Hangul codepoint − 44032)/588 ]
    return unichr(lead_start + (1 + int((ord(block) - 44032) / 588)))

def table_lookup(array_ch):
    latin_arr = []
    for x in array_ch:
        latin_arr.append(table[x]) if x in table.keys() else latin_arr.append(x)
    latin_str = ''.join(filter(lambda x:x!='',latin_arr))
    return latin_str

def wrapper(word):
    dec = break_const(word)
    lt_word = table_lookup(dec)
    return lt_word

if __name__=="__main__":
    lt_word = wrapper("없었습니까")
    print lt_word