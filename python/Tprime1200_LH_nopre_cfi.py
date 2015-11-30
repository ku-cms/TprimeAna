import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'root://xrootd.unl.edu//store/group/phys_b2g/B2GAnaFW/TprimeBToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_v74x_v6p1_25ns/150930_172819/0000/B2GEDMNtuple_1.root',
        'root://xrootd.unl.edu//store/group/phys_b2g/B2GAnaFW/TprimeBToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_v74x_v6p1_25ns/150930_172819/0000/B2GEDMNtuple_2.root',
        'root://xrootd.unl.edu//store/group/phys_b2g/B2GAnaFW/TprimeBToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_v74x_v6p1_25ns/150930_172819/0000/B2GEDMNtuple_3.root',
        'root://xrootd.unl.edu//store/group/phys_b2g/B2GAnaFW/TprimeBToTH_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_v74x_v6p1_25ns/150930_172819/0000/B2GEDMNtuple_4.root',
    )
)

