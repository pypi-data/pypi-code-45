
__all__ = ['sbjVrbAgreement', 'fragmentSent', 'modalRuleError', 'PrpDonot', 'VrbTenseAgreementError', 'a_an_error', 'realWrds', 'symSentSim', 'motionVerbs', 'coherentWrds', 'hyponymPolysem_cnt', 'concretMeaningPOS', 'vocabSize', 'commonWrd']

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from nltk import word_tokenize, sent_tokenize, pos_tag, FreqDist
from nltk.corpus import stopwords as sw, cmudict, wordnet as wn, brown
import re
from nltk.stem import WordNetLemmatizer
from essay_eval.lookup import helpingVrbs, comparisonWrds, additionWrds, exemplificationWrds, sequencing, result, contrast, qualifying, reformulation, highlighting, transition, cohesiveWrds, causalVerbs, mrc_psycholing
#remove in prod
import os
from nltk.parse.stanford import StanfordDependencyParser
import pandas as pd

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Look up data
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
helpingVrbs = helpingVrbs()
cohesiveWrds = cohesiveWrds()
causalVerbs = causalVerbs()
#Concreteness and Meaningfulness scores from MRC Psycholinguistic database.
mrc_psycholing = mrc_psycholing()

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Functions
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#function to remove punctuation
def remov_punct(withpunct):
    #punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    punctuations = set(['!','(',')','-','[',']','{','}',';',':',',','<','>','.','/','?','@','#','$','%','^','&','*','_','~',"\\"])
    without_punct = ""
    char = 'nan'
    for char in withpunct:
        if char not in punctuations:
            without_punct = without_punct + char
    return(without_punct)


#function to suppress stop words and special characters
def dropStopWrds(s):
    withoutpunct = remov_punct(s)
    stopWords = set(sw.words('english'))
    withStopwords = word_tokenize(withoutpunct)
    withoutStopwords = [w for w in withStopwords if not w in stopWords]
    return(withoutStopwords)

#function to count total words(including stop words)
def wrdCnt(s):
    withoutpunct = remov_punct(s)
    wrds = withoutpunct.split(' ')
    wrd_cnt = len(wrds)
    return(wrd_cnt)

#function to count correctly spelt words
def realWrds(s):
    realWrds = []
    withoutpunct = remov_punct(s)
    wrds = withoutpunct.split(' ')
    realwordCnt = len(set(wrds).intersection(set(words.words())))
    return(realwordCnt)       

#function to measure size of vocabulary post stop words suppression.
def vocabSize(s):
    withoutpunct = remov_punct(s)
    withoutStopwords = dropStopWrds(withoutpunct)
    vocabLen = len(set(withoutStopwords))
    return(vocabLen)

#function to count # sentences and paragraphs. This doesnt work when the period is not followed by a space. fix that later
def cntSentences(d):    
    sentences = nltk.sent_tokenize(d)    
    sentLen = len(sentences)
    return(sentLen)
 
#function to identify subject verb aggreement in number.
def sbjVrbAgreement(s):
    tag = pos_tag(word_tokenize(s))
    sbj_pos = ''
    vb_pos = ''
    agreement = 0
    NoAgreement = 0
    causal_verbs = 0
    causal_particles = 0
    for i in range(0,len(tag)):
       if re.search(r"N(N|S|P)",str(tag[i][1])):
           if (len(sbj_pos)==0):
             sbj_pos = str(tag[i][1])
       if re.search(r"VB(P|Z)",str(tag[i][1])):
           if (len(vb_pos)==0):
             vb_pos = str(tag[i][1])
       if (re.search(r"(CC|IN)",str(tag[i][1]))) or (str(tag[i][0]) in result):
           causal_particles += 1
       elif(str(tag[i][0]) in causalVerbs):
           causal_verbs += 1
    if(sbj_pos == '' or vb_pos == ''):
        agreement = agreement
    else:
        if((sbj_pos == 'NN' and vb_pos == 'VBZ') or (sbj_pos == 'NNS' and vb_pos == 'VBP') ):
            agreement = 1            
        elif((sbj_pos == 'NN' and vb_pos == 'VBP') or (sbj_pos == 'NNS' and vb_pos == 'VBZ') ):
            NoAgreement = 1
              
        else:
            agreement = agreement
       
    return(agreement,NoAgreement,causal_verbs,causal_particles)

#Function to identify fragmented sentence.
def fragmentSent(s):
    subj_flag = ''
    vb_flag = ''
    thought_flag = ''
    xAndFrag_flag = ''
    fragmented = 'n'
    subCc = ['after','although','as','as if','as long as','as soon as','as though','because','before','even if','even though','how','if','in case','in that','in order that','in so far as','just as','no matter how','now that','once','provided that','rather than','since','so','than','that','though','till','unless','until','when','whenever','where','whereas','where as','wherever','where ever','whether','while'];
    relPrn  = ['which','whichever','which ever','who','whoever','who ever','whom','whomever','whom ever','whose'];
    relAdverbs = ['when','where','why'];
    
    #checking if subj is present
    depParsed = standep_parser.raw_parse(s)
    depParsedNxt = depParsed.next()
    depParsedList = list(depParsedNxt.triples())
    for i in range(0,len(depParsedList)):
        dep = depParsedList[i][1]
        if (dep == "nsubj"):
            subj_flag = 'y'
        else:
            subj_flag = subj_flag
    #checking if verb is present
    tag = pos_tag(word_tokenize(s))
    for j in range(0,len(tag)):
        if re.search(r"VB.",str(tag[j][1])):
            vb_flag = 'y'
        else:
            vb_flag = vb_flag
    #checking if thought is completed    
    wrdTokens = word_tokenize(s)
    firstWrd = wrdTokens[0]
    matches1 = ''
    matches2 = ''
    matches3 = ''
    for w in subCc:    
        if (firstWrd == w):            
            matches1 = 'y'
        else:
            matches1 = matches1
    
    for w in relPrn:    
        if (firstWrd == w):            
            matches2 = 'y'
        else:
            matches2 = matches2
            
    for w in relAdverbs:    
        if (firstWrd == w):            
            matches3= 'y'
        else:
            matches3 = matches3        
    
    if ((len(matches1) + len(matches2) + len(matches3)) == 0):
        thought_flag = 'y'
    else:
        thought_flag = thought_flag
        
    #checking if there is X or FRAG at the root as it indicates fragmented sentence
    parsed = stanparser.raw_parse(s)
    for tree in parsed:
        if (tree[0].label() == 'X' or tree[0].label() == 'FRAG'):
            xAndFrag_flag = 'y'
        else:
            xAndFrag_flag = xAndFrag_flag
    
    if (subj_flag == 'y' and vb_flag == 'y' and thought_flag == 'y' and xAndFrag_flag != 'y'):
        fragmented = 'n'
    else:
        fragmented = 'y'
    return(fragmented)


#check if modal verb precendence holds good. Each part is optional, but modals always precede Have and Be, and Have always precedes Be.
def modalRuleError(s):
    wnlemma = WordNetLemmatizer()
    modalError = 0
    modalNoError = 0
    lemma2 = ''
    lemma_prev = ''
    lemma_prev2 = ''
    tag = pos_tag(word_tokenize(s))
    for i in range(0,len(tag)):
        if re.search(r"MD",str(tag[i][1])):           
            lemma_prev = wnlemma.lemmatize(str(tag[i-1][0]),pos='v')
            lemma_nxt = wnlemma.lemmatize(str(tag[i+1][0]),pos='v')
            if (lemma_prev == 'have' or lemma_prev == 'be'):
               modalError += 1
            elif (lemma_nxt == 'have' or lemma_nxt == 'be'):
               modalNoError += 1
        else:
           if re.search(r"VB(|.)",str(tag[i][1])):            
              lemma2 = wnlemma.lemmatize(str(tag[i][0]),pos='v')
              if (lemma2 == 'have'):
                 lemma_prev2 = wnlemma.lemmatize(str(tag[i-1][0]),pos='v')
                 lemma_nxt2 = wnlemma.lemmatize(str(tag[i+1][0]),pos='v')
                 if (lemma_prev2 == 'be'):
                     modalError += 1
                 elif(lemma_nxt2 == 'be'):
                     modalNoError += 1
    return(modalNoError,modalError)

#check if possessive pronoun is followed by "do". "he do not..", "he have not"
def PrpDonot(s):
    PrpDoNotNoError = 0
    PrpDoNotError = 0
    tag = pos_tag(word_tokenize(s))
    for j in range(0,len(tag)):
        if (re.search(r"PRP",str(tag[j][1]))):
            nxt_wrd = str(tag[j+1][0])
            if (nxt_wrd == 'do'):
                PrpDoNotError += 1
            elif(nxt_wrd == 'does'):
                PrpDoNotNoError += 1            
        else:
            PrpDoNotNoError = PrpDoNotNoError
            PrpDoNotError = PrpDoNotError
    return(PrpDoNotNoError, PrpDoNotError)

#check for helping verb and main verb tense agreement
def VrbTenseAgreementError(s):
    tenseError_flag = 'n'
    tense_hlp_vrb = 'n'
    tense_main_vrb = 'n'
    tag = pos_tag(word_tokenize(s))
    for i in range(0,len(tag)):
        if (set(helpingVrbs) & set(word_tokenize(tag[i][0]))):             
            tense_hlp_vrb = str(tag[i][1])            
            for j in range(i+1,len(tag)):
                if(re.search(r"VB(|.)",str(tag[j][1]))):
                    tense_main_vrb = str(tag[j][1])                    
                    if(tense_hlp_vrb == tense_main_vrb and tense_hlp_vrb == 'VBD' or tense_hlp_vrb == 'VBN'):
                        tenseError_flag = 'y'
                    if(tense_hlp_vrb == tense_main_vrb and tense_hlp_vrb == 'VBG' or tense_hlp_vrb == 'VBP'):
                        tenseError_flag = 'y'                
                    else:
                        tenseError_flag = tenseError_flag    
    return(tenseError_flag)

#check for "a" vs "an" before vowels.
def a_an_error(s):
    a_an_error = 0
    a_an_NoError = 0
    vowel_flag = 'n'
    wrds = word_tokenize(s)
    loaded_dict = cmudict.dict()
    for i in range(0,len(wrds)):
        try:
            frst_alpha = str(loaded_dict.get(wrds[i+1])[0][0])
        except:
            break
        if (wrds[i] == 'a' or wrds[i] == 'an'):
            frst_alpha = str(loaded_dict.get(wrds[i+1])[0][0])            
            if frst_alpha in ['a','e','i','o','u']:
                vowel_flag = 'y'
            if ((wrds[i] == 'a' and vowel_flag == 'y') or (wrds[i] == 'an' and vowel_flag == 'n')):
                a_an_error += 1
            elif ((wrds[i] == 'a' and vowel_flag == 'n') or (wrds[i] == 'an' and vowel_flag == 'y')):
                a_an_NoError += 1
        else:
            a_an_error = a_an_error
            a_an_NoError = a_an_NoError  
    return (a_an_NoError, a_an_error)            

#build a sentence similarity score.    
#Retrieve the POS tag
def ptb_to_wn(tag):    
    if tag.startswith('N'):
        return 'n' 
    if tag.startswith('V'):
        return 'v' 
    if tag.startswith('J'):
        return 'a' 
    if tag.startswith('R'):
        return 'r' 
    return None


def tagged_to_synset(word, tag):
    wn_tag = ptb_to_wn(tag)
    if wn_tag is None:
        return None 
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
    
    
def sentence_similarity(s1, s2):    
    s1 = pos_tag(word_tokenize(s1))
    s2 = pos_tag(word_tokenize(s2)) 
    
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in s1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in s2]
 
    #suppress "none"
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
    
    for synset in synsets1:
        best_score = max([synset.path_similarity(ss) for ss in synsets2])
        if best_score is not None:
            score += best_score
            count += 1
 
    # Average the values
    score /= count
    return score

#compute the symmetric sentence similarity
def symSentSim(s1, s2):
    sss_score = (sentence_similarity(s1, s2) + sentence_similarity(s2,s1)) / 2
    return (sss_score)

#coherent words per sentence
def coherentWrds(s):
    coherenceCnt = 0
    for i in range(0,len(cohesiveWrds)):
       match = re.search(cohesiveWrds[i],s)
       if match is not None:
          coherenceCnt += 1
          break
    return(coherenceCnt)

#hypernymy and polysemy
def hyponymPolysem_cnt(s):
    hyponyms_cnt = 0
    polysem_cnt = 0
    hyponym_perWrd = 0
    polysem_perWrd = 0
    wrds = dropStopWrds(s)
    for w in wrds:      
        wrd_synsets = wn.synsets(w)
        polysem_cnt += len(wrd_synsets)
        try:
            wrd = wrd_synsets[0]
            hyponyms = len(wrd.hyponyms())        
            hyponyms_cnt += hyponyms 
        except:
            next 
        hyponym_perWrd = hyponyms_cnt/len(wrds)
        polysem_perWrd = polysem_cnt/len(wrds)
    return(hyponym_perWrd,polysem_perWrd)
    
    
#This is at document level. Compute the avg frequency of the words used. This indicates how many frequently used words did the author use. This will have a correlation with the vocabulary size as well.
def commonWrd(d):
    sumWrdFreq = 0
    all_text = brown.words()
    wrdfreq = FreqDist([w.lower() for w in all_text])
    wrdlist = list(set(dropStopWrds(d)))
    for wrd in wrdlist:        
        sumWrdFreq += wrdfreq[wrd.lower()]
    commonWrds_Score = sumWrdFreq/float(len(wrdlist))
    return(commonWrds_Score)

#concreteness and meaningfulness scores
def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']
def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']
def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']
def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return wn.NOUN 

def concretMeaningPOS(s):
    wnlemma = WordNetLemmatizer()
    tag = pos_tag(word_tokenize(s))
    wrds = dropStopWrds(s)
    lemma_final = []
    concrete_denom = 0
    concreteSum = 0
    meaning_denom = 0
    meaningSum = 0
    adverbCnt = 0
    verbCnt = 0
    adjectiveCnt = 0
    nounCnt = 0    
    for i in range(0,len(tag)):
        if tag[i][0] in wrds:
            lemma = wnlemma.lemmatize(str(tag[i][0]),pos= penn_to_wn((tag)[i][1]))            
            lemma_final.append(str(lemma))
        #embedding the pos freq
        if (penn_to_wn((tag)[i][1]) == 'r'):
            adverbCnt += 1
        elif (penn_to_wn((tag)[i][1]) == 'v'):
            verbCnt += 1
        elif (penn_to_wn((tag)[i][1]) == 'a'):
            adjectiveCnt += 1
        elif (penn_to_wn((tag)[i][1]) == 'n'):
            nounCnt += 1        
    
    psycholin_match = set(lemma_final) & set(mrc_psycholing['WORD'].str.lower())   
    
    for j in lemma_final:
        if set({j}) & psycholin_match:
            concrete_denom += 1
            index_wrd = mrc_psycholing.loc[mrc_psycholing['WORD'].str.lower()==j].index[0]
            concreteSum += mrc_psycholing['CNC'].iloc[index_wrd]            
            if (mrc_psycholing['mean_meaningfulness'].iloc[index_wrd] > 0):
                meaning_denom += 1
                meaningSum = mrc_psycholing['mean_meaningfulness'].iloc[index_wrd]
    return(concreteSum,concrete_denom, meaningSum,meaning_denom, adverbCnt, verbCnt, adjectiveCnt,nounCnt)

#Spatial cohesion score.
def _recurse_all_hyponyms(synset, all_hyponyms):
    synset_hyponyms = synset.hyponyms()
    if synset_hyponyms:
        all_hyponyms += synset_hyponyms
        for hyponym in synset_hyponyms:
            _recurse_all_hyponyms(hyponym, all_hyponyms)

def all_hyponyms(synset):
    """Get the set of the tree of hyponyms under the synset"""
    hyponyms = []
    _recurse_all_hyponyms(synset, hyponyms)
    return hyponyms

#motion verbs using the above functions.
MotionVerbsList = []
for syn in wn.synsets('move'):
    if re.search(r'move.v.',str(syn)):
        listOfHyponyms = all_hyponyms(syn)
        for hypo in listOfHyponyms:
            MotionVerbsList.append(hypo.name().split('.')[0])
MotionVerbs = set(MotionVerbsList)

def motionVerbs(s):
    motionVerbsCnt = 0
    wnlemma = WordNetLemmatizer()#move this to the start of the evaluat function for efficiency
    tag = pos_tag(word_tokenize(s))
    wrds = dropStopWrds(s)    
    for i in range(0,len(tag)):
        if tag[i][0] in wrds:
            lemma = wnlemma.lemmatize(str(tag[i][0]),pos= penn_to_wn((tag)[i][1]))
            if str(lemma) in MotionVerbs:
                motionVerbsCnt += 1
                break
    return(motionVerbsCnt)
