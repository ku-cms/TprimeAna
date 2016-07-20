#!/usr/bin/env python
import ROOT as rt
# lfn of samples to be run over
dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_7_4_8_patch1/src/TprimeAna/test/SelectionTtotZ_26May16/samples/'

# data Luminosity
lumi = 2264.524

# Dictionaries of sample names and root files
Data = { 
         'JetHT_05Oct'      : dirSamples + 'JetHT_05Oct.root',
         'JetHT_PromptReco' : dirSamples + 'JetHT_Prompt.root',
         'JetHT_2015C'      : dirSamples + 'JetHT_2015C.root'
       }

BackgroundFiles = { 'Nominal' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg.root',
                                    'WJets'      : dirSamples + 'WJets.root',
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
                               'TbtZ_800_LH' : dirSamples + 'TbtZ_800_LH.root',
                               'TbtZ_900_LH' : dirSamples + 'TbtZ_900_LH.root',
                               'TbtZ_1000_LH' : dirSamples + 'TbtZ_1000_LH.root',
                               'TbtZ_1100_LH' : dirSamples + 'TbtZ_1100_LH.root',
                               'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH.root',
                               'TbtZ_1300_LH' : dirSamples + 'TbtZ_1300_LH.root',
                               'TbtZ_1400_LH' : dirSamples + 'TbtZ_1400_LH.root',
                               'TbtZ_1500_LH' : dirSamples + 'TbtZ_1500_LH.root',
                               'TbtZ_1700_LH' : dirSamples + 'TbtZ_1700_LH.root',
                               'TbtZ_1800_LH' : dirSamples + 'TbtZ_1800_LH.root',
                               'TbtZ_800_RH' : dirSamples + 'TbtZ_800_RH.root',
                               'TbtZ_900_RH' : dirSamples + 'TbtZ_900_RH.root',
                               'TbtZ_1000_RH' : dirSamples + 'TbtZ_1000_RH.root',
                               'TbtZ_1100_RH' : dirSamples + 'TbtZ_1100_RH.root',
                               'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH.root',
                               'TbtZ_1300_RH' : dirSamples + 'TbtZ_1300_RH.root',
                               'TbtZ_1400_RH' : dirSamples + 'TbtZ_1400_RH.root',
                               'TbtZ_1500_RH' : dirSamples + 'TbtZ_1500_RH.root',
                               'TbtZ_1700_RH' : dirSamples + 'TbtZ_1700_RH.root',
                               'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH.root'
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
               'ST'           : 35.6,
               #'ZJets'        : 6.97,
               'TbtZ_800_LH' : 1.0,
               'TbtZ_900_LH' : 1.0,
               'TbtZ_1000_LH' : 1.0,
               'TbtZ_1100_LH' : 1.0,
               'TbtZ_1200_LH' : 1.0,
               'TbtZ_1300_LH' : 1.0,
               'TbtZ_1400_LH' : 1.0,
               'TbtZ_1500_LH' : 1.0,
               'TbtZ_1700_LH' : 1.0,
               'TbtZ_1800_LH' : 1.0,
               'TbtZ_800_RH' : 1.0,
               'TbtZ_900_RH' : 1.0,
               'TbtZ_1000_RH' : 1.0,
               'TbtZ_1100_RH' : 1.0,
               'TbtZ_1200_RH' : 1.0,
               'TbtZ_1300_RH' : 1.0,
               'TbtZ_1400_RH' : 1.0,
               'TbtZ_1500_RH' : 1.0,
               'TbtZ_1700_RH' : 1.0,
               'TbtZ_1800_RH' : 1.0
             }

# Dictionary containing the information for each variable to be retrieved

preselDict = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts' : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : '1100',
                    'xMax'   : '2700',
                    'nBins'  : '20',
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
                'PrunedMassAK8' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts'    : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : '0',
                    'xMax'   : '800',
                    'nBins'  : '40',
                    'xLabel' : 'Pruned Mass [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'tau2AK8/tau1AK8'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'SigWts'    : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : '0', 
                    'xMax'   : '1', 
                    'nBins'  : '50',
                    'xLabel' : '#tau_{21}',
                    'yLabel' : 'Jets',
                    'log'    : True 
                  }
             }
