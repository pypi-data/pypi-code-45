#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Invoke Libraries
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
from essay_eval.functions import *
import math

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Functions
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def buildFeatures(d):        
    vocab_size = 0
    sbjVrbAgreement_err = 0
    sbjVrbAgreement_noerr = 0
    sbjVrbAgreement_errscore = 0
    fragmentSent_err = 0
    fragmentSent_errscore = 0
    modalErrorCnt = 0
    modalNoErrorCnt = 0
    modalRule_errscore = 0
    PrpDoNotNoErrorCnt = 0
    PrpDoNotErrorCnt = 0
    PrpDonot_errscore = 0
    VrbTenseAgreement_errscore = 0
    a_an_NoErrorCnt = 0
    a_an_ErrorCnt = 0
    a_an_errscore = 0
    real_wrd = 0
    sss_score = 0
    cosine_score = 0
    coherenceCnt = 0
    coherence_score = 0
    hyponymCnt = 0
    hyponym_score = 0
    polysemCnt = 0
    polysem_score = 0
    commonWrd_score = 0
    concrete_sum = 0
    concrete_score = 0
    meaning_sum = 0
    meaning_score = 0
    causalVerb_score = 0
    causalParticle_score = 0
    causalVerbCnt = 0
    causalParticleCnt = 0
    motionVerbCnt = 0
    motionVerb_score = 0
    adverbCnt = 0
    verbCnt = 0 
    adjectiveCnt = 0
    nounCnt = 0
    adverb_score = 0
    verb_score = 0
    adjective_score = 0
    noun_score = 0    
    lcase = d.lower()
    sentences = lcase.split('.')
    no_of_sents = len(sentences)
    for i in range(0,len(sentences)):
        s = sentences[i]              
        vocab_size += vocabSize(s)             

        try:
            sub_verb_agre,sub_verb_notagre,causalVerb,causalParticle = sbjVrbAgreement(s)
            sbjVrbAgreement_noerr += sub_verb_agre
            sbjVrbAgreement_err += sub_verb_notagre
            causalVerbCnt += causalVerb
            causalParticleCnt += causalParticle
        except:
            sbjVrbAgreement_noerr = sbjVrbAgreement_noerr  
            sbjVrbAgreement_err = sbjVrbAgreement_err
            
        try:
            frag_sent = fragmentSent(s)
            if(frag_sent == 'y'):
               fragmentSent_err += 1
        except:
            fragmentSent_err = fragmentSent_err
        
        try:
            modalNoError,modalError = modalRuleError(s)
            modalNoErrorCnt += modalNoError
            modalErrorCnt += modalError
        except:
            modalNoErrorCnt = modalNoErrorCnt
            modalErrorCnt = modalErrorCnt
        try:
            PrpDoNotNoError,PrpDoNotError = PrpDonot(s)
            PrpDoNotNoErrorCnt += PrpDoNotNoError
            PrpDoNotErrorCnt += PrpDoNotError
        except:
            PrpDoNotNoErrorCnt = PrpDoNotNoErrorCnt
            PrpDoNotErrorCnt = PrpDoNotErrorCnt
        
        try:
            verb_tense_agree = VrbTenseAgreementError(s)
            if(verb_tense_agree == 'y'):
              VrbTenseAgreement_errscore += 1
        except:
            VrbTenseAgreement_errscore = VrbTenseAgreement_errscore
        
        try:
            a_an_NoError, a_an_Error = a_an_error(s)    
            a_an_NoErrorCnt += a_an_NoError
            a_an_ErrorCnt += a_an_ErrorCnt
        except:
            a_an_NoErrorCnt  = a_an_NoErrorCnt
            a_an_ErrorCnt = a_an_ErrorCnt
        
        try:
            real_wrd += realWrds(s)                   
        except:
            real_wrd = real_wrd
        
        if (i == 0):
            sss_score = sss_score
            cosine_score = cosine_score
        else:
            try:
               sss_score += symSentSim(s, sentences[i-1])    
            except:
                sss_score = sss_score                               
        
        try:
            motionVerbCnt += motionVerbs(s)
        except:
            motionVerbCnt = motionVerbCnt
            
        coherenceCnt += coherentWrds(s)
        hyponym, polysem =  hyponymPolysem_cnt(s)
        hyponymCnt += hyponym
        polysemCnt += polysem
        concret, concreteDenom ,meaning, meaningDenom, adverb, verb, adjective, noun = concretMeaningPOS(s)        
        concrete_sum += concret
        meaning_sum += meaning
        adverbCnt += adverb
        verbCnt += verb
        adjectiveCnt += adjective
        nounCnt += noun
    
    #start creating derived features(rational)    
    if (sbjVrbAgreement_err == 0 or sbjVrbAgreement_noerr == 0):
        sbjVrbAgreement_errscore = 0
    else:
        sbjVrbAgreement_errscore = math.log(sbjVrbAgreement_err/float(sbjVrbAgreement_noerr))
    
    
    if (fragmentSent_err/float(no_of_sents)) <= 0:
        fragmentSent_errscore = 0
    else:
        fragmentSent_errscore = math.log(fragmentSent_err/float(no_of_sents))
    
    if (modalNoErrorCnt == 0 or modalErrorCnt == 0):
        modalRule_errscore = 0
    else:
        modalRule_errscore = math.log(modalErrorCnt/float(modalNoErrorCnt))
    
    if (PrpDoNotNoErrorCnt == 0 or PrpDoNotErrorCnt == 0):
        PrpDonot_errscore = 0
    else:
        PrpDonot_errscore = math.log(PrpDoNotErrorCnt/float(PrpDoNotNoErrorCnt))
    
    if (a_an_NoErrorCnt == 0 or a_an_ErrorCnt == 0):
        a_an_errscore = 0
    else:
        a_an_errscore = math.log(a_an_ErrorCnt/float(a_an_NoErrorCnt))
    
    if (coherenceCnt == 0):
        coherence_score = 0
    else:
        coherence_score = math.log(coherenceCnt/float(no_of_sents))    
    
    if (no_of_sents == 1 or sss_score == 0):
        sss_score_avg = 0
        causalVerb_score = causalVerbCnt
        causalParticle_score = causalParticleCnt
    else:        
        sss_score_avg = math.log(sss_score/float(no_of_sents-1))
        if (causalVerbCnt == 0):
            causalVerb_score = 0
        else:
            causalVerb_score = math.log(causalVerbCnt/float(no_of_sents-1))
        if(causalParticle_score == 0):
            causalParticle_score = 0
        else:
            causalParticle_score = math.log(causalParticleCnt/float(no_of_sents-1))
    
    if (hyponymCnt == 0):
        hyponym_score = 0
    else:
        hyponym_score = math.log(hyponymCnt/float(no_of_sents))
    
    if (polysemCnt == 0):
        polysem_score = 0
    else:
        polysem_score = math.log(polysemCnt/float(no_of_sents))
    
    commonWrd_score = commonWrd(d)
    
    if (concrete_sum == 0):
        concrete_score = 0
    else:
        concrete_score = math.log(concrete_sum/float(no_of_sents))
        
    if (meaning_sum == 0):
        meaning_score = 0
    else:
        meaning_score = math.log(meaning_sum/float(no_of_sents))
        
    if (motionVerbCnt ==0):
        motionVerb_score = 0
    else:
        motionVerb_score = math.log(motionVerbCnt/float(no_of_sents))
    
    if (adverbCnt == 0):
        adverb_score = 0
    else:
        adverb_score = math.log(adverbCnt/float(no_of_sents))
    
    if (verbCnt == 0):
        verb_score = 0
    else:
        verb_score = math.log(verbCnt/float(no_of_sents))
    
    if (adjectiveCnt == 0):
        adjective_score = 0
    else:
        adjective_score = math.log(adjectiveCnt/float(no_of_sents))
    
    if (nounCnt == 0):
        noun_score = 0
    else:
        noun_score = math.log(nounCnt/float(no_of_sents))

    temp_feats = {'vocab_size':[vocab_size],'adverb_score':[adverb_score], 'verb_score':[verb_score], 'adjective_score':[adjective_score], 'noun_score':[noun_score], 'sbjVrbAgreement_errscore':[sbjVrbAgreement_errscore],'fragmentSent_errscore':[fragmentSent_errscore],'modalRule_errscore':[modalRule_errscore],'PrpDonot_errscore':[PrpDonot_errscore],'VrbTenseAgreement_errscore':[VrbTenseAgreement_errscore],'a_an_errscore':[a_an_errscore], 'sss_score_avg':[sss_score_avg],'coherence_score':[coherence_score],'hyponym_score':[hyponym_score],'polysem_score':[polysem_score],'commonWrd_score':[commonWrd_score], 'concreteness_score':[concrete_score], 'meaningfulness_score':[meaning_score], 'causalVerb_score':[causalVerb_score], 'causalParticle_score':[causalParticle_score],
 'motionVerb_score':[motionVerb_score]}

    return(temp_feats)

