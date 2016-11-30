#!/usr/bin/env python
import ROOT as rt
# lfn of samples to be run over
dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_2p1/samples/'

# data Luminosity
lumi = 27202.655 #B-G
#lumi = 12884.276

# Dictionaries of sample names and root files
Data = { 
         'JetHT_2016B'      : dirSamples + 'JetHT_2016B.root',
         'JetHT_2016C'      : dirSamples + 'JetHT_2016C.root',
         'JetHT_2016D'      : dirSamples + 'JetHT_2016D.root',
         'JetHT_2016E'      : dirSamples + 'JetHT_2016E.root',
         'JetHT_2016F'      : dirSamples + 'JetHT_2016F.root',
         'JetHT_2016G'      : dirSamples + 'JetHT_2016G.root',
       }

BackgroundFiles = { 'Nominal' : {
                                    'TTJets'     : dirSamples + 'TTJets.root',
                                    'WJets'      : dirSamples + 'WJets.root',
                                    #'QCDHT700_ext'   : dirSamples + 'QCDHT700_ext.root',
                                    #'QCDHT1000_ext'  : dirSamples + 'QCDHT1000_ext.root',
                                    #'QCDHT1500_ext'  : dirSamples + 'QCDHT1500_ext.root',
                                    #'QCDHT2000_ext'  : dirSamples + 'QCDHT2000_ext.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_top'     : dirSamples + 'ST_top.root',
                                    #'ZJets'      : dirSamples + 'ZJets.root'
                                },
                    'JERUp' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg_JERUp.root',
                                    'WJets'      : dirSamples + 'WJets_JERUp.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700_JERUp.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000_JERUp.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500_JERUp.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000_JERUp.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop_JERUp.root',
                                    'ST_top'     : dirSamples + 'ST_top_JERUp.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JERUp.root'
                                },
                    'JERDown' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg_JERDown.root',
                                    'WJets'      : dirSamples + 'WJets_JERDown.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700_JERDown.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000_JERDown.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500_JERDown.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000_JERDown.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop_JERDown.root',
                                    'ST_top'     : dirSamples + 'ST_top_JERDown.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JERDown.root'
                                },
                    'JESUp' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg_JESUp.root',
                                    'WJets'      : dirSamples + 'WJets_JESUp.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700_JESUp.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000_JESUp.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500_JESUp.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000_JESUp.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop_JESUp.root',
                                    'ST_top'     : dirSamples + 'ST_top_JESUp.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JESUp.root'
                                },
                    'JESDown' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg_JESDown.root',
                                    'WJets'      : dirSamples + 'WJets_JESDown.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700_JESDown.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000_JESDown.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500_JESDown.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000_JESDown.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop_JESDown.root',
                                    'ST_top'     : dirSamples + 'ST_top_JESDown.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JESDown.root'
                                }
                  
                  }
SignalFiles = { 'Nominal' : { 
                               'TbtH_800_LH' : dirSamples + 'TbtH_800_LH.root',
                               'TbtH_900_LH' : dirSamples + 'TbtH_900_LH.root',
                               'TbtH_1000_LH' : dirSamples + 'TbtH_1000_LH.root',
                               'TbtH_1200_LH' : dirSamples + 'TbtH_1200_LH.root',
                               'TbtH_1500_LH' : dirSamples + 'TbtH_1500_LH.root',
                               'TbtH_1800_LH' : dirSamples + 'TbtH_1800_LH.root'
                            },
                'JERUp'   : {
                               'TbtZ_800_LH' : dirSamples + 'TbtZ_800_LH_JERUp.root',
                               'TbtZ_900_LH' : dirSamples + 'TbtZ_900_LH_JERUp.root',
                               'TbtZ_1000_LH' : dirSamples + 'TbtZ_1000_LH_JERUp.root',
                               'TbtZ_1100_LH' : dirSamples + 'TbtZ_1100_LH_JERUp.root',
                               'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH_JERUp.root',
                               'TbtZ_1300_LH' : dirSamples + 'TbtZ_1300_LH_JERUp.root',
                               'TbtZ_1400_LH' : dirSamples + 'TbtZ_1400_LH_JERUp.root',
                               'TbtZ_1500_LH' : dirSamples + 'TbtZ_1500_LH_JERUp.root',
                               'TbtZ_1700_LH' : dirSamples + 'TbtZ_1700_LH_JERUp.root',
                               'TbtZ_1800_LH' : dirSamples + 'TbtZ_1800_LH_JERUp.root',
                               'TbtZ_800_RH' : dirSamples + 'TbtZ_800_RH_JERUp.root',
                               'TbtZ_900_RH' : dirSamples + 'TbtZ_900_RH_JERUp.root',
                               'TbtZ_1000_RH' : dirSamples + 'TbtZ_1000_RH_JERUp.root',
                               'TbtZ_1100_RH' : dirSamples + 'TbtZ_1100_RH_JERUp.root',
                               'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH_JERUp.root',
                               'TbtZ_1300_RH' : dirSamples + 'TbtZ_1300_RH_JERUp.root',
                               'TbtZ_1400_RH' : dirSamples + 'TbtZ_1400_RH_JERUp.root',
                               'TbtZ_1500_RH' : dirSamples + 'TbtZ_1500_RH_JERUp.root',
                               'TbtZ_1700_RH' : dirSamples + 'TbtZ_1700_RH_JERUp.root',
                               'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH_JERUp.root'
                            },
                'JERDown' : {
                               'TbtZ_800_LH' : dirSamples + 'TbtZ_800_LH_JERDown.root',
                               'TbtZ_900_LH' : dirSamples + 'TbtZ_900_LH_JERDown.root',
                               'TbtZ_1000_LH' : dirSamples + 'TbtZ_1000_LH_JERDown.root',
                               'TbtZ_1100_LH' : dirSamples + 'TbtZ_1100_LH_JERDown.root',
                               'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH_JERDown.root',
                               'TbtZ_1300_LH' : dirSamples + 'TbtZ_1300_LH_JERDown.root',
                               'TbtZ_1400_LH' : dirSamples + 'TbtZ_1400_LH_JERDown.root',
                               'TbtZ_1500_LH' : dirSamples + 'TbtZ_1500_LH_JERDown.root',
                               'TbtZ_1700_LH' : dirSamples + 'TbtZ_1700_LH_JERDown.root',
                               'TbtZ_1800_LH' : dirSamples + 'TbtZ_1800_LH_JERDown.root',
                               'TbtZ_800_RH' : dirSamples + 'TbtZ_800_RH_JERDown.root',
                               'TbtZ_900_RH' : dirSamples + 'TbtZ_900_RH_JERDown.root',
                               'TbtZ_1000_RH' : dirSamples + 'TbtZ_1000_RH_JERDown.root',
                               'TbtZ_1100_RH' : dirSamples + 'TbtZ_1100_RH_JERDown.root',
                               'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH_JERDown.root',
                               'TbtZ_1300_RH' : dirSamples + 'TbtZ_1300_RH_JERDown.root',
                               'TbtZ_1400_RH' : dirSamples + 'TbtZ_1400_RH_JERDown.root',
                               'TbtZ_1500_RH' : dirSamples + 'TbtZ_1500_RH_JERDown.root',
                               'TbtZ_1700_RH' : dirSamples + 'TbtZ_1700_RH_JERDown.root',
                               'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH_JERDown.root'
                            },
                'JESUp'   : {
                               'TbtZ_800_LH' : dirSamples + 'TbtZ_800_LH_JESUp.root',
                               'TbtZ_900_LH' : dirSamples + 'TbtZ_900_LH_JESUp.root',
                               'TbtZ_1000_LH' : dirSamples + 'TbtZ_1000_LH_JESUp.root',
                               'TbtZ_1100_LH' : dirSamples + 'TbtZ_1100_LH_JESUp.root',
                               'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH_JESUp.root',
                               'TbtZ_1300_LH' : dirSamples + 'TbtZ_1300_LH_JESUp.root',
                               'TbtZ_1400_LH' : dirSamples + 'TbtZ_1400_LH_JESUp.root',
                               'TbtZ_1500_LH' : dirSamples + 'TbtZ_1500_LH_JESUp.root',
                               'TbtZ_1700_LH' : dirSamples + 'TbtZ_1700_LH_JESUp.root',
                               'TbtZ_1800_LH' : dirSamples + 'TbtZ_1800_LH_JESUp.root',
                               'TbtZ_800_RH' : dirSamples + 'TbtZ_800_RH_JESUp.root',
                               'TbtZ_900_RH' : dirSamples + 'TbtZ_900_RH_JESUp.root',
                               'TbtZ_1000_RH' : dirSamples + 'TbtZ_1000_RH_JESUp.root',
                               'TbtZ_1100_RH' : dirSamples + 'TbtZ_1100_RH_JESUp.root',
                               'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH_JESUp.root',
                               'TbtZ_1300_RH' : dirSamples + 'TbtZ_1300_RH_JESUp.root',
                               'TbtZ_1400_RH' : dirSamples + 'TbtZ_1400_RH_JESUp.root',
                               'TbtZ_1500_RH' : dirSamples + 'TbtZ_1500_RH_JESUp.root',
                               'TbtZ_1700_RH' : dirSamples + 'TbtZ_1700_RH_JESUp.root',
                               'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH_JESUp.root'
                            },
                'JESDown' : {
                               'TbtZ_800_LH' : dirSamples + 'TbtZ_800_LH_JESDown.root',
                               'TbtZ_900_LH' : dirSamples + 'TbtZ_900_LH_JESDown.root',
                               'TbtZ_1000_LH' : dirSamples + 'TbtZ_1000_LH_JESDown.root',
                               'TbtZ_1100_LH' : dirSamples + 'TbtZ_1100_LH_JESDown.root',
                               'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH_JESDown.root',
                               'TbtZ_1300_LH' : dirSamples + 'TbtZ_1300_LH_JESDown.root',
                               'TbtZ_1400_LH' : dirSamples + 'TbtZ_1400_LH_JESDown.root',
                               'TbtZ_1500_LH' : dirSamples + 'TbtZ_1500_LH_JESDown.root',
                               'TbtZ_1700_LH' : dirSamples + 'TbtZ_1700_LH_JESDown.root',
                               'TbtZ_1800_LH' : dirSamples + 'TbtZ_1800_LH_JESDown.root',
                               'TbtZ_800_RH' : dirSamples + 'TbtZ_800_RH_JESDown.root',
                               'TbtZ_900_RH' : dirSamples + 'TbtZ_900_RH_JESDown.root',
                               'TbtZ_1000_RH' : dirSamples + 'TbtZ_1000_RH_JESDown.root',
                               'TbtZ_1100_RH' : dirSamples + 'TbtZ_1100_RH_JESDown.root',
                               'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH_JESDown.root',
                               'TbtZ_1300_RH' : dirSamples + 'TbtZ_1300_RH_JESDown.root',
                               'TbtZ_1400_RH' : dirSamples + 'TbtZ_1400_RH_JESDown.root',
                               'TbtZ_1500_RH' : dirSamples + 'TbtZ_1500_RH_JESDown.root',
                               'TbtZ_1700_RH' : dirSamples + 'TbtZ_1700_RH_JESDown.root',
                               'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH_JESDown.root'
                            } 
          }

# Dictionary containing the x-sections of each of the MC samples
sampleXsec = {
               'TTJets'       : 831.76,
               'WJets'        : 95.14,
               'QCDHT700'     : 6831,
               'QCDHT1000'    : 1207,
               'QCDHT1500'    : 119.9,
               'QCDHT2000'    : 25.24,
               #'QCDHT700_ext'     : 6831,
               #'QCDHT1000_ext'    : 1207,
               #'QCDHT1500_ext'    : 119.9,
               #'QCDHT2000_ext'    : 25.24,
               'ST'           : 35.6,
               #'ZJets'        : 6.97,
               'TbtH_800_LH' : 10000.0,
               'TbtH_900_LH' : 10000.0,
               'TbtH_1000_LH' : 10000.0,
               'TbtH_1200_LH' : 10000.0,
               'TbtH_1500_LH' : 10000.0,
               'TbtH_1800_LH' : 10000.0
             }

# Dictionary containing the information for each variable to be retrieved


NPV = {
                'npv' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : '1',
                    'xMin'   : '0',
                    'xMax'   : '80',
                    'nBins'  : '80',
                    'xLabel' : 'nPV',
                    'yLabel' : 'Events',
                    'log'    : True
                  },
             }
HT = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : '1100',
                    'xMax'   : '3200',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/42GeV',
                    'log'    : True
                  },
      }
btagsf = {
                'btagsf' 
                : {
                    'Wts'    : '1.0',
                    'SigWts' : '1.0',
                    'Cuts'   : '1',
                    'xMin'   : '0',
                    'xMax'   : '2000',
                    'nBins'  : '40',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/40GeV',
                    'log'    : True
                  },
      }

Cutflow_pre = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : '1100',
                    'xMax'   : '3200',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
             }

Cutflow_higgs = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*QuadWeightHT(ht,0)',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100&&(isRegionC||isRegionD)',
#                   'Cuts'   : 'ht>1100&&(isRegionA||isRegionB||isRegionC||isRegionD||(',
                    'xMin'   : '1100',
                    'xMax'   : '3200',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/42GeV',
                    'log'    : True
                  },
               }
Cutflow_top = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*toptagsf*QuadWeightHT(ht,0)',
                    'SigWts' : 'EvtWeight*EvtWtPV*toptagsf',
#                    'Cuts'   : 'ht>1100&&(ptAK8>400&&SoftDropMassAK8<220&&SoftDropMassAK8>105&&(tau3AK8/tau2AK8)<0.5)',
                    'Cuts'   : 'ht>1100&&@idxTopTagged.size()>0',
                    'xMin'   : '1100',
                    'xMax'   : '3200',
                    'nBins'  : '50',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
               }

Cutflow_higgs_top = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV*topSF(ptTopTagged)',
                    'SigWts' : 'EvtWeight*EvtWtPV*topSF(ptTopTagged)',
#                    'Cuts'   : 'ht>1100&&(ptAK8>400&&SoftDropMassAK8<220&&SoftDropMassAK8>105&&(tau3AK8/tau2AK8)<0.5&&max(sj0CSVAK8,sj1CSVAK8)>0.46)&&(isRegionC||isRegionD)&&dR(etaAK8,phiAK8,etaHTagged,phiHTagged)>2.0',
                   'Cuts'   : 'ht>1100&&isRegionD',
                    'xMin'   : '1100',
                    'xMax'   : '3200',
                    'nBins'  : '40',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
             }
