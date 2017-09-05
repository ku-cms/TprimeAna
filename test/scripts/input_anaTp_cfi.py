#!/usr/bin/env python
import ROOT as rt
# lfn of samples to be run over
dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_2p4_v3/'

# data Luminosity
lumi = 35865.177 #B-H
#lumi = 27954.748
#lumi = 12884.276

# Dictionaries of sample names and root files
Data = { 
         'JetHT_2016B'      : dirSamples + 'JetHT_Run2016B.root',
         'JetHT_2016C'      : dirSamples + 'JetHT_Run2016C.root',
         'JetHT_2016D'      : dirSamples + 'JetHT_Run2016D.root',
         'JetHT_2016E'      : dirSamples + 'JetHT_Run2016E.root',
         'JetHT_2016F'      : dirSamples + 'JetHT_Run2016F.root',
         'JetHT_2016G'      : dirSamples + 'JetHT_Run2016G.root',
        'JetHT_2016H_v2'      : dirSamples + 'JetHT_Run2016H_v2.root',
        'JetHT_2016H_v3'      : dirSamples + 'JetHT_Run2016H_v3.root',
       }

BackgroundFilesHT = { 'Nominal' : {
                                    'TTJets'     : dirSamples + 'TTJets.root',
                                    'WJets'      : dirSamples + 'WJets.root',
                                    'QCDHT100'   : dirSamples + 'QCDHT100.root',
                                    #'QCDHT200'   : dirSamples + 'QCDHT200.root',
                                    'QCDHT300'   : dirSamples + 'QCDHT300.root',
                                    'QCDHT500'   : dirSamples + 'QCDHT500.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_top'     : dirSamples + 'ST_top.root',
                                    'ttZJets'    : dirSamples + 'ttZJets.root',
                                    'ttWJets'    : dirSamples + 'ttWJets.root',
                                    'DYJets'     : dirSamples + 'DYJets.root',
                                    'tHQ'        : dirSamples + 'tHQ.root',
                                    'ZJets'      : dirSamples + 'ZJets.root',
                                    'ZZ'          : dirSamples + 'ZZ.root',
                                    'WW'          : dirSamples + 'WW.root',
                                },
                    }
BackgroundFilesPt = { 'Nominal' : {
                                    'TTJets'     : dirSamples + 'TTJets.root',
                                    'WJets'      : dirSamples + 'WJets.root',
                                    'QCDPt80'   : dirSamples + 'QCDPt80.root',
                                    'QCDPt120'   : dirSamples + 'QCDPt120.root',
                                    'QCDPt170'   : dirSamples + 'QCDPt170.root',
                                    'QCDPt300'   : dirSamples + 'QCDPt300.root',
                                    'QCDPt470'   : dirSamples + 'QCDPt470.root',
                                    'QCDPt600'   : dirSamples + 'QCDPt600.root',
                                    'QCDPt800'   : dirSamples + 'QCDPt800.root',
                                    'QCDPt1000'   : dirSamples + 'QCDPt1000.root',
                                    'QCDPt1400'   : dirSamples + 'QCDPt1400.root',
                                    'QCDPt1800'   : dirSamples + 'QCDPt1800.root',
                                    'QCDPt2400'   : dirSamples + 'QCDPt2400.root',
                                    'QCDPt3200'   : dirSamples + 'QCDPt3200.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_top'     : dirSamples + 'ST_top.root',
                                    'ttZJets'    : dirSamples + 'ttZJets.root',
                                    'ttWJets'    : dirSamples + 'ttWJets.root',
                                    'DYJets'     : dirSamples + 'DYJets.root',
                                    'tHQ'        : dirSamples + 'tHQ.root',
                                    'ZJets'      : dirSamples + 'ZJets.root',
                                    'ZZ'          : dirSamples + 'ZZ.root',
                                    'WW'          : dirSamples + 'WW.root',
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
                                    #'ST_antitop' : dirSamples + 'ST_antitop_JERDown.root',
                                    #'ST_top'     : dirSamples + 'ST_top_JERDown.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JERDown.root'
                                },
                    'JESUp' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg_JESUp.root',
                                    #'WJets'      : dirSamples + 'WJets_JESUp.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700_JESUp.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000_JESUp.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500_JESUp.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000_JESUp.root',
                                    #'ST_antitop' : dirSamples + 'ST_antitop_JESUp.root',
                                    #'ST_top'     : dirSamples + 'ST_top_JESUp.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JESUp.root'
                                },
                    'JESDown' : {
                                    'TTJets'     : dirSamples + 'TTJets_powheg_JESDown.root',
                                    #'WJets'      : dirSamples + 'WJets_JESDown.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700_JESDown.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000_JESDown.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500_JESDown.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000_JESDown.root',
                                    #'ST_antitop' : dirSamples + 'ST_antitop_JESDown.root',
                                    #'ST_top'     : dirSamples + 'ST_top_JESDown.root',
                                    #'ZJets'      : dirSamples + 'ZJets_JESDown.root'
                                }
                  
                  }
SignalFiles = { 'Nominal' : { 
                                'TbtH_1200_LH' : dirSamples + 'TbtH_1200_LH.root',
                                'TbtH_1200_RH' : dirSamples + 'TbtH_1200_RH.root',
                                'TttH_1200_LH' : dirSamples + 'TbtH_1200_LH.root',
                                'TttH_1200_RH' : dirSamples + 'TttH_1200_RH.root',
                                'TbtH_1800_LH' : dirSamples + 'TbtH_1800_LH.root',
                                'TttH_1800_RH' : dirSamples + 'TttH_1800_RH.root',
                                'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH.root',
                                'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH.root',
                                'TbtH_2600_10p_LH' : dirSamples + 'TbtH_2600_10p_LH.root',
                                'TttH_2600_10p_RH' : dirSamples + 'TttH_2600_10p_RH.root',
                               #'TbtH_1000_10p_LH' : dirSamples + 'TbtH_1000_10p_LH.root',
                              # 'TbtH_1200_10p_LH' : dirSamples + 'TbtH_1200_10p_LH.root',
                              # 'TbtH_1400_10p_LH' : dirSamples + 'TbtH_1400_10p_LH.root',
                              # 'TbtH_1600_10p_LH' : dirSamples + 'TbtH_1600_10p_LH.root',
                              #  'TbtH_1800_10p_LH' : dirSamples + 'TbtH_1800_10p_LH.root',
                               #'TbtH_2000_10p_LH' : dirSamples + 'TbtH_2000_10p_LH.root',
                              # 'TbtH_2400_10p_LH' : dirSamples + 'TbtH_2400_10p_LH.root',
                              # 'TbtH_2600_10p_LH' : dirSamples + 'TbtH_2600_10p_LH.root',
                              # 'TbtH_1000_20p_LH' : dirSamples + 'TbtH_1000_20p_LH.root',
                              # 'TbtH_1200_20p_LH' : dirSamples + 'TbtH_1200_20p_LH.root',
                              # 'TbtH_1400_20p_LH' : dirSamples + 'TbtH_1400_20p_LH.root',
                              # 'TbtH_1600_20p_LH' : dirSamples + 'TbtH_1600_20p_LH.root',
                              # 'TbtH_1800_20p_LH' : dirSamples + 'TbtH_1800_20p_LH.root',
                              # 'TbtH_2000_20p_LH' : dirSamples + 'TbtH_2000_20p_LH.root',
                              # 'TbtH_2400_20p_LH' : dirSamples + 'TbtH_2400_20p_LH.root',
                              # 'TbtH_2600_20p_LH' : dirSamples + 'TbtH_2600_20p_LH.root',
                              # 'TbtH_1000_30p_LH' : dirSamples + 'TbtH_1000_30p_LH.root',
                              # 'TbtH_1200_30p_LH' : dirSamples + 'TbtH_1200_30p_LH.root',
                              # 'TbtH_1400_30p_LH' : dirSamples + 'TbtH_1400_30p_LH.root',
                              # 'TbtH_1600_30p_LH' : dirSamples + 'TbtH_1600_30p_LH.root',
                              # 'TbtH_1800_30p_LH' : dirSamples + 'TbtH_1800_30p_LH.root',
                              # 'TbtH_2000_30p_LH' : dirSamples + 'TbtH_2000_30p_LH.root',
                              # 'TbtH_2400_30p_LH' : dirSamples + 'TbtH_2400_30p_LH.root',
                              # 'TbtH_2600_30p_LH' : dirSamples + 'TbtH_2600_30p_LH.root',
                              # 'TbtH_2000_10GeV_LH' : dirSamples + 'TbtH_2000_10GeV_LH.root',
                              # 'TbtH_2400_10GeV_LH' : dirSamples + 'TbtH_2400_10GeV_LH.root',
                              # 'TbtH_2600_10GeV_LH' : dirSamples + 'TbtH_2600_10GeV_LH.root',
 
                              # 'TttH_1000_10p_RH' : dirSamples + 'TttH_1000_10p_RH.root',
                              # 'TttH_1200_10p_RH' : dirSamples + 'TttH_1200_10p_RH.root',
                              # 'TttH_1400_10p_RH' : dirSamples + 'TttH_1400_10p_RH.root',
                              # 'TttH_1600_10p_RH' : dirSamples + 'TttH_1600_10p_RH.root',
                              # 'TttH_1800_10p_RH' : dirSamples + 'TttH_1800_10p_RH.root',
                              # 'TttH_2000_10p_RH' : dirSamples + 'TttH_2000_10p_RH.root',
                              # 'TttH_2400_10p_RH' : dirSamples + 'TttH_2400_10p_RH.root',
                              # 'TttH_2600_10p_RH' : dirSamples + 'TttH_2600_10p_RH.root',
                              # 'TttH_1000_20p_RH' : dirSamples + 'TttH_1000_20p_RH.root',
                              # 'TttH_1400_20p_RH' : dirSamples + 'TttH_1400_20p_RH.root',
                              # 'TttH_1600_20p_RH' : dirSamples + 'TttH_1600_20p_RH.root',
                              # 'TttH_1800_20p_RH' : dirSamples + 'TttH_1800_20p_RH.root',
                              # 'TttH_2400_20p_RH' : dirSamples + 'TttH_2400_20p_RH.root',
                              # 'TttH_2600_20p_RH' : dirSamples + 'TttH_2600_20p_RH.root',
                              # 'TttH_1000_30p_RH' : dirSamples + 'TttH_1000_30p_RH.root',
                              # 'TttH_1200_30p_RH' : dirSamples + 'TttH_2600_20p_RH.root',
                              # 'TttH_1400_30p_RH' : dirSamples + 'TttH_1400_30p_RH.root',
                              # 'TttH_1600_30p_RH' : dirSamples + 'TttH_1600_30p_RH.root',
                              # 'TttH_1800_30p_RH' : dirSamples + 'TttH_1800_30p_RH.root',
                              # 'TttH_2400_30p_RH' : dirSamples + 'TttH_2400_30p_RH.root',
                              # 'TttH_2600_30p_RH' : dirSamples + 'TttH_2600_30p_RH.root',
                              # 'TttH_2000_10GeV_RH' : dirSamples + 'TttH_2000_10GeV_RH.root',
                              # 'TttH_2400_10GeV_RH' : dirSamples + 'TttH_2400_10GeV_RH.root',
                              # 'TttH_2600_10GeV_RH' : dirSamples + 'TttH_2600_10GeV_RH.root',
 
                            },

                'JERUp'   : {
                               'TbtH_800_10p_LH' : dirSamples + 'TbtH_800_10p_LH_JERUp.root',
                               'TbtH_900_10p_LH' : dirSamples + 'TbtH_900_10p_LH_JERUp.root',
                               'TbtH_1000_10p_LH' : dirSamples + 'TbtH_1000_10p_LH_JERUp.root',
                               'TbtH_1100_10p_LH' : dirSamples + 'TbtH_1100_10p_LH_JERUp.root',
                               'TbtH_1200_10p_LH' : dirSamples + 'TbtH_1200_10p_LH_JERUp.root',
                               'TbtH_1300_10p_LH' : dirSamples + 'TbtH_1300_10p_LH_JERUp.root',
                               'TbtH_1400_10p_LH' : dirSamples + 'TbtH_1400_10p_LH_JERUp.root',
                               'TbtH_1500_10p_LH' : dirSamples + 'TbtH_1500_10p_LH_JERUp.root',
                               'TbtH_1700_10p_LH' : dirSamples + 'TbtH_1700_10p_LH_JERUp.root',
                               'TbtH_1800_10p_LH' : dirSamples + 'TbtH_1800_10p_LH_JERUp.root',
                               'TbtH_800_10p_RH' : dirSamples + 'TbtH_800_10p_RH_JERUp.root',
                               'TbtH_900_10p_RH' : dirSamples + 'TbtH_900_10p_RH_JERUp.root',
                               'TbtH_1000_10p_RH' : dirSamples + 'TbtH_1000_10p_RH_JERUp.root',
                               'TbtH_1100_10p_RH' : dirSamples + 'TbtH_1100_10p_RH_JERUp.root',
                               'TbtH_1200_10p_RH' : dirSamples + 'TbtH_1200_10p_RH_JERUp.root',
                               'TbtH_1300_10p_RH' : dirSamples + 'TbtH_1300_10p_RH_JERUp.root',
                               'TbtH_1400_10p_RH' : dirSamples + 'TbtH_1400_10p_RH_JERUp.root',
                               'TbtH_1500_10p_RH' : dirSamples + 'TbtH_1500_10p_RH_JERUp.root',
                               'TbtH_1700_10p_RH' : dirSamples + 'TbtH_1700_10p_RH_JERUp.root',
                               'TbtH_1800_10p_RH' : dirSamples + 'TbtH_1800_10p_RH_JERUp.root'
                            },
                'JERDown' : {
                               'TbtH_800_10p_LH' : dirSamples + 'TbtH_800_10p_LH_JERDown.root',
                               'TbtH_900_10p_LH' : dirSamples + 'TbtH_900_10p_LH_JERDown.root',
                               'TbtH_1000_10p_LH' : dirSamples + 'TbtH_1000_10p_LH_JERDown.root',
                               'TbtH_1100_10p_LH' : dirSamples + 'TbtH_1100_10p_LH_JERDown.root',
                               'TbtH_1200_10p_LH' : dirSamples + 'TbtH_1200_10p_LH_JERDown.root',
                               'TbtH_1300_10p_LH' : dirSamples + 'TbtH_1300_10p_LH_JERDown.root',
                               'TbtH_1400_10p_LH' : dirSamples + 'TbtH_1400_10p_LH_JERDown.root',
                               'TbtH_1500_10p_LH' : dirSamples + 'TbtH_1500_10p_LH_JERDown.root',
                               'TbtH_1700_10p_LH' : dirSamples + 'TbtH_1700_10p_LH_JERDown.root',
                               'TbtH_1800_10p_LH' : dirSamples + 'TbtH_1800_10p_LH_JERDown.root',
                               'TbtH_800_10p_RH' : dirSamples + 'TbtH_800_10p_RH_JERDown.root',
                               'TbtH_900_10p_RH' : dirSamples + 'TbtH_900_10p_RH_JERDown.root',
                               'TbtH_1000_10p_RH' : dirSamples + 'TbtH_1000_10p_RH_JERDown.root',
                               'TbtH_1100_10p_RH' : dirSamples + 'TbtH_1100_10p_RH_JERDown.root',
                               'TbtH_1200_10p_RH' : dirSamples + 'TbtH_1200_10p_RH_JERDown.root',
                               'TbtH_1300_10p_RH' : dirSamples + 'TbtH_1300_10p_RH_JERDown.root',
                               'TbtH_1400_10p_RH' : dirSamples + 'TbtH_1400_10p_RH_JERDown.root',
                               'TbtH_1500_10p_RH' : dirSamples + 'TbtH_1500_10p_RH_JERDown.root',
                               'TbtH_1700_10p_RH' : dirSamples + 'TbtH_1700_10p_RH_JERDown.root',
                               'TbtH_1800_10p_RH' : dirSamples + 'TbtH_1800_10p_RH_JERDown.root'
                            },
                'JESUp'   : {
                               'TbtH_800_10p_LH' : dirSamples + 'TbtH_800_10p_LH_JESUp.root',
                               'TbtH_900_10p_LH' : dirSamples + 'TbtH_900_10p_LH_JESUp.root',
                               'TbtH_1000_10p_LH' : dirSamples + 'TbtH_1000_10p_LH_JESUp.root',
                               'TbtH_1100_10p_LH' : dirSamples + 'TbtH_1100_10p_LH_JESUp.root',
                               'TbtH_1200_10p_LH' : dirSamples + 'TbtH_1200_10p_LH_JESUp.root',
                               'TbtH_1300_10p_LH' : dirSamples + 'TbtH_1300_10p_LH_JESUp.root',
                               'TbtH_1400_10p_LH' : dirSamples + 'TbtH_1400_10p_LH_JESUp.root',
                               'TbtH_1500_10p_LH' : dirSamples + 'TbtH_1500_10p_LH_JESUp.root',
                               'TbtH_1700_10p_LH' : dirSamples + 'TbtH_1700_10p_LH_JESUp.root',
                               'TbtH_1800_10p_LH' : dirSamples + 'TbtH_1800_10p_LH_JESUp.root',
                               'TbtH_800_10p_RH' : dirSamples + 'TbtH_800_10p_RH_JESUp.root',
                               'TbtH_900_10p_RH' : dirSamples + 'TbtH_900_10p_RH_JESUp.root',
                               'TbtH_1000_10p_RH' : dirSamples + 'TbtH_1000_10p_RH_JESUp.root',
                               'TbtH_1100_10p_RH' : dirSamples + 'TbtH_1100_10p_RH_JESUp.root',
                               'TbtH_1200_10p_RH' : dirSamples + 'TbtH_1200_10p_RH_JESUp.root',
                               'TbtH_1300_10p_RH' : dirSamples + 'TbtH_1300_10p_RH_JESUp.root',
                               'TbtH_1400_10p_RH' : dirSamples + 'TbtH_1400_10p_RH_JESUp.root',
                               'TbtH_1500_10p_RH' : dirSamples + 'TbtH_1500_10p_RH_JESUp.root',
                               'TbtH_1700_10p_RH' : dirSamples + 'TbtH_1700_10p_RH_JESUp.root',
                               'TbtH_1800_10p_RH' : dirSamples + 'TbtH_1800_10p_RH_JESUp.root'
                            },
                'JESDown' : {
                               'TbtH_800_10p_LH' : dirSamples + 'TbtH_800_10p_LH_JESDown.root',
                               'TbtH_900_10p_LH' : dirSamples + 'TbtH_900_10p_LH_JESDown.root',
                               'TbtH_1000_10p_LH' : dirSamples + 'TbtH_1000_10p_LH_JESDown.root',
                               'TbtH_1100_10p_LH' : dirSamples + 'TbtH_1100_10p_LH_JESDown.root',
                               'TbtH_1200_10p_LH' : dirSamples + 'TbtH_1200_10p_LH_JESDown.root',
                               'TbtH_1300_10p_LH' : dirSamples + 'TbtH_1300_10p_LH_JESDown.root',
                               'TbtH_1400_10p_LH' : dirSamples + 'TbtH_1400_10p_LH_JESDown.root',
                               'TbtH_1500_10p_LH' : dirSamples + 'TbtH_1500_10p_LH_JESDown.root',
                               'TbtH_1700_10p_LH' : dirSamples + 'TbtH_1700_10p_LH_JESDown.root',
                               'TbtH_1800_10p_LH' : dirSamples + 'TbtH_1800_10p_LH_JESDown.root',
                               'TbtH_800_10p_RH' : dirSamples + 'TbtH_800_10p_RH_JESDown.root',
                               'TbtH_900_10p_RH' : dirSamples + 'TbtH_900_10p_RH_JESDown.root',
                               'TbtH_1000_10p_RH' : dirSamples + 'TbtH_1000_10p_RH_JESDown.root',
                               'TbtH_1100_10p_RH' : dirSamples + 'TbtH_1100_10p_RH_JESDown.root',
                               'TbtH_1200_10p_RH' : dirSamples + 'TbtH_1200_10p_RH_JESDown.root',
                               'TbtH_1300_10p_RH' : dirSamples + 'TbtH_1300_10p_RH_JESDown.root',
                               'TbtH_1400_10p_RH' : dirSamples + 'TbtH_1400_10p_RH_JESDown.root',
                               'TbtH_1500_10p_RH' : dirSamples + 'TbtH_1500_10p_RH_JESDown.root',
                               'TbtH_1700_10p_RH' : dirSamples + 'TbtH_1700_10p_RH_JESDown.root',
                               'TbtH_1800_10p_RH' : dirSamples + 'TbtH_1800_10p_RH_JESDown.root'
                            } 
          }

# Dictionary containing the x-sections of each of the MC samples
sampleXsec = {
               'TTJets'       : 831.76,
               'WJets'        : 95.14,
               'QCDHT100'     : 27540000,
               'QCDHT200'     : 1,
               'QCDHT300'     : 351300,
               'QCDHT500'     : 31630,
               'QCDHT700'     : 6831,
               'QCDHT1000'    : 1207,
               'QCDHT1500'    : 119.9,
               'QCDHT2000'    : 25.24,
               'QCDPt80'     : 2762530,
               'QCDPt120'    : 471100,
               'QCDPt170'    : 117276., 
               'QCDPt300'    : 7823.,
               'QCDPt470'    : 648.2,
               'QCDPt600'    : 186.9,
               'QCDPt800'    : 32.293,
               'QCDPt1000'   : 9.4183,
               'QCDPt1400'   : 0.84265,
               'QCDPt1800'   : 0.114943,
               'QCDPt2400'   : 0.00682981,
               'QCDPt3200'   : 0.000165445,
               'ST'           : 35.6,
               'ZJets'        : 6.97,
               'DYJets'        : 1187, #LO
               'ttZJets'      : 0.616, #LO
               'ttWJets'      : 0.511, #LO
               'tHQ'          : 0.2608,
               'WW'           : 28.7,
               'ZZ'           : 6.842,

               'TbtH_1200_LH' :0.0614,
               'TttH_1200_LH' :0.0145,
               'TbtH_1200_RH' :0.0614,
               'TttH_1200_RH' :0.0145,

               'TbtH_1800_LH' :0.0109,
               'TttH_1800_RH' :0.00324,

               'TbtH_1200_10p_LH' :0.0614,
               'TbtH_1800_10p_LH' :0.0109,
               'TbtH_2400_10p_LH' :0.00222,
               'TbtH_2600_10p_LH' :0.00122,

               'TttH_2400_10p_LH' :0.000283,
               'TttH_2600_10p_RH' :0.000155,

               'TbtZ_1200_RH' :0.0614,
               'TbtZ_1800_RH' :0.0109,
             }

