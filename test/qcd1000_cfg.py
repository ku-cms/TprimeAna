import FWCore.ParameterSet.Config as cms


from Analysis.VLQAna.JetSelector_cfi import *

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	'file:/home/t3-ku/erichjs/store/b2g/Spring15/QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/crab_b2ganafw74xV2_QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/150629_145644/0000/B2GEDMNtuple_10.root',
#	'file:/home/t3-ku/erichjs/store/b2g/Spring15/QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/crab_b2ganafw74xV2_QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/150629_145644/0000/B2GEDMNtuple_11.root',
#	'file:/home/t3-ku/erichjs/store/b2g/Spring15/QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/crab_b2ganafw74xV2_QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/150629_145644/0000/B2GEDMNtuple_12.root',
#	'file:/home/t3-ku/erichjs/store/b2g/Spring15/QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/crab_b2ganafw74xV2_QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/150629_145644/0000/B2GEDMNtuple_13.root',
#	'file:/home/t4-ku/erichjs/store/b2g/Spring15/QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/crab_b2ganafw74xV2_QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/150629_145644/0000/B2GEDMNtuple_14.root',
    )
)

process.analyze = cms.EDAnalyzer('TprimeAna'
)

from Analysis.VLQAna.JetSelector_cfi import *
from Analysis.VLQAna.VLQAna_cfi import *

process.load ("Analysis.VLQAna.HbbCandidateProducer_cfi") 

process.load ("UserCode.TprimeAna.presel_cfi")


process.TFileService = cms.Service("TFileService", fileName = cms.string('QCD1000.root') )


process.p = cms.Path(process.hbb*process.presel*process.analyze)
#process.p = cms.Path(process.hbb)

#process.outpath = cms.EndPath(process.out)
#process.p = cms.Schedule(p2)

