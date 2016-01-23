import FWCore.ParameterSet.Config as cms


from Analysis.VLQAna.JetSelector_cfi import *

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/home/t3-ku/erichjs/store/b2g/Spring15/TToTH/TprimeTToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/TprimeTToTH_M-1200_LH/150620_211013/0000/B2GEDMNtuple_1.root'
    )
)

process.analyze = cms.EDAnalyzer('TprimeAna'
)
process.load ("UserCode.TprimeAna.presel_cfi")


process.TFileService = cms.Service("TFileService", fileName = cms.string('Tprime1200_LH_900trig.root') )

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("SingleTprime800AnaEvts.root"),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('p')
      ),
    outputCommands = cms.untracked.vstring(
      "drop *",
      "keep *_genPart_*_*",
      "keep *_jetsAK4_*_*",
      "keep *_jetsAK8_*_*",
      "keep *_*_npv_*",
      "keep *_subjets*_*_*",
      "keep *_ana_*_*",
      "keep *_vjj_*_*",
      )
    )

process.p = cms.Path(process.presel*process.analyze)
#process.p = cms.Path(process.presel)

#process.p = cms.Schedule(p2)
#process.outpath = cms.EndPath(process.out)
