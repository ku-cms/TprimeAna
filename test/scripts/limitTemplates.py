#!/usr/bin/env python
import sys,imp
import os
import ROOT as rt
from input_anaTp_cfi import *
from anaTp import *
from ABCDRegions_cfi import *

helper = imp.load_source('fix' , './help.py')

outFileName = sys.argv[1]

jetType = 'CHS' # The tree to be run over
QCDType = 'Pt' # Which QCD sample to run over: can be 'Pt' or 'HT'
do2015 = False
if 'tH' in outFileName:
    dotH = True
    dotZ = False
else:
    dotH = False
    dotZ = True

#isRegionA['ht']['Cuts'] = 'ht>1100 && @idxHTagged.size()==0 && @idxAntiHTagged.size()>0 && @idxTopTaggedM.size()==0 && ptAntiHTagged > 350' 
#isRegionB_mt['mtprimeDummy']['Cuts'] = 'ht>1100 && @idxHTagged.size()==0 && @idxAntiHTagged.size()>0 && @idxTopTaggedM.size()>0 && dR(etaAntiHTagged,phiAntiHTagged,etaTopTaggedM,phiTopTaggedM)>2.0 && ptAntiHTagged > 350 && ptTopTaggedM>500' 
#isRegionC['ht']['Cuts'] = 'ht>1100 && @idxHTagged.size()>0 && @idxAntiHTagged.size()>=0 && @idxTopTaggedM.size()==0 && ptHTagged > 350'
#isRegionD_mt['mtprime']['Cuts'] = 'ht>1100 && @idxHTagged.size()>0 && @idxAntiHTagged.size()>=0 && @idxTopTaggedM.size()>0 && dR(etaHTagged,phiHTagged,etaTopTaggedM,phiTopTaggedM)>2.0 && ptHTagged > 350 && ptTopTaggedM>500'
#isRegionA_mt['mtprimeDummyA']['Cuts'] += '&& Sum$(abs(etaAK4)>2.4)>0' 
#isRegionB_mt['mtprimeDummy']['Cuts'] += '&& Sum$(abs(etaAK4)>2.4)>0' 
#isRegionC_mt['mtprimeDummyC']['Cuts'] += '&& Sum$(abs(etaAK4)>2.4)>0' 
#isRegionD_mt['mtprime']['Cuts'] += '&& Sum$(abs(etaAK4)>2.4)>0'
#isRegionA_mt['mtprimeDummyA']['Cuts'] += '&& @ptExtraAK4.size()>0' 
#isRegionB_mt['mtprimeDummy']['Cuts'] += '&& @ptExtraAK4.size()>0' 
#isRegionC_mt['mtprimeDummyC']['Cuts'] += '&& @ptExtraAK4.size()>0' 
#isRegionD_mt['mtprime']['Cuts'] += '&& @ptExtraAK4.size()>0'
#isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L && @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0'

#isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0'
#isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0'
#
#isRegionA_mt_tZ['mtprimeATilde_tM_ZB']['Cuts'] = 'isRegionA_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0'
#isRegionB_mt_tZ['mtprimeBTilde_tM_ZB']['Cuts'] = 'isRegionB_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionC_mt_tZ['mtprimeCTilde_tM_ZB']['Cuts'] = 'isRegionC_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(ZAnul[2])&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0' 
#isRegionD_mt_tZ['mtprimeDTilde_tM_ZB']['Cuts'] = 'isRegionD_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(ZAnul[2])&& @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0'

#isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L&&Sum$(abs(etaAK4)>2.4)==00&&(ptAK8[0]+ptAK8[1])>850' 
#isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850' 
#isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])' 
#isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])'
#
#isRegionA_mt_tZ['mtprimeATilde_tM_ZB']['Cuts'] = 'isRegionA_tM_ZB&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850' 
#isRegionB_mt_tZ['mtprimeBTilde_tM_ZB']['Cuts'] = 'isRegionB_tM_ZB&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850' 
#isRegionC_mt_tZ['mtprimeCTilde_tM_ZB']['Cuts'] = 'isRegionC_tM_ZB&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850&&!(ZAnul[2])' 
#isRegionD_mt_tZ['mtprimeDTilde_tM_ZB']['Cuts'] = 'isRegionD_tM_ZB&&Sum$(abs(etaAK4)>2.4)==0&&(ptAK8[0]+ptAK8[1])>850&&!(ZAnul[2])'

isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850' 
isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850' 
isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])' 
isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])'
#
isRegionA_mt_tZ['mtprimeATilde_tM_ZB']['Cuts'] = 'isRegionA_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850' 
isRegionB_mt_tZ['mtprimeBTilde_tM_ZB']['Cuts'] = 'isRegionB_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850' 
isRegionC_mt_tZ['mtprimeCTilde_tM_ZB']['Cuts'] = 'isRegionC_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(ZAnul[2])' 
isRegionD_mt_tZ['mtprimeDTilde_tM_ZB']['Cuts'] = 'isRegionD_tM_ZB&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(ZAnul[2])'

#isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&ptZTagged0L>350' 
#isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&ptZTagged0L>350' 
#isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])&&ptZTagged1M1L>350' 
#isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1])>850&&!(higgsAnul[2])&&ptZTagged1M1L>350'
#isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&ptHTagged1M0L>350' 
#isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&ptHTagged1M0L>350' 
#isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&!(higgsAnul[2])&&ptHTagged1M1L>350' 
#isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&!(higgsAnul[2])&&ptHTagged1M1L>350'
#isRegionA_mt['mtprimeATilde_tM_H1M0L']['Cuts'] = 'isRegionA_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&((ptTopTagged0M[0]-ptHTagged1M0L[0])/mtprimeATilde_tM_H1M0L)<0.1' 
#isRegionB_mt['mtprimeBTilde_tM_H1M0L']['Cuts'] = 'isRegionB_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&((ptTopTaggedM[0]-ptHTagged1M0L[0])/mtprimeBTilde_tM_H1M0L)<0.1' 
#isRegionC_mt['mtprimeCTilde_tM_H1M0L']['Cuts'] = 'isRegionC_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&!(higgsAnul[2])&&((ptTopTagged0M[0]-ptHTagged1M1L[0])/mtprimeCTilde_tM_H1M0L)<0.1' 
#isRegionD_mt['mtprimeDTilde_tM_H1M0L']['Cuts'] = 'isRegionD_tM_H1M0L&&@ptExtraAK4.size()>1&&Sum$(abs(etaAK4)>2.4)>0&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&!(higgsAnul[2])&&((ptTopTaggedM[0]-ptHTagged1M1L[0])/mtprimeDTilde_tM_H1M0L)<0.1'
#isRegionA_mt['mtprimeTilde_tM_H1M0L(mtprimeDummyA,MTopTagged0M,MAntiHTagged)']['Cuts'] += '&&@ptExtraAK4.size()>0&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptAntiHTagged,etaAntiHTagged,phiAntiHTagged,MAntiHTagged,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M))<0.9' 
#isRegionB_mt['mtprimeTilde_tM_H1M0L(mtprimeDummy,MTopTaggedM,MAntiHTagged)']['Cuts'] += '&&@ptExtraAK4.size()>0&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptAntiHTagged,etaAntiHTagged,phiAntiHTagged,MAntiHTagged,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM))<0.9' 
#isRegionC_mt['mtprimeTilde_tM_H1M0L(mtprimeDummyC,MTopTagged0M,MHTagged)']['Cuts'] += '&&@ptExtraAK4.size()>0&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptHTagged,etaHTagged,phiHTagged,MHTagged,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M))<0.9' 
#isRegionD_mt['mtprimeTilde_tM_H1M0L(mtprime,MTopTaggedM,MHTagged)']['Cuts'] += '&&@ptExtraAK4.size()>0&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptHTagged,etaHTagged,phiHTagged,MHTagged,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM))<0.9'

if 'HT' in QCDType:  #add Sump Pt weight if using HT binned QCD samples
    isRegionA_mt['mtprimeDummyA']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
    isRegionB_mt['mtprimeDummy']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
    isRegionC_mt['mtprimeDummyC']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
    isRegionD_mt['mtprime']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)'
    isRegionA_mt['mtprimeDummyA']['SigWts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
    isRegionB_mt['mtprimeDummy']['SigWts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
    isRegionC_mt['mtprimeDummyC']['SigWts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
    isRegionD_mt['mtprime']['SigWts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)'

finalHists = {}
finalHists['A'] = {}
finalHists['B'] = {}
finalHists['C'] = {}
finalHists['D'] = {}

hists = {}
hists['A'] = {}
hists['B'] = {}
hists['C'] = {}
hists['D'] = {}
if do2015:
    hists['A']['Nominal'], hists['B']['Nominal'], hists['C']['Nominal'], hists['D']['Nominal'] = ABCD(isRegionA,isRegionB_mt,isRegionC,isRegionD_mt, False, './limits/LimitHists-MTNominal.root', 'Wts', 'SigWts', 'Nominal', jetType, QCDType)
if dotH:
    hists['A']['Nominal'], hists['B']['Nominal'], hists['C']['Nominal'], hists['D']['Nominal'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTNominal.root', 'Wts', 'SigWts', 'Nominal', jetType, QCDType)

# function needs to be run once per systematic, each function call returns histograms corresponding to the specified systematic

    #hists['A']['HTUp'], hists['B']['HTUp'], hists['C']['HTUp'], hists['D']['HTUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_HTUp.root', 'Wts_HTUp', 'SigWts_HTUp')
    #hists['A']['HTDown'], hists['B']['HTDown'], hists['C']['HTDown'], hists['D']['HTDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_HTDown.root', 'Wts_HTDown', 'SigWts_HTDown')
    hists['A']['JERUp'], hists['B']['JERUp'], hists['C']['JERUp'], hists['D']['JERUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JERUp.root', 'Wts', 'SigWts', 'Nominal', 'JERUp', QCDType)
    hists['A']['JERDown'], hists['B']['JERDown'], hists['C']['JERDown'], hists['D']['JERDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JERDown.root', 'Wts', 'SigWts', 'Nominal', 'JERDown', QCDType)
    hists['A']['JESUp'], hists['B']['JESUp'], hists['C']['JESUp'], hists['D']['JESUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JESUp.root', 'Wts', 'SigWts', 'Nominal', 'JERUp', QCDType)
    hists['A']['JESDown'], hists['B']['JESDown'], hists['C']['JESDown'], hists['D']['JESDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JESDown.root', 'Wts', 'SigWts', 'Nominal', 'JESDown', QCDType)
    hists['A']['ttagDown'], hists['B']['ttagDown'], hists['C']['ttagDown'], hists['D']['ttagDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_ttagDown.root', 'Wts_topSFDown', 'SigWts_topSFDown', 'Nominal', jetType, QCDType)
    hists['A']['ttagUp'], hists['B']['ttagUp'], hists['C']['ttagUp'], hists['D']['ttagUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_ttagUp.root', 'Wts_topSFUp', 'SigWts_topSFUp', 'Nominal', jetType, QCDType)
    hists['A']['lDown'], hists['B']['lDown'], hists['C']['lDown'], hists['D']['lDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTlDown.root', 'Wts_lDown', 'SigWts_lDown', 'Nominal', jetType, QCDType)
    hists['A']['lUp'], hists['B']['lUp'], hists['C']['lUp'], hists['D']['lUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTlUp.root', 'Wts_lUp', 'SigWts_lUp', 'Nominal', jetType, QCDType)
    hists['A']['bcDown'], hists['B']['bcDown'], hists['C']['bcDown'], hists['D']['bcDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTbcDown.root', 'Wts_bcDown', 'SigWts_bcDown', 'Nominal', jetType, QCDType)
    hists['A']['bcUp'], hists['B']['bcUp'], hists['C']['bcUp'], hists['D']['bcUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTbcUp.root', 'Wts_bcUp', 'SigWts_bcUp', 'Nominal', jetType, QCDType)
    hists['A']['mufrDown'], hists['B']['mufrDown'], hists['C']['mufrDown'], hists['D']['mufrDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_mufrDown.root', 'Wts_mufrDown', 'SigWts_mufrDown', 'Nominal', jetType, QCDType)
    hists['A']['mufrUp'], hists['B']['mufrUp'], hists['C']['mufrUp'], hists['D']['mufrUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_mufrUp.root', 'Wts_mufrUp', 'SigWts_mufrUp', 'Nominal', jetType, QCDType)

if dotZ:
    hists['A']['Nominal'], hists['B']['Nominal'], hists['C']['Nominal'], hists['D']['Nominal'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MTNominal.root', 'Wts', 'SigWts', 'Nominal', jetType, QCDType)
    
    # function needs to be run once per systematic, each function call returns histograms corresponding to the specified systematic
    
    #hists['A']['HTUp'], hists['B']['HTUp'], hists['C']['HTUp'], hists['D']['HTUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_HTUp.root', 'Wts_HTUp', 'SigWts_HTUp')
    #hists['A']['HTDown'], hists['B']['HTDown'], hists['C']['HTDown'], hists['D']['HTDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_HTDown.root', 'Wts_HTDown', 'SigWts_HTDown')
    hists['A']['JERUp'], hists['B']['JERUp'], hists['C']['JERUp'], hists['D']['JERUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_JERUp.root', 'Wts', 'SigWts', 'Nominal', 'JERUp', QCDType)
    hists['A']['JERDown'], hists['B']['JERDown'], hists['C']['JERDown'], hists['D']['JERDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_JERDown.root', 'Wts', 'SigWts', 'Nominal', 'JERDown', QCDType)
    hists['A']['JESUp'], hists['B']['JESUp'], hists['C']['JESUp'], hists['D']['JESUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_JESUp.root', 'Wts', 'SigWts', 'Nominal', 'JERUp', QCDType)
    hists['A']['JESDown'], hists['B']['JESDown'], hists['C']['JESDown'], hists['D']['JESDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_JESDown.root', 'Wts', 'SigWts', 'Nominal', 'JESDown', QCDType)
    hists['A']['ttagDown'], hists['B']['ttagDown'], hists['C']['ttagDown'], hists['D']['ttagDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_ttagDown.root', 'Wts_topSFDown', 'SigWts_topSFDown', 'Nominal', jetType, QCDType)
    hists['A']['ttagUp'], hists['B']['ttagUp'], hists['C']['ttagUp'], hists['D']['ttagUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_ttagUp.root', 'Wts_topSFUp', 'SigWts_topSFUp', 'Nominal', jetType, QCDType)
    hists['A']['lDown'], hists['B']['lDown'], hists['C']['lDown'], hists['D']['lDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MTlDown.root', 'Wts_lDown', 'SigWts_lDown', 'Nominal', jetType, QCDType)
    hists['A']['lUp'], hists['B']['lUp'], hists['C']['lUp'], hists['D']['lUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MTlUp.root', 'Wts_lUp', 'SigWts_lUp', 'Nominal', jetType, QCDType)
    hists['A']['bcDown'], hists['B']['bcDown'], hists['C']['bcDown'], hists['D']['bcDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MTbcDown.root', 'Wts_bcDown', 'SigWts_bcDown', 'Nominal', jetType, QCDType)
    hists['A']['bcUp'], hists['B']['bcUp'], hists['C']['bcUp'], hists['D']['bcUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MTbcUp.root', 'Wts_bcUp', 'SigWts_bcUp', 'Nominal', jetType, QCDType)
    hists['A']['mufrDown'], hists['B']['mufrDown'], hists['C']['mufrDown'], hists['D']['mufrDown'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_mufrDown.root', 'Wts_mufrDown', 'SigWts_mufrDown', 'Nominal', jetType, QCDType)
    hists['A']['mufrUp'], hists['B']['mufrUp'], hists['C']['mufrUp'], hists['D']['mufrUp'] = ABCD(isRegionA_mt_tZ,isRegionB_mt_tZ,isRegionC_mt_tZ,isRegionD_mt_tZ, False, './limits/LimitHists-MT_mufrUp.root', 'Wts_mufrUp', 'SigWts_mufrUp', 'Nominal', jetType, QCDType)

for region in hists:
    for key in hists[region]:
        for var in hists[region][key]:
             for hist in hists[region][key][var].keys():
                 if 'tH' in hist and '2600' not in hist and '2400' not in hists and '2200' not in hist and 'GeV' not in hist:
                     if hist.replace('tH','tZ') not in hists[region][key][var]: continue
                     hists[region][key][var][hist.replace('tH','tHtZ')] = hists[region][key][var][hist].Clone(hist.replace('tH','tHtZ'))
                     hists[region][key][var][hist.replace('tH','tHtZ')].Add(hists[region][key][var][hist.replace('tH','tZ')], 1)
                
for region in hists:
    for key in hists[region]:
        for var in hists[region][key]:
             for hist in hists[region][key][var].keys():
                 if ('Tb' in hist or 'Tt' in hist) and '0p' not in hist:
                     if '10GeV' in hist:
                         hists[region][key][var][hist] = hists[region][key][var][hist].Clone(hist.replace('10GeV','00p'))
                     else:
                         hists[region][key][var][hist] = hists[region][key][var][hist].Clone(hist.split('_')[0]+'_'+hist.split('_')[1]+'_00p_'+hist.split('_')[2])

for region in hists:
    for key in hists[region]:
        for var in hists[region][key]:
            for hist in hists[region][key][var].keys():
                if 'Tb' in hist or 'Tt' in hist:
                    tmpInt = hists[region][key][var][hist].Integral(1,1000)
                    if tmpInt != 0.0: continue
                    print "0 integral found, inserting small number into ", hist
                    binN = hists[region][key][var][hist].FindBin(int(hist.split('_')[1]))
                    hists[region][key][var][hist].SetBinContent(binN, 0.0001)
                    newInt = hists[region][key][var][hist].Integral(1,1000)
                    print 'new Integral is ', newInt
                        
for region in hists:
    print 'Region ', region
    for key in hists[region]:   
        for var in hists[region][key]:
            print 'var: ', var
            if 'D' in region:
                hists[region][key][var]['MC_QCD'] = hists[region][key][var]['QCD'].Clone('MC_QCD')
                hists[region][key][var]['QCD'] = hists[region][key][var]['dataQCD'].Clone('QCD')
                hists[region][key][var].pop('dataQCD',None)
            else:
                hists[region][key][var]['MC_QCD'] = hists[region][key][var]['QCD'].Clone('MC_QCD')
                hists[region][key][var]['QCD'] = hists[region][key][var]['dataQCD'].Clone('QCD')
               
                hists[region][key][var].pop('dataQCD',None)
            if 'ht' in var:
                for hist in hists[region][key][var]:
                    if 'Nominal' in key:
                        if 'Data' in hist:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('HT_region'+region+'_data_obs')
                        else:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('HT_region'+region+'_'+hists[region][key][var][hist].GetName())
                            finalHists[region][hist+'_StatUp'] = finalHists[region][hist].Clone('HT_region'+region+'_'+hists[region][key][var][hist].GetName()+'_StatUp')
                            finalHists[region][hist+'_StatDown'] = finalHists[region][hist].Clone('HT_region'+region+'_'+hists[region][key][var][hist].GetName()+'_StatDown')
                            if 'MC_QCD' in hist and 'est' not in hist:
                                finalHists[region]['MC_Background'] = finalHists[region][hist].Clone('HT_region'+region+'_MC_Background')
                                finalHists[region]['MC_Background_StatUp'] = finalHists[region][hist].Clone('HT_region'+region+'_MC_Background_StatUp')
                                finalHists[region]['MC_Background_StatDown'] = finalHists[region][hist].Clone('HT_region'+region+'MC_Background_StatDown')
                            if 'D' in region: 
                                if 'estQCD' in hist and 'MC' not in hist:
                                    finalHists[region]['estBackground'] = finalHists[region][hist].Clone('HT_region'+region+'_estBackground')
                                    finalHists[region]['estBackground_StatUp'] = finalHists[region][hist].Clone('HT_region'+region+'_estBackground_StatUp')
                                    finalHists[region]['estBackground_StatDown'] = finalHists[region][hist].Clone('HT_region'+region+'_estBackground_StatDown')
                                if 'estQCD' in hist and 'MC' in hist:
                                    finalHists[region]['MC_estBackground'] = finalHists[region][hist].Clone('HT_region'+region+'_MC_estBackground')
                                    finalHists[region]['MC_estBackground_StatUp'] = finalHists[region][hist].Clone('HT_region'+region+'_MC_estBackground_StatUp')
                                    finalHists[region]['MC_estBackground_StatDown'] = finalHists[region][hist].Clone('HT_region'+region+'_MC_estBackground_StatDown')
                    else:
                        if 'Data' in hist:
                            continue
                        finalHists[region][hist+'_'+key] = hists[region][key][var][hist].Clone('HT_region'+region+'_'+hists[region][key][var][hist].GetName()+'_'+key)
                        if 'MC_QCD' in hist and 'est' not in hist:
                            finalHists[region]['MC_Background_'+key] = finalHists[region][hist+'_'+key].Clone('HT_region'+region+'_MC_Background_'+key)
                        if 'D' in region:
                            if 'estQCD' in hist and 'MC' not in hist:
                                finalHists[region]['estBackground_'+key] = finalHists[region][hist+'_'+key].Clone('HT_region'+region+'_estBackground_'+key)
                            if 'estQCD' in hist and 'MC' in hist:
                                finalHists[region]['MC_estBackground_'+key] = finalHists[region][hist+'_'+key].Clone('HT_region'+region+'_MC_estBackground_'+key)
    
                for hist in hists[region][key][var]:
                    #if 'TTJets' in hist or 'WJets' in hist or 'ST' in hist or 'ZJets' in hist:
                    if 'LH' not in hist and 'RH' not in hist and 'QCD' not in hist and 'data' not in hist and 'Data' not in hist:
                        if 'Nominal' in key:
                            finalHists[region]['MC_Background_StatUp'].Add(finalHists[region][hist])
                            finalHists[region]['MC_Background_StatDown'].Add(finalHists[region][hist])
                            finalHists[region]['MC_Background'].Add(finalHists[region][hist])
                            if 'D' in region:
                                finalHists[region]['estBackground_StatUp'].Add(finalHists[region][hist+'_StatUp'])
                                finalHists[region]['estBackground_StatDown'].Add(finalHists[region][hist+'_StatDown'])
                                finalHists[region]['estBackground'].Add(finalHists[region][hist])
                                finalHists[region]['MC_estBackground_StatUp'].Add(finalHists[region][hist+'_StatUp'])
                                finalHists[region]['MC_estBackground_StatDown'].Add(finalHists[region][hist+'_StatDown'])
                                finalHists[region]['MC_estBackground'].Add(finalHists[region][hist])
                        else:
                            finalHists[region]['MC_Background_'+key].Add(finalHists[region][hist+'_'+key])
            elif 'mtprime' in var or 'Mjj' in var:
                for hist in hists[region][key][var]:
                    if 'Nominal' in key:
                        if 'Data' in hist:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('MTP_region'+region+'_data_obs')
                        else:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('MTP_region'+region+'_'+hists[region][key][var][hist].GetName())
                            finalHists[region][hist+'_StatUp'] = finalHists[region][hist].Clone('MTP_region'+region+'_'+hists[region][key][var][hist].GetName()+'_StatUp')
                            finalHists[region][hist+'_StatDown'] = finalHists[region][hist].Clone('MTP_region'+region+'_'+hists[region][key][var][hist].GetName()+'_StatDown')
                            if 'MC_QCD' in hist and 'est' not in hist:
                                finalHists[region]['MC_Background'] = finalHists[region][hist].Clone('MTP_region'+region+'_MC_Background')
                                finalHists[region]['MC_Background_StatUp'] = finalHists[region][hist].Clone('MTP_region'+region+'_MC_Background_StatUp')
                                finalHists[region]['MC_Background_StatDown'] = finalHists[region][hist].Clone('MTP_region'+region+'_MC_Background_StatDown')
                            if 'D' in region: 
                                if 'estQCD' in hist and 'MC' not in hist:
                                    finalHists[region]['estBackground'] = finalHists[region][hist].Clone('MTP_region'+region+'_estBackground')
                                    finalHists[region]['estBackground_StatUp'] = finalHists[region][hist].Clone('MTP_region'+region+'_estBackground_StatUp')
                                    finalHists[region]['estBackground_StatDown'] = finalHists[region][hist].Clone('MTP_region'+region+'_estBackground_StatDown')
                                if 'estQCD' in hist and 'MC' in hist:
                                    finalHists[region]['MC_estBackground'] = finalHists[region][hist].Clone('MTP_region'+region+'_MC_estBackground')
                                    finalHists[region]['MC_estBackground_StatUp'] = finalHists[region][hist].Clone('MTP_region'+region+'_MC_estBackground_StatUp')
                                    finalHists[region]['MC_estBackground_StatDown'] = finalHists[region][hist].Clone('MTP_region'+region+'_MC_estBackground_StatDown')
                    else:
                        if 'Data' in hist:
                            continue
                        finalHists[region][hist+'_'+key] = hists[region][key][var][hist].Clone('MTP_region'+region+'_'+hists[region][key][var][hist].GetName()+'_'+key)
                        if 'MC_QCD' in hist and 'est' not in hist:
                            finalHists[region]['MC_Background_'+key] = finalHists[region][hist+'_'+key].Clone('MTP_region'+region+'_MC_Background_'+key)
                        if 'D' in region:
                            if 'estQCD' in hist and 'MC' not in hist:
                                finalHists[region]['estBackground_'+key] = finalHists[region][hist+'_'+key].Clone('MTP_region'+region+'_estBackground_'+key)
                            if 'estQCD' in hist and 'MC' in hist:
                                finalHists[region]['MC_estBackground_'+key] = finalHists[region][hist+'_'+key].Clone('MTP_region'+region+'_MC_estBackground_'+key)
    
                for hist in hists[region][key][var]:
                    #if 'TTJets' in hist or 'WJets' in hist or 'ST' in hist or 'ZJets' in hist:
                    if 'TpTp' not in hist and 'LH' not in hist and 'RH' not in hist and 'QCD' not in hist and 'data' not in hist and 'Data' not in hist:
                        if 'Nominal' in key:
                            finalHists[region]['MC_Background_StatUp'].Add(finalHists[region][hist+'_StatUp'])
                            finalHists[region]['MC_Background_StatDown'].Add(finalHists[region][hist+'_StatDown'])
                            finalHists[region]['MC_Background'].Add(finalHists[region][hist])
                            if 'D' in region:
                                finalHists[region]['estBackground_StatUp'].Add(finalHists[region][hist+'_StatUp'])
                                finalHists[region]['estBackground_StatDown'].Add(finalHists[region][hist+'_StatDown'])
                                finalHists[region]['estBackground'].Add(finalHists[region][hist])
                                finalHists[region]['MC_estBackground_StatUp'].Add(finalHists[region][hist+'_StatUp'])
                                finalHists[region]['MC_estBackground_StatDown'].Add(finalHists[region][hist+'_StatDown'])
                                finalHists[region]['MC_estBackground'].Add(finalHists[region][hist])
                        else:
                            finalHists[region]['MC_Background_'+key].Add(finalHists[region][hist+'_'+key])

print 'Producing statistical templates'                     
statErrUpMT = {}
statErrUpMT['A'] = {}
statErrUpMT['B'] = {}
statErrUpMT['C'] = {}
statErrUpMT['D'] = {}
statErrDownMT = {}
statErrDownMT['A'] = {}
statErrDownMT['B'] = {}
statErrDownMT['C'] = {}
statErrDownMT['D'] = {}

for region in finalHists:
    for i in xrange(1,37):
        #statErrUpMT[region][i-1] = finalHists[region]['QCD_StatUp'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Up')
        #statErrDownMT[region][i-1] = finalHists[region]['QCD_StatDown'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Down')
        if not do2015:
            statErrUpMT[region][i-1] = finalHists[region]['MC_QCD_StatUp'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Up')
            statErrDownMT[region][i-1] = finalHists[region]['MC_QCD_StatDown'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Down')
        else:
            if 'A' in region or 'C' in region:
                statErrUpMT[region][i-1] = finalHists[region]['MC_QCD_StatUp'].Clone('HT_region'+region+'_QCD_bin'+str(i)+'Up')
                statErrDownMT[region][i-1] = finalHists[region]['MC_QCD_StatDown'].Clone('HT_region'+region+'_QCD_bin'+str(i)+'Down')
            else:
                statErrUpMT[region][i-1] = finalHists[region]['MC_QCD_StatUp'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Up')
                statErrDownMT[region][i-1] = finalHists[region]['MC_QCD_StatDown'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Down')
        #if 'D' in region:
        #    statErrUpMT[region][i-1] = finalHists[region]['MC_estQCD_StatUp'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Up')
        #    statErrDownMT[region][i-1] = finalHists[region]['MC_estQCD_StatDown'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Down')
        #    statErrUpMT[region][i-1] = finalHists[region]['estQCD_StatUp'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Up')
        #    statErrDownMT[region][i-1] = finalHists[region]['estQCD_StatDown'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Down')
        statErrUpMT[region][i-1].SetBinContent(i,statErrUpMT[region][i-1].GetBinContent(i)+statErrUpMT[region][i-1].GetBinError(i))
        statErrDownMT[region][i-1].SetBinContent(i,statErrDownMT[region][i-1].GetBinContent(i)-statErrDownMT[region][i-1].GetBinError(i))
    
        for key in finalHists[region]:
            if 'StatUp' in key:
                finalHists[region][key].SetBinContent(i,finalHists[region][key].GetBinContent(i)+finalHists[region][key].GetBinError(i))
            elif 'StatDown' in key:
                finalHists[region][key].SetBinContent(i,finalHists[region][key].GetBinContent(i)-finalHists[region][key].GetBinError(i))

outFile = rt.TFile(outFileName, 'recreate')
for region in sorted(finalHists):
    for key in sorted(finalHists[region]):
        finalHists[region][key].Write()
    #for entry in sorted(statErrUpMT[region]):
    #    statErrUpMT[region][entry].Write()
    #for entry in sorted(statErrDownMT[region]):
    #    statErrDownMT[region][entry].Write()
outFile.Close()
#os.system("./SmoothTemplates.x -ifile="+outFileName+" -ofile="+outFileName.replace('.root','_smoothed.root'))
print 'done'
