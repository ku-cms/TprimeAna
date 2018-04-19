#!/usr/bin/env python
import ROOT as rt
# lfn of samples to be run over
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_new_fix_v2/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_new_fix_v3/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_new_fix_jmr_v2/'
dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_new_fix_jmr_v2_cutflow/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_newTop_v3/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_newTop_massWindow_v3/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_sys_annulus_fixed_cutflow/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_sys_annulus_true/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_new/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_sys_v1/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_sys_v1_cutflow/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_v2p4_sys_v6/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_reduced/samples_v2p4_sys_v6_cutflow/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_v2p4_sys_v2/'
#dirSamples = '/home/t3-ku/erichjs/work/B2G/CMSSW_8_0_15/src/TprimeAna/test/80X_3p2/samples_med/'

# data Luminosity
lumi = 35865.177 #B-H
#lumi = 27954.748#lumi = 12884.276
#lumi = 12884.276

# Dictionaries of sample names and root files
Data = { 
         'JetHT_2016B'      : dirSamples + 'JetHT_2016B.root',
         'JetHT_2016C'      : dirSamples + 'JetHT_2016C.root',
         'JetHT_2016D'      : dirSamples + 'JetHT_2016D.root',
         'JetHT_2016E'      : dirSamples + 'JetHT_2016E.root',
         'JetHT_2016F'      : dirSamples + 'JetHT_2016F.root',
         'JetHT_2016G'      : dirSamples + 'JetHT_2016G.root',
         'JetHT_2016H_v2'      : dirSamples + 'JetHT_2016H_v2.root',
         'JetHT_2016H_v3'      : dirSamples + 'JetHT_2016H_v3.root',
         #'JetHT_2016H_v3'      : dirSamples + 'JetHT_2016H_v3_reduced.root',
       }

BackgroundFilesHT = { 'Nominal' : {
                                    'TTJets'     : dirSamples + 'TTJets.root',
                                    #'TTJetsMTT700'     : dirSamples + 'TTJetsMTT700.root',
                                    #'TTJetsMTT1000'     : dirSamples + 'TTJetsMTT700.root',
                                    'WJets'      : dirSamples + 'WJets.root',
                                    #'QCDHT100'   : dirSamples + 'QCDHT100.root',
                                    #'QCDHT200'   : dirSamples + 'QCDHT200.root',
                                    #'QCDHT300'   : dirSamples + 'QCDHT300.root',
                                    'QCDHT500'   : dirSamples + 'QCDHT500.root',
                                    'QCDHT700'   : dirSamples + 'QCDHT700.root',
                                    'QCDHT1000'  : dirSamples + 'QCDHT1000.root',
                                    'QCDHT1500'  : dirSamples + 'QCDHT1500.root',
                                    'QCDHT2000'  : dirSamples + 'QCDHT2000.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_top'     : dirSamples + 'ST_top.root',
                                    'ST_t_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_t_top'     : dirSamples + 'ST_top.root',
                                    'ttZJets'    : dirSamples + 'ttZJets.root',
                                    'ttWJets'    : dirSamples + 'ttWJets.root',
                                    #'DYJets'     : dirSamples + 'DYJets.root',
                                    #'ttHJets'    : dirSamples + 'ttHJets.root',
                                    #'tHQ'        : dirSamples + 'tHQ.root',
                                    'ZJets'      : dirSamples + 'ZJets.root',
                                    'ZZ'          : dirSamples + 'ZZ.root',
                                    'WW'          : dirSamples + 'WW.root',
                                    'WZ'          : dirSamples + 'WZ.root',
                                },
                    }
BackgroundFilesPt = { 'Nominal' : {
                                    'TTJets'     : dirSamples + 'TTJets.root',
                                    #'TTJets_test'     : dirSamples + 'TTJets_test.root',
                                    #'TTJetsMtt700'     : dirSamples + 'TTJetsMTT700.root',
                                    #'TTJetsMtt1000'     : dirSamples + 'TTJetsMTT1000.root',
                                    'WJets'      : dirSamples + 'WJets.root',
                                    'ST_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_top'     : dirSamples + 'ST_top.root',
                                    'ST_t_antitop' : dirSamples + 'ST_antitop.root',
                                    'ST_t_top'     : dirSamples + 'ST_top.root',
                                    'ttZJets'    : dirSamples + 'ttZJets.root',
                                    'ttWJets'    : dirSamples + 'ttWJets.root',
                                    'ttHJets'    : dirSamples + 'ttHJets.root',
                                    #'DYJets'     : dirSamples + 'DYJets.root',
                                    'tHQ'        : dirSamples + 'tHQ.root',
                                    'ZJets'      : dirSamples + 'ZJets.root',
                                    'ZZ'          : dirSamples + 'ZZ.root',
                                    'WW'          : dirSamples + 'WW.root',
                                    'WZ'          : dirSamples + 'WZ.root',
                                    #'QCDPt80'   : dirSamples + 'QCDPt80.root',
                                    #'QCDPt120'   : dirSamples + 'QCDPt120.root',
                                    #'QCDPt170'   : dirSamples + 'QCDPt170.root',
                                    'QCDPt300'   : dirSamples + 'QCDPt300.root',
                                    'QCDPt470'   : dirSamples + 'QCDPt470.root',
                                    'QCDPt600'   : dirSamples + 'QCDPt600.root',
                                    'QCDPt800'   : dirSamples + 'QCDPt800.root',
                                    'QCDPt1000'   : dirSamples + 'QCDPt1000.root',
                                    'QCDPt1400'   : dirSamples + 'QCDPt1400.root',
                                    'QCDPt1800'   : dirSamples + 'QCDPt1800.root',
                                    'QCDPt2400'   : dirSamples + 'QCDPt2400.root',
                                    'QCDPt3200'   : dirSamples + 'QCDPt3200.root',
                                },
                  }
SignalFiles = { 'Nominal' : { 
                  #              'TpTp_800'  : dirSamples + 'TpTp_800.root',
                  #              'TpTp_900'  : dirSamples + 'TpTp_900.root',
                  #              'TpTp_1000' : dirSamples + 'TpTp_1000.root',
                  #              'TpTp_1100' : dirSamples + 'TpTp_1100.root',
                  #              'TpTp_1200' : dirSamples + 'TpTp_1200.root',
                  #              'TpTp_1300' : dirSamples + 'TpTp_1300.root',
                  #              'TpTp_1400' : dirSamples + 'TpTp_1400.root',
                  #              'TpTp_1500' : dirSamples + 'TpTp_1500.root',
                  #              #'TpTp_1600' : dirSamples + 'TpTp_1600.root',
                  #              'TpTp_1700' : dirSamples + 'TpTp_1700.root',
                  #              'TpTp_1800' : dirSamples + 'TpTp_1800.root',

                                'TbtH_800_LH'  : dirSamples + 'TbtH_800_LH.root',
                                'TbtH_900_LH'  : dirSamples + 'TbtH_900_LH.root',
                                'TbtH_1000_LH' : dirSamples + 'TbtH_1000_LH.root',
                                'TbtH_1100_LH' : dirSamples + 'TbtH_1100_LH.root',
                                'TbtH_1200_LH' : dirSamples + 'TbtH_1200_LH.root',
                 #               'TbtH_1200_LH_test' : dirSamples + 'TbtH_1200_LH_test.root',
                                'TbtH_1300_LH' : dirSamples + 'TbtH_1300_LH.root',
                                'TbtH_1400_LH' : dirSamples + 'TbtH_1400_LH.root',
                                'TbtH_1500_LH' : dirSamples + 'TbtH_1500_LH.root',
                                'TbtH_1700_LH' : dirSamples + 'TbtH_1700_LH.root',
                                'TbtH_1800_LH' : dirSamples + 'TbtH_1800_LH.root',
                 #               'TbtH_1800_LH_test' : dirSamples + 'TbtH_1800_LH_test.root',

                 #               'TbtH_800_RH' : dirSamples + 'TbtH_800_RH.root',
                 #               'TbtH_900_RH' : dirSamples + 'TbtH_900_RH.root',
                 #               'TbtH_1000_RH' : dirSamples + 'TbtH_1000_RH.root',
                 #               'TbtH_1100_RH' : dirSamples + 'TbtH_1100_RH.root',
                 #               'TbtH_1200_RH' : dirSamples + 'TbtH_1200_RH.root',
                 #               'TbtH_1300_RH' : dirSamples + 'TbtH_1300_RH.root',
                 #               'TbtH_1400_RH' : dirSamples + 'TbtH_1400_RH.root',
                 #               'TbtH_1500_RH' : dirSamples + 'TbtH_1500_RH.root',
                 #               'TbtH_1700_RH' : dirSamples + 'TbtH_1700_RH.root',
                 #               'TbtH_1800_RH' : dirSamples + 'TbtH_1800_RH.root',

                 #               'TttH_800_LH' : dirSamples + 'TttH_800_LH.root',
                 #               'TttH_900_LH' : dirSamples + 'TttH_900_LH.root',
                 #               'TttH_1000_LH' : dirSamples + 'TttH_1000_LH.root',
                 #               'TttH_1100_LH' : dirSamples + 'TttH_1100_LH.root',
                 #               'TttH_1200_LH' : dirSamples + 'TttH_1200_LH.root',
                 #               'TttH_1300_LH' : dirSamples + 'TttH_1300_LH.root',
                 #               'TttH_1400_LH' : dirSamples + 'TttH_1400_LH.root',
                 #               'TttH_1500_LH' : dirSamples + 'TttH_1500_LH.root',
                 #               'TttH_1700_LH' : dirSamples + 'TttH_1700_LH.root',
                 #               'TttH_1800_LH' : dirSamples + 'TttH_1800_LH.root',

                 #               'TttH_800_RH'  : dirSamples + 'TttH_800_RH.root',
                 #               'TttH_900_RH'  : dirSamples + 'TttH_900_RH.root',
                 #               'TttH_1000_RH' : dirSamples + 'TttH_1000_RH.root',
                 #               'TttH_1100_RH' : dirSamples + 'TttH_1100_RH.root',
                 #               'TttH_1200_RH' : dirSamples + 'TttH_1200_RH.root',
                 #               'TttH_1300_RH' : dirSamples + 'TttH_1300_RH.root',
                 #               'TttH_1400_RH' : dirSamples + 'TttH_1400_RH.root',
                 #               'TttH_1500_RH' : dirSamples + 'TttH_1500_RH.root',
                 #               'TttH_1700_RH' : dirSamples + 'TttH_1700_RH.root',
                 #               'TttH_1800_RH' : dirSamples + 'TttH_1800_RH.root',

                 #               'TbtZ_800_LH' : dirSamples + 'TbtZ_800_LH.root',
                 #               'TbtZ_900_LH' : dirSamples + 'TbtZ_900_LH.root',
                 #               'TbtZ_1000_LH' : dirSamples + 'TbtZ_1000_LH.root',
                 #               'TbtZ_1100_LH' : dirSamples + 'TbtZ_1100_LH.root',
                 #               'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH.root',
                 #               'TbtZ_1300_LH' : dirSamples + 'TbtZ_1300_LH.root',
                 #               'TbtZ_1400_LH' : dirSamples + 'TbtZ_1400_LH.root',
                 #               'TbtZ_1500_LH' : dirSamples + 'TbtZ_1500_LH.root',
                 #               'TbtZ_1700_LH' : dirSamples + 'TbtZ_1700_LH.root',
                 #               'TbtZ_1800_LH' : dirSamples + 'TbtZ_1800_LH.root',

                 #               'TbtZ_800_RH' : dirSamples + 'TbtZ_800_RH.root',
                 #               'TbtZ_900_RH' : dirSamples + 'TbtZ_900_RH.root',
                 #               'TbtZ_1000_RH' : dirSamples + 'TbtZ_1000_RH.root',
                 #               'TbtZ_1100_RH' : dirSamples + 'TbtZ_1100_RH.root',
                 #               'TbtZ_1200_RH' : dirSamples + 'TbtZ_1200_RH.root',
                 #               'TbtZ_1300_RH' : dirSamples + 'TbtZ_1300_RH.root',
                 #               'TbtZ_1400_RH' : dirSamples + 'TbtZ_1400_RH.root',
                 #               'TbtZ_1500_RH' : dirSamples + 'TbtZ_1500_RH.root',
                 #               'TbtZ_1700_RH' : dirSamples + 'TbtZ_1700_RH.root',
                 #               'TbtZ_1800_RH' : dirSamples + 'TbtZ_1800_RH.root',

                 #               'TttZ_800_LH' : dirSamples + 'TttZ_800_LH.root',
                 #               'TttZ_900_LH' : dirSamples + 'TttZ_900_LH.root',
                 #               'TttZ_1000_LH' : dirSamples + 'TttZ_1000_LH.root',
                 #               'TttZ_1100_LH' : dirSamples + 'TttZ_1100_LH.root',
                 #               'TttZ_1200_LH' : dirSamples + 'TttZ_1200_LH.root',
                 #               'TttZ_1300_LH' : dirSamples + 'TttZ_1300_LH.root',
                 #               'TttZ_1400_LH' : dirSamples + 'TttZ_1400_LH.root',
                 #               'TttZ_1500_LH' : dirSamples + 'TttZ_1500_LH.root',
                 #               'TttZ_1700_LH' : dirSamples + 'TttZ_1700_LH.root',
                 #               'TttZ_1800_LH' : dirSamples + 'TttZ_1800_LH.root',

                 #               'TttZ_800_RH' : dirSamples + 'TttZ_800_RH.root',
                 #               'TttZ_900_RH' : dirSamples + 'TttZ_900_RH.root',
                 #               'TttZ_1000_RH' : dirSamples + 'TttZ_1000_RH.root',
                 #               'TttZ_1100_RH' : dirSamples + 'TttZ_1100_RH.root',
                 #               'TttZ_1200_RH' : dirSamples + 'TttZ_1200_RH.root',
                 #               'TttZ_1300_RH' : dirSamples + 'TttZ_1300_RH.root',
                 #               'TttZ_1400_RH' : dirSamples + 'TttZ_1400_RH.root',
                 #               'TttZ_1500_RH' : dirSamples + 'TttZ_1500_RH.root',
                 #               'TttZ_1700_RH' : dirSamples + 'TttZ_1700_RH.root',
                 #               'TttZ_1800_RH' : dirSamples + 'TttZ_1800_RH.root',

                 #            'TbtH_800_10p_LH' : dirSamples + 'TbtH_800_10p_LH.root',
                 #            'TbtH_1000_10p_LH' : dirSamples + 'TbtH_1000_10p_LH.root',
                 #            'TbtH_1200_10p_LH' : dirSamples + 'TbtH_1200_10p_LH.root',
                 #            'TbtH_1400_10p_LH' : dirSamples + 'TbtH_1400_10p_LH.root',
                 #            'TbtH_1600_10p_LH' : dirSamples + 'TbtH_1600_10p_LH.root',
                 #            'TbtH_1800_10p_LH' : dirSamples + 'TbtH_1800_10p_LH.root',
                 #            'TbtH_2000_10p_LH' : dirSamples + 'TbtH_2000_10p_LH.root',
                 #            'TbtH_2200_10p_LH' : dirSamples + 'TbtH_2200_10p_LH.root',
                 #            'TbtH_2400_10p_LH' : dirSamples + 'TbtH_2400_10p_LH.root',
                 #            'TbtH_2600_10p_LH' : dirSamples + 'TbtH_2600_10p_LH.root',

                 #            'TbtH_800_20p_LH' : dirSamples + 'TbtH_800_20p_LH.root',
                 #            'TbtH_1000_20p_LH' : dirSamples + 'TbtH_1000_20p_LH.root',
                 #            'TbtH_1200_20p_LH' : dirSamples + 'TbtH_1200_20p_LH.root',
                 #            'TbtH_1400_20p_LH' : dirSamples + 'TbtH_1400_20p_LH.root',
                 #            'TbtH_1600_20p_LH' : dirSamples + 'TbtH_1600_20p_LH.root',
                 #            'TbtH_1800_20p_LH' : dirSamples + 'TbtH_1800_20p_LH.root',
                 #            'TbtH_2000_20p_LH' : dirSamples + 'TbtH_2000_20p_LH.root',
                 #            'TbtH_2200_20p_LH' : dirSamples + 'TbtH_2200_20p_LH.root',
                 #            'TbtH_2400_20p_LH' : dirSamples + 'TbtH_2400_20p_LH.root',
                 #            'TbtH_2600_20p_LH' : dirSamples + 'TbtH_2600_20p_LH.root',

                 #            'TbtH_800_30p_LH' : dirSamples + 'TbtH_800_30p_LH.root',
                 #            'TbtH_1000_30p_LH' : dirSamples + 'TbtH_1000_30p_LH.root',
                 #            'TbtH_1200_30p_LH' : dirSamples + 'TbtH_1200_30p_LH.root',
                 #            'TbtH_1400_30p_LH' : dirSamples + 'TbtH_1400_30p_LH.root',
                 #            'TbtH_1600_30p_LH' : dirSamples + 'TbtH_1600_30p_LH.root',
                 #            'TbtH_1800_30p_LH' : dirSamples + 'TbtH_1800_30p_LH.root',
                 #            'TbtH_2000_30p_LH' : dirSamples + 'TbtH_2000_30p_LH.root',
                 #            'TbtH_2200_30p_LH' : dirSamples + 'TbtH_2200_30p_LH.root',
                 #            'TbtH_2400_30p_LH' : dirSamples + 'TbtH_2400_30p_LH.root',
                 #            'TbtH_2600_30p_LH' : dirSamples + 'TbtH_2600_30p_LH.root',

                 #            'TbtH_2000_10GeV_LH' : dirSamples + 'TbtH_2000_10GeV_LH.root',
                 #            'TbtH_2200_10GeV_LH' : dirSamples + 'TbtH_2200_10GeV_LH.root',
                 #            'TbtH_2400_10GeV_LH' : dirSamples + 'TbtH_2400_10GeV_LH.root',
                 #            'TbtH_2600_10GeV_LH' : dirSamples + 'TbtH_2600_10GeV_LH.root',
 
                 #            'TttH_800_10p_RH' : dirSamples + 'TttH_800_10p_RH.root',
                 #            'TttH_1000_10p_RH' : dirSamples + 'TttH_1000_10p_RH.root',
                 #            'TttH_1200_10p_RH' : dirSamples + 'TttH_1200_10p_RH.root',
                 #            'TttH_1400_10p_RH' : dirSamples + 'TttH_1400_10p_RH.root',
                 #            'TttH_1600_10p_RH' : dirSamples + 'TttH_1600_10p_RH.root',
                 #            'TttH_1800_10p_RH' : dirSamples + 'TttH_1800_10p_RH.root',
                 #            'TttH_2000_10p_RH' : dirSamples + 'TttH_2000_10p_RH.root',
                 #            'TttH_2200_10p_RH' : dirSamples + 'TttH_2200_10p_RH.root',
                 #            'TttH_2400_10p_RH' : dirSamples + 'TttH_2400_10p_RH.root',
                 #            'TttH_2600_10p_RH' : dirSamples + 'TttH_2600_10p_RH.root',

                 #            'TttH_800_20p_RH' : dirSamples + 'TttH_800_20p_RH.root',
                 #            'TttH_1000_20p_RH' : dirSamples + 'TttH_1000_20p_RH.root',
                 #            #'TttH_1200_20p_RH' : dirSamples + 'TttH_1200_20p_RH.root',
                 #            'TttH_1400_20p_RH' : dirSamples + 'TttH_1400_20p_RH.root',
                 #            'TttH_1600_20p_RH' : dirSamples + 'TttH_1600_20p_RH.root',
                 #            'TttH_1800_20p_RH' : dirSamples + 'TttH_1800_20p_RH.root',
                 #            'TttH_2000_20p_RH' : dirSamples + 'TttH_2000_20p_RH.root',
                 #            'TttH_2200_20p_RH' : dirSamples + 'TttH_2200_20p_RH.root',
                 #            'TttH_2400_20p_RH' : dirSamples + 'TttH_2400_20p_RH.root',
                 #            'TttH_2600_20p_RH' : dirSamples + 'TttH_2600_20p_RH.root',

                 #            'TttH_800_30p_RH' : dirSamples + 'TttH_800_30p_RH.root',
                 #            'TttH_1000_30p_RH' : dirSamples + 'TttH_1000_30p_RH.root',
                 #            'TttH_1200_30p_RH' : dirSamples + 'TttH_1200_30p_RH.root',
                 #            'TttH_1400_30p_RH' : dirSamples + 'TttH_1400_30p_RH.root',
                 #            'TttH_1600_30p_RH' : dirSamples + 'TttH_1600_30p_RH.root',
                 #            'TttH_1800_30p_RH' : dirSamples + 'TttH_1800_30p_RH.root',
                 #            #'TttH_2000_30p_RH' : dirSamples + 'TttH_2000_30p_RH.root',
                 #            'TttH_2200_30p_RH' : dirSamples + 'TttH_2200_30p_RH.root',
                 #            'TttH_2400_30p_RH' : dirSamples + 'TttH_2400_30p_RH.root',
                 #            'TttH_2600_30p_RH' : dirSamples + 'TttH_2600_30p_RH.root',

                 #            'TttH_2000_10GeV_RH' : dirSamples + 'TttH_2000_10GeV_RH.root',
                 #            'TttH_2200_10GeV_RH' : dirSamples + 'TttH_2200_10GeV_RH.root',
                 #            'TttH_2400_10GeV_RH' : dirSamples + 'TttH_2400_10GeV_RH.root',
                 #            'TttH_2600_10GeV_RH' : dirSamples + 'TttH_2600_10GeV_RH.root',

                 #            'TbtZ_800_10p_LH' : dirSamples + 'TbtZ_800_10p_LH.root',
                 #            'TbtZ_1000_10p_LH' : dirSamples + 'TbtZ_1000_10p_LH.root',
                 #            'TbtZ_1200_10p_LH' : dirSamples + 'TbtZ_1200_10p_LH.root',
                 #            'TbtZ_1400_10p_LH' : dirSamples + 'TbtZ_1400_10p_LH.root',
                 #            'TbtZ_1600_10p_LH' : dirSamples + 'TbtZ_1600_10p_LH.root',
                 #            'TbtZ_1800_10p_LH' : dirSamples + 'TbtZ_1800_10p_LH.root',
                 #            'TbtZ_2000_10p_LH' : dirSamples + 'TbtZ_2000_10p_LH.root',

                 #            'TbtZ_800_20p_LH' : dirSamples + 'TbtZ_800_20p_LH.root',
                 #            #'TbtZ_1000_20p_LH' : dirSamples + 'TbtZ_1000_20p_LH.root',
                 #            'TbtZ_1200_20p_LH' : dirSamples + 'TbtZ_1200_20p_LH.root',
                 #            'TbtZ_1400_20p_LH' : dirSamples + 'TbtZ_1400_20p_LH.root',
                 #            'TbtZ_1600_20p_LH' : dirSamples + 'TbtZ_1600_20p_LH.root',
                 #            'TbtZ_1800_20p_LH' : dirSamples + 'TbtZ_1800_20p_LH.root',
                 #            'TbtZ_2000_20p_LH' : dirSamples + 'TbtZ_2000_20p_LH.root',

                 #            'TbtZ_800_30p_LH' : dirSamples + 'TbtZ_800_30p_LH.root',
                 #            'TbtZ_1000_30p_LH' : dirSamples + 'TbtZ_1000_30p_LH.root',
                 #            'TbtZ_1200_30p_LH' : dirSamples + 'TbtZ_1200_30p_LH.root',
                 #            'TbtZ_1400_30p_LH' : dirSamples + 'TbtZ_1400_30p_LH.root',
                 #            'TbtZ_1600_30p_LH' : dirSamples + 'TbtZ_1600_30p_LH.root',
                 #            'TbtZ_1800_30p_LH' : dirSamples + 'TbtZ_1800_30p_LH.root',
                 #            'TbtZ_2000_30p_LH' : dirSamples + 'TbtZ_2000_30p_LH.root',
 
                 #            'TttZ_800_10p_RH' : dirSamples + 'TttZ_800_10p_RH.root',
                 #            'TttZ_1000_10p_RH' : dirSamples + 'TttZ_1000_10p_RH.root',
                 #            'TttZ_1200_10p_RH' : dirSamples + 'TttZ_1200_10p_RH.root',
                 #            'TttZ_1400_10p_RH' : dirSamples + 'TttZ_1400_10p_RH.root',
                 #            'TttZ_1600_10p_RH' : dirSamples + 'TttZ_1600_10p_RH.root',
                 #            'TttZ_1800_10p_RH' : dirSamples + 'TttZ_1800_10p_RH.root',
                 #            'TttZ_2000_10p_RH' : dirSamples + 'TttZ_2000_10p_RH.root',

                 #            'TttZ_800_20p_RH' : dirSamples + 'TttZ_800_20p_RH.root',
                 #            #'TttZ_1000_20p_RH' : dirSamples + 'TttZ_1000_20p_RH.root',
                 #            'TttZ_1200_20p_RH' : dirSamples + 'TttZ_1200_20p_RH.root',
                 #            'TttZ_1400_20p_RH' : dirSamples + 'TttZ_1400_20p_RH.root',
                 #            'TttZ_1600_20p_RH' : dirSamples + 'TttZ_1600_20p_RH.root',
                 #            'TttZ_1800_20p_RH' : dirSamples + 'TttZ_1800_20p_RH.root',
                 #            'TttZ_2000_20p_RH' : dirSamples + 'TttZ_2000_20p_RH.root',

                 #            'TttZ_800_30p_RH' : dirSamples + 'TttZ_800_30p_RH.root',
                 #            'TttZ_1000_30p_RH' : dirSamples + 'TttZ_1000_30p_RH.root',
                 #            'TttZ_1200_30p_RH' : dirSamples + 'TttZ_1200_30p_RH.root',
                 #            'TttZ_1400_30p_RH' : dirSamples + 'TttZ_1400_30p_RH.root',
                 #            'TttZ_1600_30p_RH' : dirSamples + 'TttZ_1600_30p_RH.root',
                 #            'TttZ_1800_30p_RH' : dirSamples + 'TttZ_1800_30p_RH.root',
                 #            'TttZ_2000_30p_RH' : dirSamples + 'TttZ_2000_30p_RH.root',
                            },
          }

# Dictionary containing the x-sections of each of the MC samples
sampleXsec = {
               'TTJets'       : 831.76,
               'TTJets_test'       : 831.76,
               'TTJetsMtt700' : 831.76 * 0.0921 ,
               'TTJetsMtt1000': 831.76 * 0.02474,
               #'TTJetsMtt700' : 831.76  ,
               #'TTJetsMtt1000': 831.76 ,
               'WJets'        : 95.14,
               'QCDHT100'     : 27540000,
               'QCDHT200'     : 2000000,
               'QCDHT300'     : 351300,
               'QCDHT500'     : 31630,
               'QCDHT700'     : 6831,
               'QCDHT1000'    : 1207,
               'QCDHT1500'    : 119.9,
               'QCDHT2000'    : 25.24,
               'QCDPt80'     : 2735000.,
               'QCDPt120'    : 467500.,
               'QCDPt170'    : 117400., 
               'QCDPt300'    : 7753.,
               'QCDPt470'    : 642.1,
               'QCDPt600'    : 185.9,
               'QCDPt800'    : 32.05,
               'QCDPt1000'   : 9.365,
               'QCDPt1400'   : 0.8398,
               'QCDPt1800'   : 0.1124,
               'QCDPt2400'   : 0.006752,
               'QCDPt3200'   : 0.0001626,
               'ST'           : 35.6,
               'ST_t_top'     : 136.02,
               'ST_t_antitop' : 80.95,
               'ZJets'        : 6.97,
               'DYJets'        : 1187, #LO
               'ttZJets'      : 0.6529, #LO
               'ttHJets'      : 0.295, #LO
               'ttWJets'      : 0.511, #LO
               'tHQ'          : 0.2609,
               'WW'           : 45.2,
               'WZ'           : 23.43,
               'ZZ'           : 6.912,

               'TbtH_800_LH'      :0.24125,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_800_LH'      :0.0665,# *(0.5*0.5)*0.50 = 0.1250
               'TbtH_800_RH'      :0.24125,
               'TttH_800_RH'      :0.0665,

               'TbtH_900_LH'      :0.170,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_900_LH'      :0.0485,# *(0.5*0.5)*0.50 = 0.1250
               'TbtH_900_RH'      :0.170,
               'TttH_900_RH'      :0.0485,

               'TbtH_1000_LH'     :0.121875,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_1000_LH'     :0.035625,# *(0.5*0.5)*0.50 = 0.1250
               'TbtH_1000_RH'     :0.121875,
               'TttH_1000_RH'     :0.035625,

               'TbtH_1100_LH'     :0.084375,
               'TttH_1100_LH'     :0.0265,
               'TbtH_1100_RH'     :0.084375,
               'TttH_1100_RH'     :0.0265,

               'TbtH_1200_LH'     :0.061375,
               'TbtH_1200_LH_test'     :0.061375,
               'TttH_1200_LH'     :0.019875,
               'TbtH_1200_RH'     :0.061375,
               'TttH_1200_RH'     :0.019875,

               'TbtH_1300_LH'     :0.04475,
               'TttH_1300_LH'     :0.015,
               'TbtH_1300_RH'     :0.04475,
               'TttH_1300_RH'     :0.015,

               'TbtH_1400_LH'     :0.03375,
               'TttH_1400_LH'     :0.011463,
               'TbtH_1400_RH'     :0.03375,
               'TttH_1400_RH'     :0.011463,

               'TbtH_1500_LH'     :0.0255,
               'TttH_1500_LH'     :0.008825,
               'TbtH_1500_RH'     :0.0255,
               'TttH_1500_RH'     :0.008825,

               'TbtH_1600_LH'     :0.019063,
               'TttH_1600_LH'     :0.006763,
               'TbtH_1600_RH'     :0.019063,
               'TttH_1600_RH'     :0.006763,

               'TbtH_1700_LH'     :0.014375,
               'TttH_1700_LH'     :0.00525,
               'TbtH_1700_RH'     :0.014375,
               'TttH_1700_RH'     :0.00525,

               'TbtH_1800_LH_test'     :0.010875,
               'TbtH_1800_LH'     :0.010875,
               'TttH_1800_LH'     :0.00405,
               'TbtH_1800_RH'     :0.010875,
               'TttH_1800_RH'     :0.00324,

             'TbtH_2000_10GeV_LH' :0.006375,
             'TttH_2000_10GeV_RH' :0.002475,

             'TbtH_2200_10GeV_LH' :0.00377,
             'TttH_2200_10GeV_RH' :0.001464,

             'TbtH_2400_10GeV_LH' :0.002261,
             'TttH_2400_10GeV_RH' :0.000878,

             'TbtH_2600_10GeV_LH' :0.001375,
             'TttH_2600_10GeV_RH' :0.000534,

               'TbtH_800_10p_LH'  :0.436874,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_800_10p_RH'  :0.0456,

               'TbtH_1000_10p_LH' :0.139761,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_1000_10p_RH' :0.0254,

               'TbtH_1100_10p_LH' :0.084121,
               'TttH_1100_10p_RH' :0.0190,

               'TbtH_1200_10p_LH' :0.052201,
               'TttH_1200_10p_RH' :0.0145,

               'TbtH_1300_10p_LH' :0.033359,
               'TttH_1300_10p_RH' :0.0112,

               'TbtH_1400_10p_LH' :0.021735,
               'TttH_1400_10p_RH' :0.00865,

               'TbtH_1500_10p_LH' :0.014478,
               'TttH_1500_10p_RH' :0.00675,

               'TbtH_1600_10p_LH' :0.009788,
               'TttH_1600_10p_RH' :0.00525,

               'TbtH_1700_10p_LH' :0.006732,
               'TttH_1700_10p_RH' :0.00413,

               'TbtH_1800_10p_LH' :0.004679,
               'TttH_1800_10p_RH' :0.00324,

               'TbtH_2000_10p_LH' :0.002344,
               'TttH_2000_10p_RH' :0.00203,

               'TbtH_2200_10p_LH' :0.00234,
               'TttH_2200_10p_RH' :0.00203,

               'TbtH_2400_10p_LH' :0.00222,
               'TttH_2400_10p_RH' :0.000283,

               'TbtH_2600_10p_LH' :0.00122,
               'TttH_2600_10p_RH' :0.000155,

               'TbtH_800_20p_LH'  :0.8193,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_800_20p_RH'  :0.0456,

               'TbtH_1000_20p_LH' :0.2645,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_1000_20p_RH' :0.0254,

               'TbtH_1100_20p_LH' :0.1596,
               'TttH_1100_20p_RH' :0.0190,

               'TbtH_1200_20p_LH' :0.0998,
               'TttH_1200_20p_RH' :0.0145,

               'TbtH_1300_20p_LH' :0.064,
               'TttH_1300_20p_RH' :0.0112,

               'TbtH_1400_20p_LH' :0.042,
               'TttH_1400_20p_RH' :0.00865,

               'TbtH_1500_20p_LH' :0.0281,
               'TttH_1500_20p_RH' :0.00675,

               'TbtH_1600_20p_LH' :0.01909,
               'TttH_1600_20p_RH' :0.00525,

               'TbtH_1700_20p_LH' :0.0132,
               'TttH_1700_20p_RH' :0.00413,

               'TbtH_1800_20p_LH' :0.00927,
               'TttH_1800_20p_RH' :0.00324,

               'TbtH_2000_20p_LH' :0.00474,
               'TttH_2000_20p_RH' :0.00203,

               'TbtH_2200_20p_LH' :0.00474,
               'TttH_2200_20p_RH' :0.00203,

               'TbtH_2400_20p_LH' :0.00222,
               'TttH_2400_20p_RH' :0.000283,

               'TbtH_2600_20p_LH' :0.00122,
               'TttH_2600_20p_RH' :0.000155,

               'TbtH_800_30p_LH'  :1.1538,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_800_30p_RH'  :0.330323,

               'TbtH_1000_30p_LH' :0.3747,# *(0.5*0.5)*0.25 = 0.0625
               'TttH_1000_30p_RH' :0.106718,

               'TbtH_1100_30p_LH' :0.2272,
               'TttH_1100_30p_RH' :0.064774,

               'TbtH_1200_30p_LH' :0.14196,
               'TttH_1200_30p_RH' :0.040715,

               'TbtH_1300_30p_LH' :0.0915,
               'TttH_1300_30p_RH' :0.026255,

               'TbtH_1400_30p_LH' :0.0601,
               'TttH_1400_30p_RH' :0.017332,

               'TbtH_1500_30p_LH' :0.04041,
               'TttH_1500_30p_RH' :0.011697,

               'TbtH_1600_30p_LH' :0.02764,
               'TttH_1600_30p_RH' :0.008051,

               'TbtH_1700_30p_LH' :0.0193,
               'TttH_1700_30p_RH' :0.005623,

               'TbtH_1800_30p_LH' :0.01356,
               'TttH_1800_30p_RH' :0.003982,

               'TbtH_2000_30p_LH' :0.00702,
               'TttH_2000_30p_RH' :0.002065,

               'TbtH_2200_30p_LH' :0.00702,
               'TttH_2200_30p_RH' :0.00203,

               'TbtH_2400_30p_LH' :0.00222,
               'TttH_2400_30p_RH' :0.000283,

               'TbtH_2600_30p_LH' :0.00122,
               'TttH_2600_30p_RH' :0.000155,

################# tZ #########################
 
               'TbtZ_800_LH'      :0.24125,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_800_LH'      :0.0665,# *(0.5*0.5)*0.50 = 0.1250
               'TbtZ_800_RH'      :0.24125,
               'TttZ_800_RH'      :0.0665,

               'TbtZ_900_LH'      :0.170,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_900_LH'      :0.0485,# *(0.5*0.5)*0.50 = 0.1250
               'TbtZ_900_RH'      :0.170,
               'TttZ_900_RH'      :0.0485,

               'TbtZ_1000_LH'     :0.121875,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_1000_LH'     :0.035625,# *(0.5*0.5)*0.50 = 0.1250
               'TbtZ_1000_RH'     :0.121875,
               'TttZ_1000_RH'     :0.035625,

               'TbtZ_1100_LH'     :0.084375,
               'TttZ_1100_LH'     :0.0265,
               'TbtZ_1100_RH'     :0.084375,
               'TttZ_1100_RH'     :0.0265,

               'TbtZ_1200_LH'     :0.061375,
               'TttZ_1200_LH'     :0.019875,
               'TbtZ_1200_RH'     :0.061375,
               'TttZ_1200_RH'     :0.019875,

               'TbtZ_1300_LH'     :0.04475,
               'TttZ_1300_LH'     :0.015,
               'TbtZ_1300_RH'     :0.04475,
               'TttZ_1300_RH'     :0.015,

               'TbtZ_1400_LH'     :0.03375,
               'TttZ_1400_LH'     :0.011463,
               'TbtZ_1400_RH'     :0.03375,
               'TttZ_1400_RH'     :0.011463,

               'TbtZ_1500_LH'     :0.0255,
               'TttZ_1500_LH'     :0.008825,
               'TbtZ_1500_RH'     :0.0255,
               'TttZ_1500_RH'     :0.008825,

               'TbtZ_1600_LH'     :0.019063,
               'TttZ_1600_LH'     :0.006763,
               'TbtZ_1600_RH'     :0.019063,
               'TttZ_1600_RH'     :0.006763,

               'TbtZ_1700_LH'     :0.014375,
               'TttZ_1700_LH'     :0.00525,
               'TbtZ_1700_RH'     :0.014375,
               'TttZ_1700_RH'     :0.00525,

               'TbtZ_1800_LH'     :0.010875,
               'TttZ_1800_LH'     :0.00405,
               'TbtZ_1800_RH'     :0.010875,
               'TttZ_1800_RH'     :0.00405,
 
               'TbtZ_800_10p_LH'  :0.4369,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_800_10p_RH'  :0.0456,

               'TbtZ_1000_10p_LH' :0.1398,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_1000_10p_RH' :0.0254,

               'TbtZ_1100_10p_LH' :0.0841,
               'TttZ_1100_10p_RH' :0.0190,

               'TbtZ_1200_10p_LH' :0.0522,
               'TttZ_1200_10p_RH' :0.0145,

               'TbtZ_1300_10p_LH' :0.0334,
               'TttZ_1300_10p_RH' :0.0112,

               'TbtZ_1400_10p_LH' :0.0217,
               'TttZ_1400_10p_RH' :0.00865,

               'TbtZ_1500_10p_LH' :0.01448,
               'TttZ_1500_10p_RH' :0.00675,

               'TbtZ_1600_10p_LH' :0.00979,
               'TttZ_1600_10p_RH' :0.00525,

               'TbtZ_1700_10p_LH' :0.00673,
               'TttZ_1700_10p_RH' :0.00413,

               'TbtZ_1800_10p_LH' :0.00468,
               'TttZ_1800_10p_RH' :0.00324,

               'TbtZ_2000_10p_LH' :0.00234,
               'TttZ_2000_10p_RH' :0.00203,

               'TbtZ_2400_10p_LH' :0.00222,
               'TttZ_2400_10p_RH' :0.000283,

               'TbtZ_2600_10p_LH' :0.00122,
               'TttZ_2600_10p_RH' :0.000155,

               'TbtZ_800_20p_LH'  :0.8193,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_800_20p_RH'  :0.0456,

               'TbtZ_1000_20p_LH' :0.2645,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_1000_20p_RH' :0.0254,

               'TbtZ_1100_20p_LH' :0.1596,
               'TttZ_1100_20p_RH' :0.0190,

               'TbtZ_1200_20p_LH' :0.0998,
               'TttZ_1200_20p_RH' :0.0145,

               'TbtZ_1300_20p_LH' :0.064,
               'TttZ_1300_20p_RH' :0.0112,

               'TbtZ_1400_20p_LH' :0.042,
               'TttZ_1400_20p_RH' :0.00865,

               'TbtZ_1500_20p_LH' :0.0281,
               'TttZ_1500_20p_RH' :0.00675,

               'TbtZ_1600_20p_LH' :0.01909,
               'TttZ_1600_20p_RH' :0.00525,

               'TbtZ_1700_20p_LH' :0.0132,
               'TttZ_1700_20p_RH' :0.00413,

               'TbtZ_1800_20p_LH' :0.00927,
               'TttZ_1800_20p_RH' :0.00324,

               'TbtZ_2000_20p_LH' :0.00474,
               'TttZ_2000_20p_RH' :0.00203,

               'TbtZ_2400_20p_LH' :0.00222,
               'TttZ_2400_20p_RH' :0.000283,

               'TbtZ_2600_20p_LH' :0.00122,
               'TttZ_2600_20p_RH' :0.000155,

               'TbtZ_800_30p_LH'  :1.1538,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_800_30p_RH'  :0.0456,

               'TbtZ_1000_30p_LH' :0.3747,# *(0.5*0.5)*0.25 = 0.0625
               'TttZ_1000_30p_RH' :0.0254,

               'TbtZ_1100_30p_LH' :0.2272,
               'TttZ_1100_30p_RH' :0.0190,

               'TbtZ_1200_30p_LH' :0.14196,
               'TttZ_1200_30p_RH' :0.0145,

               'TbtZ_1300_30p_LH' :0.0915,
               'TttZ_1300_30p_RH' :0.0112,

               'TbtZ_1400_30p_LH' :0.0601,
               'TttZ_1400_30p_RH' :0.00865,

               'TbtZ_1500_30p_LH' :0.04041,
               'TttZ_1500_30p_RH' :0.00675,

               'TbtZ_1600_30p_LH' :0.02764,
               'TttZ_1600_30p_RH' :0.00525,

               'TbtZ_1700_30p_LH' :0.0193,
               'TttZ_1700_30p_RH' :0.00413,

               'TbtZ_1800_30p_LH' :0.01356,
               'TttZ_1800_30p_RH' :0.00324,

               'TbtZ_2000_30p_LH' :0.005454,
               'TttZ_2000_30p_RH' :0.000407,

###################### TprimeTprime ###################################
               
               'TpTp_800': 0.196,
               'TpTp_900': 0.0903,
               'TpTp_1000': 0.0440,
               'TpTp_1100': 0.0224,
               'TpTp_1200': 0.0118,
               'TpTp_1300': 0.00639,
               'TpTp_1400': 0.00354,
               'TpTp_1500': 0.00200,
               'TpTp_1600': 0.001148,
               'TpTp_1700': 0.000666,
               'TpTp_1800': 0.000391,
             }
sampleXsec1pb = {
               'TTJets'       : 831.76,
               'TTJets_test'       : 831.76,
               'TTJetsMtt700' : 831.76 * 0.0921 ,
               'TTJetsMtt1000': 831.76 * 0.02474,
               #'TTJetsMtt700' : 831.76  ,
               #'TTJetsMtt1000': 831.76 ,
               'WJets'        : 95.14,
               'QCDHT100'     : 27540000,
               'QCDHT200'     : 2000000,
               'QCDHT300'     : 351300,
               'QCDHT500'     : 31630,
               'QCDHT700'     : 6831,
               'QCDHT1000'    : 1207,
               'QCDHT1500'    : 119.9,
               'QCDHT2000'    : 25.24,
               'QCDPt80'     : 2735000.,
               'QCDPt120'    : 467500.,
               'QCDPt170'    : 117400., 
               'QCDPt300'    : 7753.,
               'QCDPt470'    : 642.1,
               'QCDPt600'    : 185.9,
               'QCDPt800'    : 32.05,
               'QCDPt1000'   : 9.365,
               'QCDPt1400'   : 0.8398,
               'QCDPt1800'   : 0.1124,
               'QCDPt2400'   : 0.006752,
               'QCDPt3200'   : 0.0001626,
               'ST'           : 35.6,
               'ST_t_top'     : 136.02,
               'ST_t_antitop' : 80.95,
               'ZJets'        : 6.97,
               'DYJets'        : 1187, #LO
               'ttZJets'      : 0.6529, #LO
               'ttHJets'      : 0.295, #LO
               'ttWJets'      : 0.511, #LO
               'tHQ'          : 0.2609,
               'WW'           : 45.2,
               'WZ'           : 23.43,
               'ZZ'           : 6.912,

               'TbtH_800_LH'      :1.0,
               'TttH_800_LH'      :1.0,
               'TbtH_800_RH'      :1.0,
               'TttH_800_RH'      :1.0,

               'TbtH_900_LH'      :1.0,
               'TttH_900_LH'      :1.0,
               'TbtH_900_RH'      :1.0,
               'TttH_900_RH'      :1.0,

               'TbtH_1000_LH'     :1.0,
               'TttH_1000_LH'     :1.0,
               'TbtH_1000_RH'     :1.0,
               'TttH_1000_RH'     :1.0,

               'TbtH_1100_LH'     :1.0,
               'TttH_1100_LH'     :1.0,
               'TbtH_1100_RH'     :1.0,
               'TttH_1100_RH'     :1.0,

               'TbtH_1200_LH'     :1.0,
               'TbtH_1200_LH_test'     :1.0,
               'TttH_1200_LH'     :1.0,
               'TbtH_1200_RH'     :1.0,
               'TttH_1200_RH'     :1.0,

               'TbtH_1300_LH'     :1.0,
               'TttH_1300_LH'     :1.0,
               'TbtH_1300_RH'     :1.0,
               'TttH_1300_RH'     :1.0,

               'TbtH_1400_LH'     :1.0,
               'TttH_1400_LH'     :1.0,
               'TbtH_1400_RH'     :1.0,
               'TttH_1400_RH'     :1.0,

               'TbtH_1500_LH'     :1.0,
               'TttH_1500_LH'     :1.0,
               'TbtH_1500_RH'     :1.0,
               'TttH_1500_RH'     :1.0,

               'TbtH_1600_LH'     :1.0,
               'TttH_1600_LH'     :1.0,
               'TbtH_1600_RH'     :1.0,
               'TttH_1600_RH'     :1.0,

               'TbtH_1700_LH'     :1.0,
               'TttH_1700_LH'     :1.0,
               'TbtH_1700_RH'     :1.0,
               'TttH_1700_RH'     :1.0,

               'TbtH_1800_LH'     :1.0,
               'TbtH_1800_LH_test'     :1.0,
               'TttH_1800_LH'     :1.0,
               'TbtH_1800_RH'     :1.0,
               'TttH_1800_RH'     :1.0,

             'TbtH_2000_10GeV_LH' :1.0,
             'TttH_2000_10GeV_LH' :1.0,
             'TbtH_2000_10GeV_RH' :1.0,
             'TttH_2000_10GeV_RH' :1.0,

             'TbtH_2200_10GeV_LH' :1.0,
             'TttH_2200_10GeV_LH' :1.0,
             'TbtH_2200_10GeV_RH' :1.0,
             'TttH_2200_10GeV_RH' :1.0,

             'TbtH_2400_10GeV_LH' :1.0,
             'TttH_2400_10GeV_LH' :1.0,
             'TbtH_2400_10GeV_RH' :1.0,
             'TttH_2400_10GeV_RH' :1.0,

             'TbtH_2600_10GeV_LH' :1.0,
             'TttH_2600_10GeV_LH' :1.0,
             'TbtH_2600_10GeV_RH' :1.0,
             'TttH_2600_10GeV_RH' :1.0,

               'TbtH_800_10p_LH' :1.0,
               'TttH_800_10p_LH' :1.0,
               'TbtH_800_10p_RH' :1.0,
               'TttH_800_10p_RH' :1.0,

               'TbtH_1000_10p_LH' :1.0,
               'TttH_1000_10p_LH' :1.0,
               'TbtH_1000_10p_RH' :1.0,
               'TttH_1000_10p_RH' :1.0,

               'TbtH_1100_10p_LH' :1.0,
               'TttH_1100_10p_LH' :1.0,
               'TbtH_1100_10p_RH' :1.0,
               'TttH_1100_10p_RH' :1.0,

               'TbtH_1200_10p_LH' :1.0,
               'TttH_1200_10p_LH' :1.0,
               'TbtH_1200_10p_RH' :1.0,
               'TttH_1200_10p_RH' :1.0,

               'TbtH_1300_10p_LH' :1.0,
               'TttH_1300_10p_LH' :1.0,
               'TbtH_1300_10p_RH' :1.0,
               'TttH_1300_10p_RH' :1.0,

               'TbtH_1400_10p_LH' :1.0,
               'TttH_1400_10p_LH' :1.0,
               'TbtH_1400_10p_RH' :1.0,
               'TttH_1400_10p_RH' :1.0,

               'TbtH_1500_10p_LH' :1.0,
               'TttH_1500_10p_LH' :1.0,
               'TbtH_1500_10p_RH' :1.0,
               'TttH_1500_10p_RH' :1.0,

               'TbtH_1600_10p_LH' :1.0,
               'TttH_1600_10p_LH' :1.0,
               'TbtH_1600_10p_RH' :1.0,
               'TttH_1600_10p_RH' :1.0,

               'TbtH_1700_10p_LH' :1.0,
               'TttH_1700_10p_LH' :1.0,
               'TbtH_1700_10p_RH' :1.0,
               'TttH_1700_10p_RH' :1.0,

               'TbtH_1800_10p_LH' :1.0,
               'TttH_1800_10p_LH' :1.0,
               'TbtH_1800_10p_RH' :1.0,
               'TttH_1800_10p_RH' :1.0,

               'TbtH_2000_10p_LH' :1.0,
               'TttH_2000_10p_LH' :1.0,
               'TbtH_2000_10p_RH' :1.0,
               'TttH_2000_10p_RH' :1.0,

               'TbtH_2200_10p_LH' :1.0,
               'TttH_2200_10p_LH' :1.0,
               'TbtH_2200_10p_RH' :1.0,
               'TttH_2200_10p_RH' :1.0,

               'TbtH_2400_10p_LH' :1.0,
               'TttH_2400_10p_LH' :1.0,
               'TbtH_2400_10p_RH' :1.0,
               'TttH_2400_10p_RH' :1.0,

               'TbtH_2600_10p_LH' :1.0,
               'TttH_2600_10p_LH' :1.0,
               'TbtH_2600_10p_RH' :1.0,
               'TttH_2600_10p_RH' :1.0,

               'TbtH_800_20p_LH' :1.0,
               'TttH_800_20p_LH' :1.0,
               'TbtH_800_20p_RH' :1.0,
               'TttH_800_20p_RH' :1.0,

               'TbtH_1000_20p_LH' :1.0,
               'TttH_1000_20p_LH' :1.0,
               'TbtH_1000_20p_RH' :1.0,
               'TttH_1000_20p_RH' :1.0,

               'TbtH_1100_20p_LH' :1.0,
               'TttH_1100_20p_LH' :1.0,
               'TbtH_1100_20p_RH' :1.0,
               'TttH_1100_20p_RH' :1.0,

               'TbtH_1200_20p_LH' :1.0,
               'TttH_1200_20p_LH' :1.0,
               'TbtH_1200_20p_RH' :1.0,
               'TttH_1200_20p_RH' :1.0,

               'TbtH_1300_20p_LH' :1.0,
               'TttH_1300_20p_LH' :1.0,
               'TbtH_1300_20p_RH' :1.0,
               'TttH_1300_20p_RH' :1.0,

               'TbtH_1400_20p_LH' :1.0,
               'TttH_1400_20p_LH' :1.0,
               'TbtH_1400_20p_RH' :1.0,
               'TttH_1400_20p_RH' :1.0,

               'TbtH_1500_20p_LH' :1.0,
               'TttH_1500_20p_LH' :1.0,
               'TbtH_1500_20p_RH' :1.0,
               'TttH_1500_20p_RH' :1.0,

               'TbtH_1600_20p_LH' :1.0,
               'TttH_1600_20p_LH' :1.0,
               'TbtH_1600_20p_RH' :1.0,
               'TttH_1600_20p_RH' :1.0,

               'TbtH_1700_20p_LH' :1.0,
               'TttH_1700_20p_LH' :1.0,
               'TbtH_1700_20p_RH' :1.0,
               'TttH_1700_20p_RH' :1.0,

               'TbtH_1800_20p_LH' :1.0,
               'TttH_1800_20p_LH' :1.0,
               'TbtH_1800_20p_RH' :1.0,
               'TttH_1800_20p_RH' :1.0,

               'TbtH_2000_20p_LH' :1.0,
               'TttH_2000_20p_LH' :1.0,
               'TbtH_2000_20p_RH' :1.0,
               'TttH_2000_20p_RH' :1.0,

               'TbtH_2200_20p_LH' :1.0,
               'TttH_2200_20p_LH' :1.0,
               'TbtH_2200_20p_RH' :1.0,
               'TttH_2200_20p_RH' :1.0,

               'TbtH_2400_20p_LH' :1.0,
               'TttH_2400_20p_LH' :1.0,
               'TbtH_2400_20p_RH' :1.0,
               'TttH_2400_20p_RH' :1.0,

               'TbtH_2600_20p_LH' :1.0,
               'TttH_2600_20p_LH' :1.0,
               'TbtH_2600_20p_RH' :1.0,
               'TttH_2600_20p_RH' :1.0,

               'TbtH_800_30p_LH' :1.0,
               'TttH_800_30p_LH' :1.0,
               'TbtH_800_30p_RH' :1.0,
               'TttH_800_30p_RH' :1.0,

               'TbtH_1000_30p_LH' :1.0,
               'TttH_1000_30p_LH' :1.0,
               'TbtH_1000_30p_RH' :1.0,
               'TttH_1000_30p_RH' :1.0,

               'TbtH_1100_30p_LH' :1.0,
               'TttH_1100_30p_LH' :1.0,
               'TbtH_1100_30p_RH' :1.0,
               'TttH_1100_30p_RH' :1.0,

               'TbtH_1200_30p_LH' :1.0,
               'TttH_1200_30p_LH' :1.0,
               'TbtH_1200_30p_RH' :1.0,
               'TttH_1200_30p_RH' :1.0,

               'TbtH_1300_30p_LH' :1.0,
               'TttH_1300_30p_LH' :1.0,
               'TbtH_1300_30p_RH' :1.0,
               'TttH_1300_30p_RH' :1.0,

               'TbtH_1400_30p_LH' :1.0,
               'TttH_1400_30p_LH' :1.0,
               'TbtH_1400_30p_RH' :1.0,
               'TttH_1400_30p_RH' :1.0,

               'TbtH_1500_30p_LH' :1.0,
               'TttH_1500_30p_LH' :1.0,
               'TbtH_1500_30p_RH' :1.0,
               'TttH_1500_30p_RH' :1.0,

               'TbtH_1600_30p_LH' :1.0,
               'TttH_1600_30p_LH' :1.0,
               'TbtH_1600_30p_RH' :1.0,
               'TttH_1600_30p_RH' :1.0,

               'TbtH_1700_30p_LH' :1.0,
               'TttH_1700_30p_LH' :1.0,
               'TbtH_1700_30p_RH' :1.0,
               'TttH_1700_30p_RH' :1.0,

               'TbtH_1800_30p_LH' :1.0,
               'TttH_1800_30p_LH' :1.0,
               'TbtH_1800_30p_RH' :1.0,
               'TttH_1800_30p_RH' :1.0,

               'TbtH_2000_30p_LH' :1.0,
               'TttH_2000_30p_LH' :1.0,
               'TbtH_2000_30p_RH' :1.0,
               'TttH_2000_30p_RH' :1.0,

               'TbtH_2200_30p_LH' :1.0,
               'TttH_2200_30p_LH' :1.0,
               'TbtH_2200_30p_RH' :1.0,
               'TttH_2200_30p_RH' :1.0,

               'TbtH_2400_30p_LH' :1.0,
               'TttH_2400_30p_LH' :1.0,
               'TbtH_2400_30p_RH' :1.0,
               'TttH_2400_30p_RH' :1.0,

               'TbtH_2600_30p_LH' :1.0,
               'TttH_2600_30p_LH' :1.0,
               'TbtH_2600_30p_RH' :1.0,
               'TttH_2600_30p_RH' :1.0,

################# tZ ##############1.0,##
 
               'TbtZ_800_LH'      :1.0,
               'TttZ_800_LH'      :1.0,
               'TbtZ_800_RH'      :1.0,
               'TttZ_800_RH'      :1.0,

               'TbtZ_900_LH'      :1.0,
               'TttZ_900_LH'      :1.0,
               'TbtZ_900_RH'      :1.0,
               'TttZ_900_RH'      :1.0,

               'TbtZ_1000_LH'     :1.0,
               'TttZ_1000_LH'     :1.0,
               'TbtZ_1000_RH'     :1.0,
               'TttZ_1000_RH'     :1.0,

               'TbtZ_1100_LH'     :1.0,
               'TttZ_1100_LH'     :1.0,
               'TbtZ_1100_RH'     :1.0,
               'TttZ_1100_RH'     :1.0,

               'TbtZ_1200_LH'     :1.0,
               'TttZ_1200_LH'     :1.0,
               'TbtZ_1200_RH'     :1.0,
               'TttZ_1200_RH'     :1.0,

               'TbtZ_1300_LH'     :1.0,
               'TttZ_1300_LH'     :1.0,
               'TbtZ_1300_RH'     :1.0,
               'TttZ_1300_RH'     :1.0,

               'TbtZ_1400_LH'     :1.0,
               'TttZ_1400_LH'     :1.0,
               'TbtZ_1400_RH'     :1.0,
               'TttZ_1400_RH'     :1.0,

               'TbtZ_1500_LH'     :1.0,
               'TttZ_1500_LH'     :1.0,
               'TbtZ_1500_RH'     :1.0,
               'TttZ_1500_RH'     :1.0,

               'TbtZ_1600_LH'     :1.0,
               'TttZ_1600_LH'     :1.0,
               'TbtZ_1600_RH'     :1.0,
               'TttZ_1600_RH'     :1.0,

               'TbtZ_1700_LH'     :1.0,
               'TttZ_1700_LH'     :1.0,
               'TbtZ_1700_RH'     :1.0,
               'TttZ_1700_RH'     :1.0,

               'TbtZ_1800_LH'     :1.0,
               'TttZ_1800_LH'     :1.0,
               'TbtZ_1800_RH'     :1.0,
               'TttZ_1800_RH'     :1.0,
 
               'TbtZ_800_10p_LH'  :1.0,
               'TttZ_800_10p_LH'  :1.0,
               'TttZ_800_10p_RH'  :1.0,

               'TbtZ_1000_10p_LH' :1.0,
               'TttZ_1000_10p_LH' :1.0,
               'TbtZ_1000_10p_RH' :1.0,
               'TttZ_1000_10p_RH' :1.0,

               'TbtZ_1100_10p_LH' :1.0,
               'TttZ_1100_10p_LH' :1.0,
               'TbtZ_1100_10p_RH' :1.0,
               'TttZ_1100_10p_RH' :1.0,

               'TbtZ_1200_10p_LH' :1.0,
               'TttZ_1200_10p_LH' :1.0,
               'TbtZ_1200_10p_RH' :1.0,
               'TttZ_1200_10p_RH' :1.0,

               'TbtZ_1300_10p_LH' :1.0,
               'TttZ_1300_10p_LH' :1.0,
               'TbtZ_1300_10p_RH' :1.0,
               'TttZ_1300_10p_RH' :1.0,

               'TbtZ_1400_10p_LH' :1.0,
               'TttZ_1400_10p_LH' :1.0,
               'TbtZ_1400_10p_RH' :1.0,
               'TttZ_1400_10p_RH' :1.0,

               'TbtZ_1500_10p_LH' :1.0,
               'TttZ_1500_10p_LH' :1.0,
               'TbtZ_1500_10p_RH' :1.0,
               'TttZ_1500_10p_RH' :1.0,

               'TbtZ_1600_10p_LH' :1.0,
               'TttZ_1600_10p_LH' :1.0,
               'TbtZ_1600_10p_RH' :1.0,
               'TttZ_1600_10p_RH' :1.0,

               'TbtZ_1700_10p_LH' :1.0,
               'TttZ_1700_10p_LH' :1.0,
               'TbtZ_1700_10p_RH' :1.0,
               'TttZ_1700_10p_RH' :1.0,

               'TbtZ_1800_10p_LH' :1.0,
               'TttZ_1800_10p_LH' :1.0,
               'TbtZ_1800_10p_RH' :1.0,
               'TttZ_1800_10p_RH' :1.0,

               'TbtZ_2000_10p_LH' :1.0,
               'TttZ_2000_10p_LH' :1.0,
               'TbtZ_2000_10p_RH' :1.0,
               'TttZ_2000_10p_RH' :1.0,

               'TbtZ_2400_10p_LH' :1.0,
               'TttZ_2400_10p_LH' :1.0,
               'TbtZ_2400_10p_RH' :1.0,
               'TttZ_2400_10p_RH' :1.0,

               'TbtZ_2600_10p_LH' :1.0,
               'TttZ_2600_10p_LH' :1.0,
               'TbtZ_2600_10p_RH' :1.0,
               'TttZ_2600_10p_RH' :1.0,

               'TbtZ_800_20p_LH'  :1.0,
               'TttZ_800_20p_LH'  :1.0,
               'TttZ_800_20p_RH'  :1.0,

               'TbtZ_1000_20p_LH' :1.0,
               'TttZ_1000_20p_LH' :1.0,
               'TbtZ_1000_20p_RH' :1.0,
               'TttZ_1000_20p_RH' :1.0,

               'TbtZ_1100_20p_LH' :1.0,
               'TttZ_1100_20p_LH' :1.0,
               'TbtZ_1100_20p_RH' :1.0,
               'TttZ_1100_20p_RH' :1.0,

               'TbtZ_1200_20p_LH' :1.0,
               'TttZ_1200_20p_LH' :1.0,
               'TbtZ_1200_20p_RH' :1.0,
               'TttZ_1200_20p_RH' :1.0,

               'TbtZ_1300_20p_LH' :1.0,
               'TttZ_1300_20p_LH' :1.0,
               'TbtZ_1300_20p_RH' :1.0,
               'TttZ_1300_20p_RH' :1.0,

               'TbtZ_1400_20p_LH' :1.0,
               'TttZ_1400_20p_LH' :1.0,
               'TbtZ_1400_20p_RH' :1.0,
               'TttZ_1400_20p_RH' :1.0,

               'TbtZ_1500_20p_LH' :1.0,
               'TttZ_1500_20p_LH' :1.0,
               'TbtZ_1500_20p_RH' :1.0,
               'TttZ_1500_20p_RH' :1.0,

               'TbtZ_1600_20p_LH' :1.0,
               'TttZ_1600_20p_LH' :1.0,
               'TbtZ_1600_20p_RH' :1.0,
               'TttZ_1600_20p_RH' :1.0,

               'TbtZ_1700_20p_LH' :1.0,
               'TttZ_1700_20p_LH' :1.0,
               'TbtZ_1700_20p_RH' :1.0,
               'TttZ_1700_20p_RH' :1.0,

               'TbtZ_1800_20p_LH' :1.0,
               'TttZ_1800_20p_LH' :1.0,
               'TbtZ_1800_20p_RH' :1.0,
               'TttZ_1800_20p_RH' :1.0,

               'TbtZ_2000_20p_LH' :1.0,
               'TttZ_2000_20p_LH' :1.0,
               'TbtZ_2000_20p_RH' :1.0,
               'TttZ_2000_20p_RH' :1.0,

               'TbtZ_2400_20p_LH' :1.0,
               'TttZ_2400_20p_LH' :1.0,
               'TbtZ_2400_20p_RH' :1.0,
               'TttZ_2400_20p_RH' :1.0,

               'TbtZ_2600_20p_LH' :1.0,
               'TttZ_2600_20p_LH' :1.0,
               'TbtZ_2600_20p_RH' :1.0,
               'TttZ_2600_20p_RH' :1.0,

               'TbtZ_800_30p_LH'  :1.0,
               'TttZ_800_30p_RH'  :1.0,

               'TbtZ_1000_30p_LH' :1.0,
               'TttZ_1000_30p_LH' :1.0,
               'TbtZ_1000_30p_RH' :1.0,
               'TttZ_1000_30p_RH' :1.0,

               'TbtZ_1100_30p_LH' :1.0,
               'TttZ_1100_30p_LH' :1.0,
               'TbtZ_1100_30p_RH' :1.0,
               'TttZ_1100_30p_RH' :1.0,

               'TbtZ_1200_30p_LH' :1.0,
               'TttZ_1200_30p_LH' :1.0,
               'TbtZ_1200_30p_RH' :1.0,
               'TttZ_1200_30p_RH' :1.0,

               'TbtZ_1300_30p_LH' :1.0,
               'TttZ_1300_30p_LH' :1.0,
               'TbtZ_1300_30p_RH' :1.0,
               'TttZ_1300_30p_RH' :1.0,

               'TbtZ_1400_30p_LH' :1.0,
               'TttZ_1400_30p_LH' :1.0,
               'TbtZ_1400_30p_RH' :1.0,
               'TttZ_1400_30p_RH' :1.0,

               'TbtZ_1500_30p_LH' :1.0,
               'TttZ_1500_30p_LH' :1.0,
               'TbtZ_1500_30p_RH' :1.0,
               'TttZ_1500_30p_RH' :1.0,

               'TbtZ_1600_30p_LH' :1.0,
               'TttZ_1600_30p_LH' :1.0,
               'TbtZ_1600_30p_RH' :1.0,
               'TttZ_1600_30p_RH' :1.0,

               'TbtZ_1700_30p_LH' :1.0,
               'TttZ_1700_30p_LH' :1.0,
               'TbtZ_1700_30p_RH' :1.0,
               'TttZ_1700_30p_RH' :1.0,

               'TbtZ_1800_30p_LH' :1.0,
               'TttZ_1800_30p_LH' :1.0,
               'TbtZ_1800_30p_RH' :1.0,
               'TttZ_1800_30p_RH' :1.0,

               'TbtZ_2000_30p_LH' :1.0,
               'TttZ_2000_30p_LH' :1.0,
               'TbtZ_2000_30p_RH' :1.0,
               'TttZ_2000_30p_RH' :1.0, 
###################### TprimeTprime ###################################
               
               'TpTp_800': 0.13099,
               'TpTp_900': 0.061922,
               'TpTp_1000': 0.030953,
               'TpTp_1100': 0.016141,
               'TpTp_1200': 0.0087015,
               'TpTp_1300': 0.0048327,
               'TpTp_1400': 0.0027375,
               'TpTp_1500': 0.0015875,
               'TpTp_1600': 0.00093471,
               'TpTp_1700': 0.00055711,
               'TpTp_1800': 0.00033677,
             }

plotDictBkgr = {
               'QCD'    : {
                            'Legend': "Multijets       ",
                            'Color' : 16,
                          }, 
               'TTJets' : {
                            'Legend': "t#bar{t}+jets   " ,
                            'Color' : 26,
                          },
               'WJets'  : {
                            'Legend': "W+jets          ",
                            'Color' : 36,
                          },
               #'ST'     : {
               #             'Legend':  "Single top: tW  ",
               #             'Color' : 46,
               #           },
               'ST_t'     : {
                            'Legend':  "Single top: t-channel  ",
                            'Color' : 48,
                          },
               'ZJets'  : {
                            'Legend': "Z+jets          ",
                            'Color' : 12,
                          },
               'ttZJets': {
                            'Legend': "ttZ+jets        ",
                            'Color' : 31,
                          },
               'ttWJets': {
                            'Legend': "ttW+jets        ",
                            'Color' : 21,
                          },
               'ttHJets': {
                            'Legend': "ttH+jets        ",
                            'Color' : 28,
                          },
               #'WW'     : {
               #             'Legend': "WW              ",
               #             'Color' : 38,
               #           },
               #'ZZ'     : {
               #             'Legend': "ZZ              ",
               #             'Color' : 42,
               #           },
               'tHQ'    : {
                            'Legend': "tHQ             ",
                            'Color' : 41,
                          },
               #'DYJets' : {
               #             'Legend': "DY+jets         ",
               #             'Color' : 28,
               #           },
               }
plotDictBkgrCompare = {

  'regionA_QCD' : {
    'Legend' : 'Region A',
    'Color'  : 1,
    'Line'   : 1,
    'Fill'   : 3305
  },
  'regionB_QCD' : {
    'Legend' : 'Region B',
    'Color'  : 2,
    'Line'   : 1,
    'Fill'   : 3335
  },
#  'regionC_QCD' : {
#    'Legend' : 'Region C',
#    'Color'  : 3,
#    'Line'   : 1,
#    'Fill'   : 3353
#  },
#  'regionD_MC_QCD' : {
#    'Legend' : 'Region D',
#    'Color'  : 4,
#    'Line'   : 1,
#    'Fill'   : 3395
#  },
#  'regionA_QCD' : {
#    'Legend' : 'Region W',
#    'Color'  : 1,
#    'Line'   : 1,
#    'Fill'   : 3305
#  },
#  'regionB_QCD' : {
#    'Legend' : 'Region X',
#    'Color'  : 2,
#    'Line'   : 1,
#    'Fill'   : 3335
#  },
#  'regionC_QCD' : {
#    'Legend' : 'Region Y',
#    'Color'  : 3,
#    'Line'   : 1,
#    'Fill'   : 3353
#  },
#  'regionD_MC_QCD' : {
#    'Legend' : 'Region Z',
#    'Color'  : 4,
#    'Line'   : 1,
#    'Fill'   : 3395
#  },
 }

plotDictBkgrTemp = {
               'QCD'    : {
                            'Legend': "Multijets       ",
                            'Color' : 16,
                          }, 
               'TTJets' : {
                            'Legend': "t#bar{t}+jets   " ,
                            'Color' : 26,
                          },
               'Other'  : {
                            'Legend': "Other           ",
                            'Color' : 36,
                          },
}
sigScaled = {
                  'TbtH_1200_00p_LH' : {
                                     'Scale' : '10',
                                   },
                  'TbtH_1200_LH' : {
                                     'Scale' : '10',
                                   },
                  'TbtH_1800_00p_LH' : {
                                     'Scale' : '10',
                                   },
                  'TbtH_1800_LH' : {
                                     'Scale' : '10',
                                   },
                  'TbtH_2600_10p_LH' : { 
                                     'Scale' : '10',
                                   },

                  'TttH_1200_RH' : {
                                     'Scale' : '10',
                                   },
                  'TttH_1800_RH' : {
                                     'Scale' : '10',
                                   },
                  'TttH_2600_10p_RH' : {
                                     'Scale' : '10',
                                   },

                  'TbtZ_1200_LH' : { 
                                     'Scale' : '10',
                                   },
                  'TbtZ_1800_LH' : {
                                     'Scale' : '10',
                                   },
                  'TbtZ_1200_00p_LH' : { 
                                     'Scale' : '10',
                                   },
                  'TbtZ_1800_00p_LH' : {
                                     'Scale' : '10',
                                   },
                  'TttZ_1200_RH' : { 
                                     'Scale' : '10',
                                   },
                  'TttZ_1800_RH' : {
                                     'Scale' : '10',
                                   },
                 }
plotDictSignal = {
#                  'TbtH_1200_00p_LH' : {
#                                     'Legend': "#splitline{Tbq, M(T) = 1200 GeV}{"+str(sampleXsec1pb['TbtH_1200_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq, M(T) = 1200 GeV}{"+sigScaled['TbtH_1200_00p_LH']['Scale']+'x'+str(sampleXsec1pb['TbtH_1200_LH'])+" pb xsec.}",
#                                     'Color' : 4,
#                                     'Scale' : 10,
#                                   },
#                  'TbtH_1800_00p_LH' : {
#                                     'Legend': "#splitline{Tbq, M(T) = 1800 GeV}{"+str(sampleXsec1pb['TbtH_1800_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq, M(T) = 1800 GeV}{"+sigScaled['TbtH_1800_00p_LH']['Scale']+'x'+str(sampleXsec1pb['TbtH_1800_LH'])+" pb xsec.}",
#                                     'Color' : 3,
#                                     'Scale' : 10,
#                                   },
#                  'TbtH_1200_LH' : {
#                                     'Legend': "#splitline{Tbq, M(T) = 1200 GeV}{"+str(sampleXsec['TbtH_1200_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq, M(T) = 1200 GeV}{"+sigScaled['TbtH_1200_LH']['Scale']+'x'+str(sampleXsec['TbtH_1200_LH'])+" pb xsec.}",
#                                     'Color' : 4,
#                                     'Scale' : 10,
#                                   },
#                  'TbtH_1800_LH' : {
#                                     'Legend': "#splitline{Tbq, M(T) = 1800 GeV}{"+str(sampleXsec['TbtH_1800_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq, M(T) = 1800 GeV}{"+sigScaled['TbtH_1800_LH']['Scale']+'x'+str(sampleXsec['TbtH_1800_LH'])+" pb xsec.}",
#                                     'Color' : 3,
#                                     'Scale' : 10,
#                                   },
#                  'TbtH_2600_10p_LH' : { 
#                                     'Legend' : "#splitline{Tbq, M(T) = 2600 GeV}{"+str(sampleXsec['TbtH_2600_10p_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq, M(T) = 2600 GeV}{"+sigScaled['TbtH_2600_10p_LH']['Scale']+'x'+str(sampleXsec['TbtH_2600_10p_LH'])+" pb xsec.}",
#                                     'Color' : 2,
#                                     'Scale' : 10,
#                                   },
#
#                  'TttH_1200_RH' : {
#                                     'Legend' : "#splitline{Ttq, M(T) = 1200 GeV}{"+str(sampleXsec['TttH_1800_RH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Ttq, M(T) = 1200 GeV}{"+sigScaled['TttH_1200_RH']['Scale']+'x'+str(sampleXsec['TttH_1200_RH'])+" pb xsec.}",
#                                     'Color' : 7,
#                                     'Scale' : 10,
#                                   },
#                  'TttH_1800_RH' : {
#                                     'Legend' : "#splitline{Ttq, M(T) = 1800 GeV}{"+str(sampleXsec['TttH_1800_RH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Ttq, M(T) = 1800 GeV}{"+sigScaled['TttH_1800_RH']['Scale']+'x'+str(sampleXsec['TttH_1800_RH'])+" pb xsec.}",
#                                     'Color' : 6,
#                                     'Scale' : 10,
#                                   },
#                  'TttH_2600_10p_RH' : {
#                                         'Legend' : "#splitline{Ttq, M(T) = 2600 GeV}{"+str(sampleXsec['TttH_2600_10p_RH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Ttq, M(T) = 2600 GeV}{"+sigScaled['TttH_2600_10p_RH']['Scale']+'x'+str(sampleXsec['TttH_2600_10p_RH'])+" pb xsec.}",
#                                     'Color' : 2,
#                                     'Scale' : 10,
#                                   },
#
                  'TbtZ_1200_00p_LH' : { 
                                     'Legend' : "#splitline{Tbq#rightarrow tZ, M(T) = 1200 GeV}{"+str(sampleXsec1pb['TbtZ_1200_LH'])+" pb xsec.}",
                                     'LegendScaled': "#splitline{Tbq#rightarrow tZ, M(T) = 1200 GeV}{"+sigScaled['TbtZ_1200_00p_LH']['Scale']+'x'+str(sampleXsec1pb['TbtZ_1200_LH'])+" pb xsec.}",
                                     'Color' : 2,
                                     'Scale' : 10,
                                   },
                  'TbtZ_1800_00p_LH' : {
                                     'Legend' : "#splitline{Tbq#rightarrow tZ, M(T) = 1800 GeV}{"+str(sampleXsec1pb['TbtZ_1800_LH'])+" pb xsec.}",
                                     'LegendScaled': "#splitline{Tbq#rightarrow tZ, M(T) = 1800 GeV}{"+sigScaled['TbtZ_1800_00p_LH']['Scale']+'x'+str(sampleXsec1pb['TbtZ_1800_LH'])+" pb xsec.}",
                                     'Color' : 8,
                                     'Scale' : 10,
                                   },
#                  'TbtZ_1200_LH' : { 
#                                     'Legend' : "#splitline{Tbq#rightarrow tZ, M(T) = 1200 GeV}{"+str(sampleXsec['TbtZ_1200_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq#rightarrow tZ, M(T) = 1200 GeV}{"+sigScaled['TbtZ_1200_LH']['Scale']+'x'+str(sampleXsec['TbtZ_1200_LH'])+" pb xsec.}",
#                                     'Color' : 2,
#                                     'Scale' : 10,
#                                   },
#                  'TbtZ_1800_LH' : {
#                                     'Legend' : "#splitline{Tbq#rightarrow tZ, M(T) = 1800 GeV}{"+str(sampleXsec['TbtZ_1800_LH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Tbq#rightarrow tZ, M(T) = 1800 GeV}{"+sigScaled['TbtZ_1800_LH']['Scale']+'x'+str(sampleXsec['TbtZ_1800_LH'])+" pb xsec.}",
#                                     'Color' : 8,
#                                     'Scale' : 10,
#                                   },
#                  'TttZ_1200_RH' : {
#                                     'Legend' : "#splitline{Ttq#rightarrow tZ, M(T) = 1200 GeV}{"+str(sampleXsec['TttZ_1800_RH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Ttq#rightarrow tZ, M(T) = 1200 GeV}{"+sigScaled['TttZ_1200_RH']['Scale']+'x'+str(sampleXsec['TttZ_1200_RH'])+" pb xsec.}",
#                                     'Color' : 7,
#                                     'Scale' : 10,
#                                   },
#                  'TttZ_1800_RH' : {
#                                     'Legend' : "#splitline{Ttq#rightarrow tZ, M(T) = 1800 GeV}{"+str(sampleXsec['TttZ_1800_RH'])+" pb xsec.}",
#                                     'LegendScaled': "#splitline{Ttq#rightarrow tZ, M(T) = 1800 GeV}{"+sigScaled['TttZ_1800_RH']['Scale']+'x'+str(sampleXsec['TttZ_1800_RH'])+" pb xsec.}",
#                                     'Color' : 6,
#                                     'Scale' : 10,
#                                   },
                 }
