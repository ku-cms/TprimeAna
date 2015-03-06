import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/home/t3-ku/erichjs/store/b2g/PHYS14/TprimeJetToTH_allHdecays_M800GeV_Tune4C_13TeV-madgraph-tauola/TprimeTH_allHdecays_M800GeV_edmntuple_B2GAnaFWvHEADFeb12/150212_151031/0000/B2GEDMNtuple_1.root',
    )
)

process.demo = cms.EDAnalyzer('TprimeAna'
)

process.TFileService = cms.Service("TFileService", fileName = cms.string('Tprime800.root') )

process.p = cms.Path(process.demo)
