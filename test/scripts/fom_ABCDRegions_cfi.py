cutsRegionA = {
               #'Base' : 'isRegionA_tM_H1M0L && !(higgsAnul[7])',
               'Base' : 'isRegionA_tM_H1M0L',
               #'Base' : 'isRegionA_Z',
               'ptTopHiggs' : 'isRegionA&&((ptTopTagged0M[0]-ptHTagged1M0L[0])/mtprimeATilde_tM_H1M0L)<0.1',
               'Base2' : 'isRegionA && ptHTagged1M0L>400',
               'cosThetaStar' : 'isRegionA && abs(costheta(ptHTagged1M0L,etaHTagged1M0L,phiHTagged1M0L,MHTagged1M0L,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M))<0.9',
               '1200MassRegion10p' : 'isRegionA && mtprimeATilde_tM_H1M0L > (1200-1200*0.15) && mtprimeATilde_tM_ZB < (1200+1200*0.15) && ptHTagged1M0L>350',
               '600MassRegion10p' : 'isRegionA && mtprimeATilde_tM_H1M0L > (1100-1100*0.15) && mtprimeATilde_tM_ZB < (1100+1100*0.15)',
               '1800MassRegion10p' : 'isRegionA && mtprimeATilde_tM_H1M0L > (1800-1800*0.15) && mtprimeATilde_tM_ZB < (1800+1800*0.15)',
              }
cutsRegionB = {
               #'Base' : 'isRegionB_tM_H1M0L && !(higgsAnul[7])',
               'Base' : 'isRegionB_tM_H1M0L',
               #'Base' : 'isRegionB_Z',
               'ptTopHiggs' : 'isRegionB&&((ptTopTaggedM[0]-ptHTagged1M0L[0])/mtprimeBTilde_tM_H1M0L)<0.1',
               'Base2' : 'isRegionB && ptHTagged1M0L>400',
               'cosThetaStar' : 'isRegionB && abs(costheta(ptHTagged1M0L,etaHTagged1M0L,phiHTagged1M0L,MHTagged1M0L,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM))<0.9',
               '1200MassRegion10p' : 'isRegionB && mtprimeBTilde_tM_H1M0L > (1200-1200*0.15) && mtprimeBTilde_tM_ZB < (1200+1200*0.15) && ptHTagged1M0L>350',
               '600MassRegion10p' : 'isRegionB && mtprimeBTilde_tM_H1M0L > (1100-1100*0.15) && mtprimeBTilde_tM_ZB < (1100+1100*0.15)',
               '1800MassRegion10p' : 'isRegionB && mtprimeBTilde_tM_H1M0L > (1800-1800*0.15) && mtprimeBTilde_tM_ZB < (1800+1800*0.15)',
              }
cutsRegionC = {
               'Base' : 'isRegionC_tM_H1M0L && !(higgsAnul[2])',
               #'Base' : 'isRegionC_tM_H1M0L',
               #'Base' : 'isRegionC_Z',
               'ptTopHiggs' : 'isRegionC && !(higgsAnul[7])&&((ptTopTagged0M[0]-ptHTagged1M1L[0])/mtprimeCTilde_tM_H1M0L)<0.1',
               'Base2' : 'isRegionC && !(higgsAnul[7]) && ptHTagged1M1L>400',
               'cosThetaStar' : 'isRegionC && abs(costheta(ptHTagged1M1L,etaHTagged1M1L,phiHTagged1M1L,MHTagged1M1L,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M))<0.9&&!(higgsAnul[7])',
               '1200MassRegion10p' : 'isRegionC && mtprimeCTilde_tM_H1M0L > (1200-1200*0.15) && mtprimeCTilde_tM_ZB < (1200+1200*0.15) && ptHTagged1M1L>350',
               '600MassRegion10p' : 'isRegionC && mtprimeCTilde_tM_H1M0L > (1100-1100*0.15) && mtprimeCTilde_tM_ZB < (1100+1100*0.15)',
               '1800MassRegion10p' : 'isRegionC && mtprimeCTilde_tM_H1M0L > (1800-1800*0.15) && mtprimeCTilde_tM_ZB < (1800+1800*0.15)',
              }
cutsRegionD = { 
               'Base' : 'isRegionD_tM_H1M0L && !(higgsAnul[2])', 
               #'Base' : 'isRegionD_tM_H1M0L', 
               #'Base' : 'isRegionD_Z', 
               'ptTopHiggs' : 'isRegionD && !(higgsAnul[7])&&((ptTopTaggedM[0]-ptHTagged1M1L[0])/mtprimeDTilde_tM_H1M0L)<0.1', 
               'Base2' : 'isRegionD && !(higgsAnul[7]) && ptHTagged1M1L>400', 
               'cosThetaStar' : 'isRegionD&&abs(costheta(ptHTagged1M1L[0],etaHTagged1M1L[0],phiHTagged1M1L[0],MHTagged1M1L[0],ptTopTaggedM[0],etaTopTaggedM[0],phiTopTaggedM[0],MTopTaggedM[0]))<0.9&&!(higgsAnul[7])',
               #'cosThetaStar' : 'isRegionD&&abs(costheta(ptHTagged1M1L,etaHTagged1M1L,phiHTagged1M1L,MHTagged1M1L,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM))<0.9&&!(higgsAnul[7])',
               '1200MassRegion10p' : 'isRegionD && mtprimeDTilde_tM_H1M0L > (1200-1200*0.15) && mtprimeDTilde_tM_ZB < (1200+1200*0.15) && !(higgsAnul[7]) && ptHTagged1M1L>350',
               '600MassRegion10p' : 'isRegionD && mtprimeDTilde_tM_H1M0L > (1100-1100*0.15) && mtprimeDTilde_tM_ZB < (1100+1100*0.15) && !(higgsAnul[7])',
               '1800MassRegion10p' : 'isRegionD && mtprimeDTilde_tM_H1M0L > (1800-1800*0.15) && mtprimeDTilde_tM_ZB < (1800+1800*0.15) && !(higgsAnul[7])',
             } 

additionalCuts = {
                  #'massWindow_topM_H1M0L' : '&& (ptAK8[0]+ptAK8[1])>850',
                  #'massWindow_topM_1200MassRegion' : '',
                  #'massWindow_topM_1800MassRegion' : '',
                  #'massWindow_topM_extraJetOne' : '&& @ptExtraAK4.size()>0',
                  #'massWindow_topM_extraJetTwo' : '&& @ptExtraAK4.size()>1',
                  ##'massWindow_topM_forwardJetOne' : '&& Sum$(abs(etaAK4)>2.4)>0',
                  ##'massWindow_topM_forwardJetTwo' : '&& Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraForwardJetOne_850' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_extraForwardJetTwo_850' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>1',
                  #'massWindow_topM_H1M0L_withData_forwardJetOne_extraJetVeto_annulus' : '&& Sum$(abs(etaAK4)>2.4)>0 && !(@ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0)',
                  #'massWindow_topM_H1M0L_H400_ht4-900_annulus_0p55-0p9' : '&&(ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L_Veto_relaxForward_sumPt_annulus' : '&& (ptAK8[0]+ptAK8[1])>850 && (@ptExtraAK4.size()==0 || @ptExtraAK4.size()==1)',
                  #'massWindow_topM_H1M0L_extraForwardVeto_no-annulus' : '&& !(Max$(abs(etaExtraAK4))>2.4)',
                  #'topM_H1M0L_lepVeto' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0',
                  'topM_H1M0L_norm' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L_withData_extraJetVeto' : '&& (ptAK8[0]+ptAK8[1])>850 && !(@ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0)',
                  #'massWindow_topM_H1M0L_withData_forwardVeto' : '&& (ptAK8[0]+ptAK8[1])>850 && Sum$(abs(etaAK4)>2.4)==0',
                  #'massWindow_topM_H1M0L_norm_0p16-syst' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L_withData_extraJetVeto_0p16-syst' : '&& (ptAK8[0]+ptAK8[1])>850 && !(@ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0)',
                  #'massWindow_topM_H1M0L_withData_forwardVeto_0p16-syst' : '&& (ptAK8[0]+ptAK8[1])>850 && Sum$(abs(etaAK4)>2.4)==0',
                  #'massWindow_topM_H1M0L_no-annulus_0p55-0p9' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L-350_ht4-900_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_1200MassRegion' : '&& (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L_ptSum850_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_1200MassRegion' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L-350_ht4-900_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_1800MassRegion' : '&& (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L_ptSum850_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_1800MassRegion' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_H1M0L_ht4-900_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_cosTheta0p85_1200MassRegion' : '&& (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptAK8[1],etaAK8[1],phiAK8[1],MAK8[1],ptAK8[0],etaAK8[0],phiAK8[0],MAK8[0]))<0.85',
                  #'massWindow_topM_H1M0L_ht4-900_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_cosTheta0p85_600MassRegion' : '&& (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptAK8[1],etaAK8[1],phiAK8[1],MAK8[1],ptAK8[0],etaAK8[0],phiAK8[0],MAK8[0]))<0.85',
                  #'massWindow_topM_H1M0L_ht4-900_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_cosTheta0p85_1800MassRegion' : '&& (ptAK8[0]+ptAK8[1]+ptExtraAK4[0]+ptExtraAK4[1])>900&&@ptExtraAK4.size()>1&&Sum$(abs(etaExtraAK4)>2.4)>0&&abs(costheta(ptAK8[1],etaAK8[1],phiAK8[1],MAK8[1],ptAK8[0],etaAK8[0],phiAK8[0],MAK8[0]))<0.85',
                  #'massWindow_topM_H1M0L_ptSum850_Zannulus_0p55-0p9_extraJetTwo_extraForwardJetOne_cosTheta0p9' : '&& (ptAK8[0]+ptAK8[1])>850 && @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_extraJetTwo_extraForwardJetOne_noIsoLep' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0',
                  #'massWindow_topM_extraJetTwo_extraForwardJetOne_noIsoLep_1200MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0',
                  #'massWindow_topM_extraJetTwo_extraForwardJetOne_noIsoLep_1800MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0',
                  #'massWindow_topM_extraJetTwo_oneExtraJetBtagged_extraForwardJetOne' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && Sum$(csvExtraAK4>0.5426)>0',
                  #'massWindow_topM_extraJetTwo_oneExtraJetBtagged_extraForwardJetOne_1200MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && Sum$(csvExtraAK4>0.8484)>0',
                  #'massWindow_topM_extraJetTwo_oneExtraJetBtagged_extraForwardJetOne_1800MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0 && Sum$(csvExtraAK4>0.8484)>0',
                  #'massWindow_topM_extraJetOne_ForwardJetOne_850' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_ForwardJetTwo_850' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_ForwardJetTwo_850' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_ForwardJetOne_850' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_1200MassRegion' : '&& @ptExtraAK4.size()>0',
                  #'massWindow_topM_extraJetTwo_1200MassRegion' : '&& @ptExtraAK4.size()>1',
                  #'massWindow_topM_extraForwardJetOne_1200MassRegion' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_extraForwardJetTwo_1200MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_extraForwardJetOne_1200MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_ForwardJetOne_1200MassRegion' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_ForwardJetTwo_1200MassRegion' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_ForwardJetTwo_1200MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_ForwardJetOne_1200MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_1800MassRegion' : '&& @ptExtraAK4.size()>0',
                  #'massWindow_topM_extraJetTwo_1800MassRegion' : '&& @ptExtraAK4.size()>1',
                  #'massWindow_topM_extraForwardJetOne_1800MassRegion' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_extraForwardJetTwo_1800MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_extraForwardJetOne_1800MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_ForwardJetOne_1800MassRegion' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_extraJetOne_ForwardJetTwo_1800MassRegion' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_ForwardJetTwo_1800MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>1',
                  #'massWindow_topM_extraJetTwo_ForwardJetOne_1800MassRegion' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_cosThetaT0p9_extraForwardJetOne_850' : '&& @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_cosThetaT0p9_extraForwardJetTwo_850' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>1',
                  #'massWindow_topM_cosThetaT0p9_extraJetTwoForwardJetOne_850' : '&& @ptExtraAK4.size()>1 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_cosThetaT0p9_extraForwardJetOne_650' : 'ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>650 && @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'sumPt650_forwardJetsOne' : 'nAK8>=2&&ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>650 && Sum$(abs(etaAK4)>2.4)>0',
                  #'sumPt600_forwardJetsOne' : 'nAK8>=2&&ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>600 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_forwardJetOne' : 'nAK8>=2&&ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850 && ptAK8>300 && Sum$(abs(etaAK4)>2.4)>0',
                  #'massWindow_topM_forwardjetsZero' : 'nAK8>=2&&ptAK8[0]>500&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850 && ptAK8>300 && Sum$(abs(etaAK4)>2.4)==0',
                  #'massWindow_topM_cosThetaTt_0p9' : 'nAK8>=2&&ptAK8[0]>500&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850 && ptAK8>300',
                  #'massWindow_topM_noIsoLep' : 'nAK8>=2&&ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850 && ptAK8>300 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0 ',
                  #'massWindow_topM_noIsoLep_extraForwardJetOne_850' : 'ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0 && @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                  #'massWindow_topM_noIsoLep_extraForwardJetOne_650' : 'ptAK8[0]>400&&PrunedMassAK8[0]>50&&(ptAK8[0]+ptAK8[1])>850 && @ptCleanedMu.size()==0 && @ptCleanedEl.size()==0 && @ptExtraAK4.size()>0 && Sum$(abs(etaExtraAK4)>2.4)>0',
                 } 

isRegionA_FOM = {
              'mtprimeATilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  :  cutsRegionA['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionA_FOM_HT = {
              'ht' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  :  cutsRegionA['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionA_FOM_Z = {
              'Mjj(ptAntiZTagged,etaAntiZTagged,phiAntiZTagged,MAntiZTagged,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M)' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  :  cutsRegionA['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
                }
isRegionB_FOM = {
              'mtprimeBTilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  :  cutsRegionB['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionB_FOM_HT = {
              'ht' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionB['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionB_FOM_Z = {
              'Mjj(ptAntiZTagged,etaAntiZTagged,phiAntiZTagged,MAntiZTagged,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM)' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  :  cutsRegionB['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
                }
isRegionC_FOM = {
             'mtprimeCTilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionC['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionC_FOM_HT = {
              'ht' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionC['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionC_FOM_Z = {
              'Mjj(ptZTagged,etaZTagged,phiZTagged,MZTagged,ptTopTagged0M,etaTopTagged0M,phiTopTagged0M,MTopTagged0M)' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionC['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
                }
isRegionD_FOM = {
              'mtprimeDTilde_tM_H1M0L' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionD['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionD_FOM_HT = {
              'ht' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionD['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
}
isRegionD_FOM_Z = {
              'Mjj(ptZTagged,etaZTagged,phiZTagged,MZTagged,ptTopTaggedM,etaTopTaggedM,phiTopTaggedM,MTopTaggedM)' : {
                       'Wts'   : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'SigWts' : 'EvtWeight*EvtWtPV*toptagsf*btagsfMed*btagsf*btagsfLoose*btagsfZ',
                       'Cuts'  : cutsRegionD['Base'],
                       'xMin'  : '600',
                       'xMax'  : '3100',
                       'nBins' : '50',
                       'xLabel' : 'H_{T} [GeV]',
                       'yLabel' : 'Events/80GeV',
                       'log'   : True
                     },
                 }
                 
