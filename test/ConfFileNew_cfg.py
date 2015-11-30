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


print 'dataset=',options.dataset


process.load("Analysis.Presel.Presel_cfi")

process.presel.hltPaths = cms.vstring ( "HLT_PFHT650.*","HLT_PFHT800_.*","HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v.*","HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45_v.*" )
process.presel.isData = cms.bool (False)
process.presel.skipEvents = cms.string("")
process.presel.weightFileName = cms.string("triggers_data_Run2015D_05Oct2015.root")
process.presel.weights = cms.vstring ("trig/eff_htak4_HLT_PFHT800_v","trig/eff_htak4_HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v","trig/eff_htak4_HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45_v")


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/home/t3-ku/erichjs/store/b2g/Spring15/TToTH/TprimeTToTH_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/TprimeTToTH_M-1000_LH/150620_210942/0000/B2GEDMNtuple_1.root',)
#    fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_v74x_V6p1_25ns_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/150929_133729/0000/B2GEDMNtuple_3.root')

)


process.TFileService = cms.Service("TFileService", fileName = cms.string(options.dataset+".root") )


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("PreselEvents_"+options.dataset+".root"),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('p')
      ),
    outputCommands = cms.untracked.vstring(
      "drop *",
      "keep *_genPart_*_*",
      "keep *_eventInfo_*_*",
      "keep *_met_*_*",
      "keep *_jetsAK4_*_*",
      "keep *_jetsAK8_*_*",
      "keep *_AK8Jets_*_*",
      "keep *_subjetsAK8_*_*",
      "keep *_subjetsCmsTopTag_*_*",
      "keep *_hbb_*_*",
      "keep *_presel_*_*",
      "keep *_TriggerUserData_*_*",
      "keep *_eventUserData_*_*"
      )
    )

#process.p = cms.Path(process.hbb*process.presel)
process.p = cms.Path(process.presel)

process.outpath = cms.EndPath(process.out)
