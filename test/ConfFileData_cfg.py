import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ()

options.register ('dataset',
				  'none',
				  VarParsing.multiplicity.singleton,
				  VarParsing.varType.string,
				  "Dataset to process")
options.parseArguments()

process = cms.Process("Preselection")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.options = cms.untracked.PSet(
	SkipEvent = cms.untracked.vstring('ProductNotFound')
)

print 'dataset=',options.dataset

process.load("Analysis.Presel.Presel_cfi")


process.presel.hltPaths = cms.vstring ( ".*")
process.presel.isData = cms.bool (True);

process.presel.skipEvents = cms.string ("256729,1230,1731872311");

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/home/t3-ku/erichjs/store/b2g/PHYS14/TprimeJetToTH_allHdecays_M800GeV_Tune4C_13TeV-madgraph-tauola/TprimeTH_allHdecays_M800GeV_edmntuple_B2GAnaFWvHEADFeb12/150212_151031/0000/B2GEDMNtuple_1.root',
#	'root://cmsxrootd.fnal.gov//store/user/knash/JetHT/crab_Run2015D-PromptReco-v4_Sep25_v74x_V7_25ns/150925_193904/0000/B2GEDMNtuple_46.root'    
	'root://cmsxrootd.fnal.gov//store/user/knash/JetHT/crab_Run2015D-PromptReco-v3_Oct9_v74x_V7_25ns_v2/151013_175415/0000/B2GEDMNtuple_1.root')
)


process.TFileService = cms.Service("TFileService", fileName = cms.string(options.dataset+".root") )


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("PreselEvents_"+options.dataset+".root"),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('p')
      ),
    outputCommands = cms.untracked.vstring(
      "drop *",
      "keep *_METUserData_*_*",
      "keep *_TriggerUserData_*_*",
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
