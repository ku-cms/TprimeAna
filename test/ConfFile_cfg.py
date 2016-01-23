import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ()

options.register ('dataset',
				  'none',
				  VarParsing.multiplicity.singleton,
				  VarParsing.varType.string,
				  "Dataset to process")
options.parseArguments()

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


print 'dataset=',options.dataset

from Analysis.VLQAna.JetSelector_cfi import *
from Analysis.VLQAna.VLQAna_cfi import *

process.load ("Analysis.VLQAna.HbbCandidateProducer_cfi")
process.load ("UserCode.TprimeAna.presel_cfi")

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
#    fileNames = cms.untracked.vstring(
#        'file:/home/t3-ku/erichjs/store/b2g/PHYS14/TprimeJetToTH_allHdecays_M800GeV_Tune4C_13TeV-madgraph-tauola/TprimeTH_allHdecays_M800GeV_edmntuple_B2GAnaFWvHEADFeb12/150212_151031/0000/B2GEDMNtuple_1.root',
    fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_v74x_V6p1_25ns_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/150929_133729/0000/B2GEDMNtuple_2.root')

)


process.TFileService = cms.Service("TFileService", fileName = cms.string(options.dataset+".root") )


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("PreselEvents_"+options.dataset+".root"),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('p')
      ),
    outputCommands = cms.untracked.vstring(
      "drop *",
      "keep *_eventInfo_*_*",
      "keep *_met_*_*",
      "keep *_jetsAK4_*_*",
      "keep *_jetsAK8_*_*",
      "keep *_AK8Jets_*_*",
      "keep *_subjetsAK8_*_*",
      "keep *_subjetsCmsTopTag_*_*",
      "keep *_hbb_*_*",
      "keep *_presel_*_*",
      )
    )

#process.p = cms.Path(process.hbb*process.presel)
process.p = cms.Path(process.presel)

process.outpath = cms.EndPath(process.out)
