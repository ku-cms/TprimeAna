#!/usr/bin/env python

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

Backgrounds = {
                'TTJets'     : dirSamples + 'TTJets_powheg.root',
                'WJets'      : dirSamples + 'WJets.root',
                'QCDHT700'   : dirSamples + 'QCDHT700.root',
                'QCDHT1000'  : dirSamples + 'QCDHT1000.root',
                'QCDHT1500'  : dirSamples + 'QCDHT1500.root',
                'QCDHT2000'  : dirSamples + 'QCDHT2000.root',
                'ST_antitop' : dirSamples + 'ST_antitop.root',
                'ST_top'     : dirSamples + 'ST_top.root',
                'ZJets'      : dirSamples + 'ZJets.root'
              }
Signals = {
            'TbtZ_1200_LH' : dirSamples + 'TbtZ_1200_LH.root'
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
               'ZJets'        : 6.97,
               'TbtZ_1200_LH' : 1.0
             }

# Dictionary containing the information for each variable to be retrieved
treeVarList = {
                'ht' : {
                         'Wts'   : 'EvtWeight*EvtWtPV',
                         'Cuts'  : 'ht>1100',
                         'xMin'  : 1100,
                         'xMax'  : 2700,
                         'nBins' : 20,
                         'log'   : True
                       }
              }

preselDict = {
                'ht' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : 1100,
                    'xMax'   : 2700,
                    'nBins'  : 20,
                    'xLabel' : 'H_{T} [GeV]',
                    'yLabel' : 'Events/80GeV',
                    'log'    : True
                  },
                'PrunedMassAK8' 
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : 0,
                    'xMax'   : 800,
                    'nBins'  : 40,
                    'xLabel' : 'Pruned Mass [GeV]',
                    'yLabel' : 'Jets',
                    'log'    : True
                  },
                'tau2AK8/tau1AK8'
                : {
                    'Wts'    : 'EvtWeight*EvtWtPV',
                    'Cuts'   : 'ht>1100',
                    'xMin'   : 0, 
                    'xMax'   : 1, 
                    'nBins'  : 50,
                    'xLabel' : '#tau_{21}',
                    'yLabel' : 'Jets',
                    'log'    : True 
                  }
             }
