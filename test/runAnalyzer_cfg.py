import FWCore.ParameterSet.Config as cms

from Analysis.VLQAna.JetSelector_cfi import *
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ()

options.register ('dataset',
                                  'none',
                                  VarParsing.multiplicity.singleton,
                                  VarParsing.varType.string,
                                  "Dataset to process")
options.parseArguments()

process = cms.Process("Analyze")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load("UserCode.TprimeAna."+options.dataset+"_cfi")
process.load("Analysis.VLQAna.HbbCandidateProducer_cfi")
process.load("UserCode.AnaVars.AnaVars_cfi")


process.genfilter = cms.EDFilter('GenPartFilter'
)

process.analyze = cms.EDAnalyzer('TprimeAna',
	    trigNameLabel              = cms.InputTag("TriggerUserData", "triggerNameTree"),
            trigBitLabel               = cms.InputTag("TriggerUserData", "triggerBitTree"),
            isData 			= cms.bool(False),
#       	    hltPaths                   = cms.vstring ( ".*")
       	    hltPaths                   = cms.vstring ( "HLT_PFHT800.*")
 
)


process.TFileService = cms.Service("TFileService", fileName = cms.string(options.dataset+'.root') )

if options.dataset[0:6] == "Tprime":
	process.p = cms.Path(process.genfilter*process.anavars*process.analyze)
else:
	process.p = cms.Path(process.anavars*process.analyze)
#	process.p = cms.Path(process.analyze)

#process.p = cms.Schedule(p2)

