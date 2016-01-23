import FWCore.ParameterSet.Config as cms


from Analysis.VLQAna.JetSelector_cfi import *

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	'file:/home/t3-ku/erichjs/store/b2g/Spring15/TToTH/TprimeTToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/TprimeTToTH_M-1200_LH/150620_211013/0000/B2GEDMNtuple_1.root',
	'file:/home/t3-ku/erichjs/store/b2g/Spring15/TToTH/TprimeTToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/TprimeTToTH_M-1200_LH/150620_211013/0000/B2GEDMNtuple_2.root',
	'file:/home/t3-ku/erichjs/store/b2g/Spring15/TToTH/TprimeTToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/TprimeTToTH_M-1200_LH/150620_211013/0000/B2GEDMNtuple_3.root',
	'file:/home/t3-ku/erichjs/store/b2g/Spring15/TToTH/TprimeTToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/TprimeTToTH_M-1200_LH/150620_211013/0000/B2GEDMNtuple_4.root',
    )
)

process.analyze = cms.EDAnalyzer('TprimeAna'
)

from Analysis.VLQAna.JetSelector_cfi import *
from Analysis.VLQAna.VLQAna_cfi import *

process.load ("Analysis.VLQAna.HbbCandidateProducer_cfi") 
process.load ("UserCode.TprimeAna.presel_cfi")



process.TFileService = cms.Service("TFileService", fileName = cms.string('Tprime1200_LH.root') )


process.p = cms.Path(process.hbb*process.presel*process.analyze)
#process.p = cms.Path(process.hbb)

#process.outpath = cms.EndPath(process.out)
#process.p = cms.Schedule(p2)

